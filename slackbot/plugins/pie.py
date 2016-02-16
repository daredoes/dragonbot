from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

import time

pieEndTime = 0

stage = 0

@listen_to("I want a pie", re.IGNORECASE)
@respond_to("I want a pie", re.IGNORECASE)
def pieWhatFlavor(message):
    global stage
    global pieMaxTime
    
    message.reply("What flavor?")

    stage = 1
    pieMaxTime = time.time() + 5*60 #5 min max


@listen_to("pi flavor", re.IGNORECASE)
@respond_to("pi flavor", re.IGNORECASE)
def givePi(message):
    global stage
    global pieMaxTime
    
    if (stage == 1) and (time.time() < pieMaxTime):
        stage = 0
        pieMaxTime = 0
        message.send("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609")
        
