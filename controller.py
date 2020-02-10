from modules.data import Database
from modules.rss import AnalyzeRSS, downloadXML
from modules.telegram import BotTelegram, DataBot

if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    token, chatId = DataBot.readJson()

    downloadXML(URL1, URL2)
    analyze = AnalyzeRSS()
    datas = analyze.getData()

    database = Database()
    database.add(datas)
    messages = database.getWaitingMessages()

    bot = BotTelegram(token, chatId)

    for message in messages:
        #answer = bot.sendMessage(message)

        if True:
            database.removeFromWaitList(message)
