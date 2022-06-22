# Bot de spam DISCORD

Bot utilizado para spammar no discord

## Usage
```python
from bot import Bot
from decouple import config


bot = Bot()
bot.login(config("LOGIN"), config("PASSWORD"), has2F=True)
bot.addMarket(80, 190, 5)
bot.buyXpBooster(3)
bot.evolveByCandies(2000)
bot.changePoke(5)
bot.spamming(5)

```


#### [Referência](https://github.com/devaprender/bot_comentarios_instagram)
