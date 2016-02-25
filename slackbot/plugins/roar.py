from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@listen_to("roar", re.IGNORECASE)
@respond_to("roar", re.IGNORECASE)
def roar(message):
    message.reply("ROAR")

@listen_to("rawr", re.IGNORECASE)
@respond_to("rawr", re.IGNORECASE)
@listen_to("raor", re.IGNORECASE)
@respond_to("raor", re.IGNORECASE)
def roar(message):
    message.reply("You call that a roar?")
