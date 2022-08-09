from bot import Bot
from decouple import config


bot = Bot()
bot.login(config("LOGIN"), config("PASSWORD"), has2F=True)
bot.vote()


# bot.addMarket(80, 190, 5)
bot.buyXpBooster(3)
bot.evolveByCandies(2000)
bot.changePoke(32)
bot.spamming(1)
bot.changePoke(59)
bot.spamming(30)
