from bot import Bot
from decouple import config


bot = Bot()
bot.login(config("LOGIN"), config("PASSWORD"), has2F=True)
bot.vote()
# bot.addMarket(80, 190, 5)
# bot.buyXpBooster(3)
# bot.evolveByCandies(2000)
# bot.changePoke(5)
# bot.evolveByCandies(75)
# bot.spamming(5)
