import sys

import core
from BotAuth import DataBot

if __name__ == '__main__':
    # verificar versao do python
    if sys.version_info[0] < 3 or sys.version_info[1] < 6:
        sys.exit('Este algoritmo requer uma versao do python 3.6 ou superior!')


    print('[CORE] Iniciando algoritmo ...')

    URLS = [
        'http://portal.uern.br/blog/category/noticias/feed/',
        'https://aduern.org.br/category/noticias/feed/'
    ]

    token, chatId = DataBot.readJson()
    database = core.Database(sizeHistory=len(URLS)*100)
    files = core.downloadXML(URLS)

    if len(files) > 0:
        analyze = core.AnalyzeRSS(filenames=files)
        datas = analyze.getData()
        database.add(datas)

    messages = database.getWaitingMessages()

    bot = core.BotTelegram(token, chatId)

    for message in messages:
        messageToSend = message['title'] + '\n' + message['link']

        if bot.sendMessage(messageToSend):
            database.removeFromWaitList(message)
        else:
            print('Error')
