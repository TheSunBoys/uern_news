import os
import urllib.request
import xml.etree.ElementTree as ET

def downloadXML(*urls):
    if os.path.exists(".database") == False:
        os.mkdir(".database")

    for i in range(len(urls)):
        urllib.request.urlretrieve(urls[i], f".database/.new{i}.xml")


class AnalyzeRSS():
    def __init__(self, directory = ".database"):
        self._dir = directory

    def _xtractData(self, files):
        message = list()

        for file in files:
            root = ET.parse(file).getroot()
            itemElement = root.findall("channel/item")

            for i in itemElement:
                title = i[0].text
                link = i[1].text

                message.append(f"{title}\n{link}")

        return message

    def _searchFiles(self, name):
        length = 0
        files = os.listdir(self._dir)

        for file in files:
            if file[1:4] == name:
                length += 1

        if length > 0:
            filenames = [f"{self._dir}/.{name}{x}.xml" for x in range(length)]
            return self._xtractData(filenames)
        else:
            return False


    def _updateFilenames(self):
        files = os.listdir(self._dir)

        for file in files:
            if file[1:4] == "old":
                os.remove(f"{self._dir}/"+file)

        for file in files:
            if file[1:4] == "new":
                os.rename(f"{self._dir}/"+file, f"{self._dir}/.old"+file[4:])

    def getData(self):
        newMessage = self._searchFiles("new")
        oldMessage = self._searchFiles("old")

        # delete duplicates
        if oldMessage != False:
            for element in oldMessage:
                if element in newMessage:
                    del(newMessage[newMessage.index(element)])

        self._updateFilenames()

        return newMessage
