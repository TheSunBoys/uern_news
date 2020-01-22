import urllib.request

class BotTelegram():
    def __init__(self, token, chatId):
        self._token = token
        self._chatId = chatId

    def _encodeURL(self, text):
        for i in range(len(text)):
            if text[i] == " ":
                text = text[:i] + "%20" + text[i+1:]

        return text

    def sendMessage(self, message):
        API = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatId}&text={message}"
        API = self._encodeURL(API)

        response = urllib.request.urlopen(API)

    def sendPhoto(self):
        pass

    def getUpdates(self):
        API = f"https://api.telegram.org/bot{self._token}/getUpdates"


if __name__ == "__main__":
    file = open(".bot", "r")

    lista = list()

    for x in file:
        lista.append(x.rstrip("\n"))

    token = lista[0]
    chat_id = None
    message = "teste"

    bot = BotTelegram(token, chat_id)
    bot.sendMessage(message)
