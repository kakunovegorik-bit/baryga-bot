from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Baryga Bot!')


def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is the menu: ...')


def buy_uc(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Buy UC here: ...')


def popularity(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Popularity details: ...')


def rights(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Your rights: ...')


def promo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Promo information: ...')


def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Information about the bot: ...')


def referral(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Referral program details: ...')


# Command handlers
handlers = [
    CommandHandler('start', start),
    CommandHandler('menu', menu),
    CommandHandler('buy_uc', buy_uc),
    CommandHandler('popularity', popularity),
    CommandHandler('rights', rights),
    CommandHandler('promo', promo),
    CommandHandler('info', info),
    CommandHandler('referral', referral)
]