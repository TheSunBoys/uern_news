import urllib.parse
import urllib.request

class BotTelegram():
    def __init__(self, token, chatId):
        self._token = token
        self._chatId = chatId

    def sendMessage(self, message):
        message = urllib.parse.quote(message)
        API = f'https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chatId}&text={message}'

        try:
            urllib.request.urlopen(API)
            print('[telegram] Mensagem enviada com sucesso') # log
            return True
        except:
            print('[telegram] Erro ao tentar enviar mensagem') # log
            return False

    def getUpdates(self):
        API = f'https://api.telegram.org/bot{self._token}/getUpdates'
        urllib.request.urlretrieve(urls[i], 'getUpdates.json')
