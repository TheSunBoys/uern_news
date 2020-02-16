import copy
import datetime
import json
import os

class Database():
    """
    this class is used to manage pending and sent messages,
    like a database, it allows:

    :save messages that could not be sent
    :add messages sent to history
    :analyze messages before adding to the database and remove duplicates
    if they exist
    """
    def __init__(self, directory=".database", filename="database.json"):
        self._directory = directory
        self._filename = filename
        self._database = None

        # loads the json dict, if the file does not exist, a new dict is created
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
        """analyzes the database list and removes elements that are there"""

        tem_list = [messages[x]["title"] for x in range(len(messages))]

        for elt in self._database[dict_key]:
            if elt["title"] in tem_list:
                index_ = tem_list.index(elt["title"])

                del(messages[index_])
                del(tem_list[index_])

        return messages

    def _saveDatabase(self):
        """Update the json file with latest data from dict"""

        with open(f"{self._directory}/{self._filename}", "w") as file:
            json.dump(self._database, file, ensure_ascii=False, indent=2)

    def add(self, messages):
        """analyze messages before adding to the database and remove duplicates
        if they exist"""
        messages = self._removeDuplicate(messages, "history")
        messages = self._removeDuplicate(messages, "waiting")

        if len(messages) > 0:
            self._database["waiting"] += messages

        self._saveDatabase()

    def getWaitingMessages(self):
        """returns pending messages"""
        return copy.deepcopy(self._database["waiting"])

    def removeFromWaitList(self, message):
        """removes from the pending message passed as a parameter
        and adds it to the history"""

        index_ = self._database["waiting"].index(message)
        date = str(datetime.datetime.now())

        self._database["history"].append({
            "title": self._database["waiting"][index_]["title"],
            "link": self._database["waiting"][index_]["link"],
            "sendDate": date[:len(date)-7]
        })

        del(self._database["waiting"][index_])

        self._saveDatabase()
