from rss import FeedRSS
from telegram import BotTelegram

if __name__ == "__main__":
    URL1 = "http://portal.uern.br/blog/category/noticias/feed/"
    URL2 = "https://aduern.org.br/category/noticias/feed/"

    with open(".bot", "r") as f:
        token = f.read().split("\n")


    rss = FeedRSS()
    rss.downloadXML(URL1, URL2)
    titles, links = rss.xtractData()

    bot = BotTelegram(token[0], token[1])

    for x in range(len(titles)):
        message = titles[x] + "\n" + links[x]

        bot.sendMessage(message)
