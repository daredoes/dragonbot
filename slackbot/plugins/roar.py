from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to("roar", re.IGNORECASE)
def roar(message):
    message.reply("ROAR")
    
@listen_to("roar", re.IGNORECASE)
def roarPublic(message):
    message.send("ROAR")
