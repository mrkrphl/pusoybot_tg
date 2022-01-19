
from fileinput import filename
from config import TOKEN, WORKERS
from telegram.ext import Updater

from gamethings.game_manager import GameManager

gm = GameManager()
updater = Updater(token=TOKEN, workers=WORKERS)
dispatcher = updater.dispatcher
