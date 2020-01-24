from rss import AnalyzeRSS, DataBot, downloadXML
from telegram import BotTelegram

if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    token, chatId = DataBot.readJson()

    downloadXML(URL1, URL2)
    analyze = AnalyzeRSS()
    titles, links = analyze.getData()

    bot = BotTelegram(token, chatId)

    for x in range(len(titles)-1, -1, -1):
        message = titles[x] + "\n" + links[x]

        bot.sendMessage(message)
