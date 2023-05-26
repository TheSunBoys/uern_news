import os
import urllib.parse
import urllib.request

class BotTelegram():
    def __init__(self, token, chatId):
        self._token = token
        self._chatId = chatId

    def sendMessage(self, message):
        message = urllib.parse.quote(message)
        command = f'curl -X POST https://api.telegram.org/bot{self._token}/sendMessage -H \'Content-Type: application/json\' -d \'{"chat_id":"{self._chatId}","text":"{message}"}\''

        try:
            os.system(command)
            print('[telegram] Mensagem enviada com sucesso') # log
            return True
        except:
            print('[telegram] Erro ao tentar enviar mensagem') # log
            return False
