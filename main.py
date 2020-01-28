from rss import AnalyzeRSS, downloadXML
from telegram import BotTelegram, DataBot

if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    token, chatId = DataBot.readJson()

    downloadXML(URL1, URL2)
    analyze = AnalyzeRSS()
    messages = analyze.getData()

    bot = BotTelegram(token, chatId)

    for message in messages[::-1]:
        bot.sendMessage(message)
