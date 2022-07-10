from bot import Bot
from decouple import config


bot = Bot()
bot.login(config("LOGIN"), config("PASSWORD"), has2F=config("HAS2F"))
# bot.run()


bot.changePoke(88)
bot.spamming(20)
bot.driver.close()
