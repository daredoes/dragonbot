from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

import time

options = []
votes = []

voteCloseTime = 0

@respond_to("start vote", re.IGNORECASE)
def startVote(message):
    global options
    global votes
    global voteCloseTime

    #reset variables
    options = []
    votes = []
    voteCloseTime = time.time() + 60*60 #give an hour to vote

    message.reply("Vote started")
    

@respond_to("add option (.*)", re.IGNORECASE)
def addOption(message, optionName):
    global options
    global votes
    global voteCloseTime

    if time.time() < voteCloseTime:
        options.append(optionName)
        votes.append(0)

        message.reply("Option \"" + optionName + "\" added.")

@respond_to("list options", re.IGNORECASE)
def listOptions(message):
    global options
    global votes
    global voteCloseTime

    if time.time() < voteCloseTime:
        message.send("Options:")
        
        for option in options:
            message.send(option)

@respond_to("vote (.*)", re.IGNORECASE)
def addVote(message, voteFor):
    global options
    global votes
    global voteCloseTime

    if time.time() < voteCloseTime:
        if options.count(voteFor) > 0:
            
            votes[options.index(voteFor)] += 1
            message.reply("Sucessfully voted for " + voteFor)

        else:
            message.reply("Option " + voteFor + " does not exist!")

@respond_to("end vote", re.IGNORECASE)
def endVote(message):
    global options
    global votes
    global voteCloseTime

    if time.time() < voteCloseTime:
        voteCloseTime = 0

        maxVotes =  0
        maxIndex = -1

        #find the winner
        for i in range(0, len(options)):
            maxVotes = max(votes[i], maxVotes)

            if votes[i] == maxVotes:
                maxIndex = i

        if maxVotes > 0:
            message.send(options[maxIndex] + " wins!")

            for i in range(0, len(options)):
                message.send(options[i] + " - " + str(votes[i]))

        else:
            message.send("There is no winner!")
    

    
