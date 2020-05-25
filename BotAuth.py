import json

class DataBot():
    @staticmethod
    def writeJson(token, chat_id):
        config = {'token': token, 'chatId': chat_id}

        with open('.bot.json', 'w') as file:
            json.dump(config, file, ensure_ascii=False, indent=2)

    @staticmethod
    def readJson():
        print('[DataBot] Lendo dados do json ...')
        with open('.bot.json', 'r') as file:
            config = json.load(file)

        return config['token'], config['chatId']

if __name__ == '__main__':
    # criar arquivo .bot.json
    TOKEN = 'coloque seu token aqui'
    CHAT_ID = [
        'coloque todos os chatIds aqui',
        'separados cada um como uma string'
    ]

    DataBot.writeJson(TOKEN, CHAT_ID)
