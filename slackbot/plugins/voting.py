from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

import time

voteName = ""

options = []
votes = []

voted = {}
voteChannel = ""

voteCloseTime = 0

def isVoteOpen(message):
    global voteCloseTime
    global voteChannel

    if time.time() >= voteCloseTime:
        message.reply("No active vote.")

    elif voteChannel != message._body["channel"]:
            message.reply("Vote locked to another channel.")

    else:
        return True

    return False

@respond_to("start vote (.*)", re.IGNORECASE)
def startVote(message, setVoteName):
    global voteName
    global options
    global votes
    global voteCloseTime
    global voted
    global voteChannel

    #reset variables
    voteName = setVoteName
    options = []
    votes = []
    voted = {}
    voteCloseTime = time.time() + 60*60 #give an hour to vote

    voteChannel = message._body["channel"]

    message.reply("Vote \"" + voteName + "\" started")
    

@respond_to("add option (.*)", re.IGNORECASE)
def addOption(message, optionName):
    global options
    global votes

    if isVoteOpen(message):
        options.append(optionName)
        votes.append(0)

        message.reply("Option \"" + optionName + "\" added.")

@respond_to("list vote", re.IGNORECASE)
def listOptions(message):
    global options
    global votes
    global voteName

    if isVoteOpen(message):
        message.send(voteName)
        message.send("Options:")
        
        for option in options:
            message.send(option)

@respond_to("cast vote (.*)", re.IGNORECASE)
def addVote(message, voteFor):
    global options
    global votes
    global voted

    if isVoteOpen(message):
        if options.count(voteFor) > 0:
            voter = message._get_user_id()

            if voter in voted:#if they already voted
                votes[options.index(voted[voter])] -= 1 #remove previous vote
            
            votes[options.index(voteFor)] += 1
            voted[voter] = voteFor #record vote for changing
            message.reply("Sucessfully voted for " + voteFor)

        else:
            message.reply("Option " + voteFor + " does not exist!")

@respond_to("end vote", re.IGNORECASE)
def endVote(message):
    global options
    global votes

    if isVoteOpen(message):
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
    

    
