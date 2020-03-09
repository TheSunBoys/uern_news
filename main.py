import time

from BotAuth import DataBot
from modules.data import Database
from modules.rss import AnalyzeRSS, downloadXML
from modules.telegram import BotTelegram

if __name__ == "__main__":
    URLS = [
        "http://portal.uern.br/blog/category/noticias/feed/",
        "https://aduern.org.br/category/noticias/feed/"
    ]

    token, chatId = DataBot.readJson()

    files = downloadXML(URLS)
    database = Database()

    if len(files) > 0:
        analyze = AnalyzeRSS(filenames=files)
        datas = analyze.getData()
        database.add(datas)
    
    messages = database.getWaitingMessages()

    bot = BotTelegram(token, chatId)

    for message in messages:
        #DEBUG
        messageToSend = message["title"] + "\n" + message["link"]
        print(messageToSend)
        #answer = bot.sendMessage(messageToSend)

        if True:
            database.removeFromWaitList(message)
            time.sleep(1)
        else:
            print("Error")
            break
