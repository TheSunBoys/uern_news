import os
import xml.etree.ElementTree as ET

class AnalyzeRSS():
    def __init__(self, directory = '.database', filenames=None):
        self._dir = directory
        self._filenames = filenames

    def _xtractData(self, files):
        messages = []

        for file in files:
            root = ET.parse(file).getroot()
    
            itemElement = root.findall('channel/item')
            for i in itemElement:
                messages.append({
                    'title': i[0].text,
                    'link': i[1].text,
                    'pubDate': i[3].text
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
