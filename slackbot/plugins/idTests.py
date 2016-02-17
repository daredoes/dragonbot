from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to("Who am I?", re.IGNORECASE)
def replyID(message):
    message.reply("Human #" + message._get_user_id());

@respond_to("Where am I?", re.IGNORECASE)
def replyChannelID(message):
    message.reply("Channel #" + message._body['channel']);
