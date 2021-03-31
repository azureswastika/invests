import json

from telegram import Update
from telegram.ext import CallbackContext

from .constants import CHAT, DATA, NAME, SEARCH, TICKER, TYPE


def start(update: Update, _: CallbackContext):
    update.message.reply_text(
        (
            "Use /subscribe <ticker> to subscribe on the ticker changes\n"
            "Use /unsubscribe <ticker> to unsubscribe on the ticker changes"
        )
    )


def send_search(ws, chat_id, ticker):
    return ws.send(
        json.dumps(
            {
                TYPE: SEARCH,
                DATA: {CHAT: chat_id, TICKER: {NAME: ticker}},
            }
        )
    )
