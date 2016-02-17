from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@listen_to("roar", re.IGNORECASE)
@respond_to("roar", re.IGNORECASE)
def roar(message):
    message.reply("ROAR")
