import json
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
