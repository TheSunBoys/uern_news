from modules.data import Database
from modules.rss import AnalyzeRSS, downloadXML
from modules.telegram import BotTelegram, DataBot

if __name__ == "__main__":
    URLS = [
        "http://portal.uern.br/blog/category/noticias/feed/",
        "https://aduern.org.br/category/noticias/feed/"
    ]

    token, chatId = DataBot.readJson()

    downloadXML(URLS)
    analyze = AnalyzeRSS()
    datas = analyze.getData()

    database = Database()
    database.add(datas)
    messages = database.getWaitingMessages()

    bot = BotTelegram(token, chatId)

    for message in messages:
        #DEBUG
        #answer = bot.sendMessage(message)

        if True:
            database.removeFromWaitList(message)
