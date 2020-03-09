import urllib.parse
import urllib.request

class BotTelegram():
    def __init__(self, token, chatId):
        self._token = token
        self._chatId = chatId

    def sendMessage(self, message):
        message = urllib.parse.quote(message)
        responses = list()

        for id in self._chatId:
            API = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={id}&text={message}"
  
            try:
                urllib.request.urlopen(API)
                responses.append(True)
            except:
                responses.append(None)
                continue

        return responses
            

    def sendPhoto(self):
        pass

    def getUpdates(self):
        API = f"https://api.telegram.org/bot{self._token}/getUpdates"
        urllib.request.urlretrieve(urls[i], "getUpdates.json")

