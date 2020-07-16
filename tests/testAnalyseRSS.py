import sys

from createXml import createXmlfile

sys.path.append('..')
import core

def testAnalyseRSS():
    """testa o comportamento da classe AnaluyseRSS"""

    FILENAME = 'fileTest.xml'
    createXmlfile(FILENAME, 4)

    analyse = core.AnalyzeRSS(filenames=[FILENAME])
    messages = analyse.getData()
    
    messages = messages[::-1]
    for x in range(len(messages)):
        dictTest = {
            'title': f'titulo{x}',
            'link': f'link{x}',
            'pubDate': f'uma data{x}',
        }

        assert messages[x]['title'] == dictTest['title']
        assert messages[x]['link'] == dictTest['link']
        assert messages[x]['pubDate'] == dictTest['pubDate']

if __name__ == "__main__":
    testAnalyseRSS()

