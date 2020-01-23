import json
import urllib.request
import xml.etree.ElementTree as ET

class FeedRSS():
    def __init__(self):
        self._filenames = list()
        self._title = list()
        self._link = list()

    def downloadXML(self, *urls):
        for i in range(len(urls)):
            urllib.request.urlretrieve(urls[i], f".rss{i}.xml")
            self._filenames.append(f".rss{i}.xml")

    def xtractData(self):
        for file in self._filenames:
            root = ET.parse(file).getroot()
            itemElement = root.findall("channel/item")

            for i in itemElement:
                self._title.append(i[0].text)
                self._link.append(i[1].text)

        return self._title, self._link


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
    TOKEN = "put yuor token here"
    CHAT_ID = "put your chat_id here"
