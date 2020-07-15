import shutil
import sys
import json

sys.path.append('..')
import core

def createDataStruct() -> list:
    """Criar uma lista de dicionarios com os mesmos dados que seriam inseridos no json criado pela
    classe Database"""

    dataStruct = []
    for x in range(3):
        dataStruct.append({
            'title': f'titulo{x}',
            'link': f'link{x}',
            'sendDate': f'date{x}'
        })
    
    
    return dataStruct

def checkDataFromClass(data: list, DIRECTORY='testDatabase') -> None:
    """Testa o comportamento da classe"""

    FILENAME = 'testDatabase.json'

    database = core.Database(directory=DIRECTORY, filename=FILENAME)
    database.add(data)
    messageWaiting = database.getWaitingMessages()

    for x in range(len(messageWaiting)):
        assert messageWaiting[x]['title'] == f'titulo{x}'
        assert messageWaiting[x]['link'] == f'link{x}'
        assert messageWaiting[x]['sendDate'] == f'date{x}'

def testDatabase() -> None:
    """Executa varios testes na classe Database"""

    DIRECTORY = 'testDatabase'

    dataJson = createDataStruct()
    checkDataFromClass(dataJson, DIRECTORY)

    shutil.rmtree(DIRECTORY)



if __name__ == "__main__":
    testDatabase()