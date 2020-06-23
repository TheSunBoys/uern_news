import core
from BotAuth import DataBot

if __name__ == '__main__':
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
        responses = bot.sendMessage(messageToSend)

        if True in responses:
            database.removeFromWaitList(message)
        else:
            print('Error')
            break
