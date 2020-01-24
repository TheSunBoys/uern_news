import json
import os
import urllib.request
import xml.etree.ElementTree as ET

def downloadXML(*urls):
    filenames = list()

    if os.path.exists(".database") == False:
        os.mkdir(".database")

    for i in range(len(urls)):
        urllib.request.urlretrieve(urls[i], f".database/.new{i}.xml")
        filenames.append(f".database/.new{i}.xml")

    return filenames

class AnalyzeRSS():
    def _xtractData(self, files):
        title = list()
        link = list()

        for file in files:
            root = ET.parse(file).getroot()
            itemElement = root.findall("channel/item")

            for i in itemElement:
                title.append(i[0].text)
                link.append(i[1].text)

        return title, link

    def _newfiles(self):
        length = 0
        files = os.listdir(".database")

        for file in files:
            if file[1:4] == "new":
                length += 1

        filenames = [f".database/.new{x}.xml" for x in range(length)]

        return self._xtractData(filenames)

    def _oldfiles(self):
        length = 0
        files = os.listdir(".database")

        for file in files:
            if file[1:4] == "old":
                length += 1

        if length > 0:
            filenames = [f".database/.old{x}.xml" for x in range(length)]
            return self._xtractData(filenames)
        else:
            return False, False

    def _updateFilenames(self):
        files = os.listdir(".database")

        for file in files:
            if file[1:4] == "old":
                os.remove(".database/"+file)

        for file in files:
            if file[1:4] == "new":
                os.rename(".database/"+file, ".database/.old"+file[4:])

    def getData(self):
        newTitle, newLink = self._newfiles()
        oldTitle, oldLink = self._oldfiles()

        if oldTitle != False:
            for element in oldTitle:
                if element in newTitle:
                    del(newTitle[newTitle.index(element)])

            for element in oldLink:
                if element in newLink:
                    del(newLink[newLink.index(element)])
                    
        self._updateFilenames()

        return newTitle, newLink

class DataBot():
    @staticmethod
    def writeJson(token, chat_id):
        config = {"token": token, "chatId": chat_id}

        with open(".bot.json", "w") as file:
            json.dump(config, file, ensure_ascii=False, indent=2)

    @staticmethod
    def readJson():
        with open(".bot.json", "r") as file:
            config = json.load(file)

        return config["token"], config["chatId"]

if __name__ == "__main__":
    TOKEN = "your token here"
    CHAT_ID = "-your chat_id here"

    DataBot.writeJson(TOKEN, CHAT_ID)
