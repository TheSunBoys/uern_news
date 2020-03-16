import copy
import datetime
import json
import os

class Database():
    """
    Esta classe é usada para gerenciar mensagens, enviadas e pendentes
    como um banco de dados, ela permite:

    :salvar mensagens que ainda não foram enviadas
    :adicionar mensagens enviadas a um historico
    :analisar mensagens antes de serem adicionar ao banco de dados e removendo
    duplicações
    """
    
    def __init__(self, directory=".database", filename="database.json", sizeHistory=60):
        self._directory = directory
        self._filename = filename
        self._sizeHistory = sizeHistory
        self._database = None

        # carrega na memoria o json, se o arquivo não existir, um novo será criado
        if os.path.exists(f"{self._directory}/{self._filename}"):
            with open(f"{self._directory}/{self._filename}", "r") as file:
                self._database = json.load(file)
        else:
            if os.path.exists(self._directory) == False:
                os.mkdir(self._directory)

            self._database = {}
            self._database["waiting"] = []
            self._database["history"] = []

    def _removeDuplicate(self, messages, dict_key):
        """Analisa a lista do banco de dados e remove duplicações"""

        tem_list = [messages[x]["link"] for x in range(len(messages))]

        for elt in self._database[dict_key]:
            if elt["link"] in tem_list:
                index_ = tem_list.index(elt["link"])

                del(messages[index_])
                del(tem_list[index_])

        return messages

    def _saveDatabase(self):
        """Atualiza o arquivo json com os ultimos dados do dict"""

        with open(f"{self._directory}/{self._filename}", "w") as file:
            json.dump(self._database, file, ensure_ascii=False, indent=2)

    def _removeOldDataFromHystory(self):
        """Este metodo remove mensagens muito antigas do historico
        de mensagens para manter o limite de dados do historico"""

        while len(self._database["history"]) > self._sizeHistory:
            del(self._database["history"][0])
    
    def add(self, messages):
        """Analisa as mensagens antes de serem adicionadas ao banco de dados e remove
        dupĺicações"""
        messages = self._removeDuplicate(messages, "history")
        messages = self._removeDuplicate(messages, "waiting")
        self._removeOldDataFromHystory()

        if len(messages) > 0:
            self._database["waiting"] += messages

        self._saveDatabase()

    def getWaitingMessages(self):
        """retona as mensagens não enviadas"""
        return copy.deepcopy(self._database["waiting"])

    def removeFromWaitList(self, message):
        """remove da lista de mensagens pendentes, a mensagem passada como parametro
        e adiciona a lista do historico"""

        index_ = self._database["waiting"].index(message)
        date = str(datetime.datetime.now())

        self._database["history"].append({
            "title": self._database["waiting"][index_]["title"],
            "link": self._database["waiting"][index_]["link"],
            "sendDate": date[:len(date)-7]
        })

        del(self._database["waiting"][index_])

        self._saveDatabase()
