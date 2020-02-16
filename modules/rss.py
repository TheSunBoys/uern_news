import os
import urllib.request
import xml.etree.ElementTree as ET

def downloadXML(*urls):
    directory = ".database"

    if os.path.exists(directory) == False:
        os.mkdir(directory)

    for i in range(len(urls)):
        urllib.request.urlretrieve(urls[i], f"{directory}/file{i}.xml")


class AnalyzeRSS():
    def __init__(self, directory = ".database", filename="file"):
        self._dir = directory
        self._filename = filename

    def _xtractData(self, files):
        message = list()

        for file in files:
            root = ET.parse(file).getroot()
            itemElement = root.findall("channel/item")

            for i in itemElement:
                title = i[0].text
                link = i[1].text
                pubdate = i[3].text

                message.append({
                    "title": title,
                    "link": link,
                    "pubDate": pubdate
                })

        return message[::-1]

    def _searchFiles(self, name):
        length = 0
        files = os.listdir(self._dir)

        for file in files:
            if file[:len(name)] == name:
                length += 1

        if length > 0:
            filenames = [f"{self._dir}/{name}{x}.xml" for x in range(length)]
            return filenames

    def _removeFiles(self):
        files = os.listdir(self._dir)

        for file in files:
            if file[:3] == self._filename:
                os.remove(f"{self._dir}/{file}")

    def getData(self):
        files = self._searchFiles(self._filename)
        self._removeFiles()

        if files != None:
            data = self._xtractData(files)
            return data
