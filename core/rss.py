import os
import urllib.request
import xml.etree.ElementTree as ET

def downloadXML(urls, directory=".database"):
    print('[RSS] Baixando xmls ...') # log

    filenames = []
    for i in range(len(urls)):
        try:
            urllib.request.urlretrieve(urls[i], f"{directory}/file{i}.xml")
            filenames.append(f"{directory}/file{i}.xml")
        except:
            print(f'[RSS] erro ao tentar baixar da url {urls[i]}') # log

    return filenames


class AnalyzeRSS():
    def __init__(self, directory = ".database", filenames=None):
        self._dir = directory
        self._filenames = filenames

    def _xtractData(self, files):
        messages = list()

        for file in files:
            root = ET.parse(file).getroot()
            itemElement = root.findall("channel/item")

            for i in itemElement:
                title = i[0].text
                link = i[1].text
                pubdate = i[3].text

                messages.append({
                    "title": title,
                    "link": link,
                    "pubDate": pubdate
                })

        # é retornado a reversa da lista para que os ultimos dados postados
        # no xml fiquem no fim da lista
        return messages[::-1]

    def _removeFiles(self):
        """Remove os xmls"""

        for file in self._filenames:
            os.remove(file)

    def getData(self):
        print('[RSS] analisando xmls ...') # log
        
        if self._filenames != None:
            data = self._xtractData(self._filenames)
            self._removeFiles()    

            return data
