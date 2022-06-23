from bot import Bot
from decouple import config


bot = Bot()
bot.login(config("LOGIN"), config("PASSWORD"), has2F=config("HAS2F"))
bot.run()