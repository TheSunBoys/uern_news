import datetime
import json
import os

class Database():
    def __init__(self, directory=".database", filename="database.json"):
        self._directory = directory
        self._filename = filename
        self._database = None

        if os.path.exists(self._directory) == False:
            os.mkdir(self._directory)
            self._database = {}
            self._database["waiting"] = []
            self._database["history"] = []
        else:
            with open(f"{self._directory}/{self._filename}", "r") as file:
                self._database = json.load(file)

    def _removeDuplicate(self, messages):
        for elt in self._database["history"]:
            if elt["msg"] in messages:
                del(messages[messages.index(elt[msg])])

        for elt in self._database["waiting"]:
            if elt in messages:
                del(messages[messages.index(elt)])

        return messages

    def _saveDatabase(self):
        with open(f"{self._directory}/{self._filename}", "w") as file:
            json.dump(self._database, file, ensure_ascii=False, indent=2)

    def add(self, messages):
        messages = self._removeDuplicate(messages)

        if len(messages) > 0:
            self._database["waiting"] += messages

        self._saveDatabase()

    def getWaitingMessages(self):
        return self._database["waiting"]

    def removeFromWaitList(self, message):
        index_ = self;_database["waiting"].index(message)
        date = str(datetime.datetime.now())

        self._database["history"].append({
        "msg": self._database["waiting"][index_],
        "sendDate": date[:len(date)-7]
        })

        del(self._database["waiting"][index_])

        self._saveDatabase()
