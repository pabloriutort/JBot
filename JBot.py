from os import environ
from telegram.ext import CommandHandler as c_handler
from telegram.ext import MessageHandler as m_handler
from telegram.ext import Updater


class JBot(object):

    def __init__(self):
        updater = Updater(token=environ['BOT_TOKEN'])
        self.__updater = updater
        self.__dispatcher = updater.dispatcher


    def add_command(self, name, command):
        self.__dispatcher.add_handler(c_handler(name, command))


    def listen(self):
        self.__updater.start_polling(clean=True)
        self.__updater.idle()

