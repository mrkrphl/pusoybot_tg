import telegram
import card

bot = telegram.Bot
for i in card.STICKERS.keys():
    bot.sendSticker("wala")

print(card.STICKERS_GRAY)