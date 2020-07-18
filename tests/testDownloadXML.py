import hashlib
import multiprocessing
import os
import random
import sys
import time

sys.path.append('..')

import core
from createXml import createXmlfile

def getHashFile(filename: str) -> bytes:
    BLOCK_SIZE = 128 * 64
    sha2 = hashlib.sha256()
    file = open(filename, 'rb')

    while True:
        data = file.read(BLOCK_SIZE)
        if not data:
            break

        sha2.update(data)

    return sha2.digest()

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
    core.downloadXML(URLS, directory='.')

    server.terminate()

    assert getHashFile(FILENAME) == getHashFile('file0.xml')

if __name__ == "__main__":
    testDownloadXml()

    