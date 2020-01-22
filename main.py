import urllib.request
import xml.etree.ElementTree as ET

def donwload_xml(*urls):
    for i in range(len(urls)):
        urllib.request.urlretrieve(urls[i], f".rss{i}.xml")

if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    #donwload_xml(URL1, URL2)

    root = ET.parse("feed0.xml").getroot()

    for x in root.findall("channel/item/link"):
        print(x.text)
