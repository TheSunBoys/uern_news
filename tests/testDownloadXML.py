import multiprocessing
import os
import random
import sys
import time

sys.path.append('..')

import core
from createXml import createXmlfile

def startSimpleServer(PORT='8080'):
    os.system(f'python -m http.server {PORT}')

def testDownloadXml():
    FILENAME = 'testDownload.xml'
    PORT = f'{random.randint(48620, 49150)}'
    URLS = [f'http://127.0.0.1:{PORT}/{FILENAME}']

    createXmlfile(FILENAME, 4)

    server = multiprocessing.Process(target=startSimpleServer, args=(PORT,))
    server.start()

    time.sleep(2)
    print(core.downloadXML(URLS, directory='.'))

    server.terminate()

if __name__ == "__main__":
    testDownloadXml()

    