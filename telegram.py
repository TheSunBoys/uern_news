import urllib.parse
import urllib.request

class BotTelegram():
    def __init__(self, token, chatId):
        self._token = token
        self._chatId = chatId

    def sendMessage(self, message):
        message = urllib.parse.quote(message)
        API = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatId}&text={message}"

        response = urllib.request.urlopen(API)

    def sendPhoto(self):
        pass

    def getUpdates(self):
        API = f"https://api.telegram.org/bot{self._token}/getUpdates"

class DataBot():
    @staticmethod
    def writeJson(token, chat_id):
        config = {"token": token, "chatId": chat_id}

        with open(".bot.json", "w") as file:
            json.dump(config, file, ensure_ascii=False, indent=2)

    @staticmethod
    def readJson():
        with open(".bot.json", "r") as file:
            config = json.load(file)

        return config["token"], config["chatId"]

if __name__ == "__main__":
    TOKEN = "your token here"
    CHAT_ID = "-your chat_id here"

    DataBot.writeJson(TOKEN, CHAT_ID)
