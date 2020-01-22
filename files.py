import urllib.request
import xml.etree.ElementTree as ET

class FeedRSS():
    def __init__(self):
        self._filenames = list()

    def downloadXML(self, *urls):
        for i in range(len(urls)):
            urllib.request.urlretrieve(urls[i], f".rss{i}.xml")
            self._filenames.append(f".rss{i}.xml")

    def xtractData(self, *elements):
        root = ET.parse(self._filenames[0]).getroot()
        titulo = list()
        link = list()

        for x in root.findall("channel/item/title"):
            titulo.append(x.text)

        for x in root.findall("channel/item/link"):
            link.append(x.text)

        for x in range(len(titulo)):
            print(titulo[x])
            print(link[x])
            print()


if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    feed = FeedRSS()
    feed.downloadXML(URL1, URL2)
    feed.xtractData()
