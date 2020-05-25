from BotAuth import DataBot
from core.data import Database
from core.rss import AnalyzeRSS, downloadXML
from core.telegram import BotTelegram

if __name__ == '__main__':
    print('[CORE] Iniciando algoritmo ...')

    URLS = [
        'http://portal.uern.br/blog/category/noticias/feed/',
        'https://aduern.org.br/category/noticias/feed/'
    ]

    token, chatId = DataBot.readJson()

    database = Database(sizeHistory=len(URLS)*100)
    files = downloadXML(URLS)

    if len(files) > 0:
        analyze = AnalyzeRSS(filenames=files)
        datas = analyze.getData()
        database.add(datas)
    
    messages = database.getWaitingMessages()

    bot = BotTelegram(token, chatId)

    for message in messages:
        messageToSend = message['title'] + '\n' + message['link']
        responses = bot.sendMessage(messageToSend)

        if True in responses:
            database.removeFromWaitList(message)
        else:
            print('Error')
            break
