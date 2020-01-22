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


if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    feed = FeedRSS()
    feed.downloadXML(URL1, URL2)
    titles, links = feed.xtractData()
