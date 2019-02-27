"""The Executioner - For Discord
            Made by Leveles"""

import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands import has_permissions
from random import choice
import datetime
import eulogy

imports_to_delete = "from discord.utils import get, import os, import re, import asyncio"

bot = commands.Bot(command_prefix="exec!")

responses = ["Right away.", "*Slicing sounds.*", "My pleasure.", "Of course.", "It is an honor.",
             "It is always an honor.", "It shall be done.", "On it.", "Yes your grace.", "I am on it.", "Yes...",
             "*Distant cries.*", "Consider it done.", "This will be fun.", "If I must...", "A pleasure.",
             "Always a pleasure.", "Where's my hammer...", "I'll hold nothing back.", "Like this?", "Yes Senpai."
             "..."]

client = discord.Client()

@bot.event
async def on_ready():
    print("Active as " + bot.user.name + "\nWith the id " + bot.user.id + ".")

#HOW2USE
@bot.command(name="how2use", pass_context=True)
async def how2use(ctx):
    server_of_origin = ctx.message.server
    await bot.say("**I am the executioner of " + str(server_of_origin) + "**.\n" + "\n"
                  + "Here is how I may serve you:\n"
                  + "*(all commands work by mentioning a target after said command)*\n"
                  + "`exec!rip` command will have me create a eulogy for the target without bringing action to them.\n"
                  + "`exec!resurrect` command will have me announce that the target has been resurrected"
                  + "`exec!execute` command will have me create a eulogy for the target signifying their execution.\n"
                  + "`exec!mute` command will have me mute a target and create a eulogy for said muting.\n"
                  + "`exec!unmute` command will have me unmute a target and announce their pardoning.\n"
                  + "`exec!kick` command will have me kick a target from " + str(server_of_origin) + ".\n"
                  + "`exec!ban` command will have me ban a target from " + str(server_of_origin) + ".\n"
                  + "**NOTE:** *all commands will notify the target of the action, as well as who initiated it.*")

#RIP
@bot.command(name="rip", pass_context=True)
async def rip(ctx):
    #Setup
    verdict = "remember"
    requester = ctx.message.author
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await self.bot.user("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #executing process starts (just a eulogy)
        await bot.say(choice(responses))

        #Sending message to target
        #getting server name that request was made
        server_of_origin = ctx.message.server
        #creating base embed
        embed = discord.Embed(title="🔔 **Attention** 🔔", description= "Your funeral is being held on the server "
                              + str(server_of_origin) + ".")
        #Setting up timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message to offender
        await bot.send_message(target, embed=embed)

        #Writing within server
        #creating eulogy
        spoken_eulogy = eulogy.rememberence(name, verdict)
        #creating base embed
        embed = discord.Embed(title="🔔 **A Member Has Died** 🔔", description= spoken_eulogy, footer= "foot",
                              color=0x7d4a86)
        #Setting up embed timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message for chat
        await bot.say(embed=embed)

#Resurect
@bot.command(name="resurrect", pass_context=True)
async def resurrect(ctx):
    #Setup
    verdict = "resurrect"
    requester = ctx.message.author
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #unmuting process starts
        await bot.say(choice(responses))

        #Sending message to target
        #getting server name that request was made
        server_of_origin = ctx.message.server
        #creating base embed
        embed = discord.Embed(title="🎺 **Attention** 🎺"
                              , description="You have been resurrected on the server "
                              + str(server_of_origin) + ".")
        #Setting up timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message to offender
        await bot.send_message(target, embed=embed)

        #Writing within server
        #creating base embed
        embed = discord.Embed(title="🎺 **A Member Has Been Resurrected** 🎺"
                              , description=name + " has been resurrected.",
                              color=0x7d4a86)
        #Setting up embed timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message for chat
        await bot.say(embed=embed)

#EXECUTE
@bot.command(name="execute", pass_context=True)
@has_permissions(ban_members=True)
async def execute(ctx):
    #Setup
    verdict = "execute"
    requester = ctx.message.author
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #executing process starts (just a eulogy)
        await bot.say(choice(responses))

        #Sending message to target
        #getting server name that request was made
        server_of_origin = ctx.message.server
        #creating base embed
        embed = discord.Embed(title="🔔 **Attention** 🔔", description= "You have been executed on the server "
                              + str(server_of_origin) + ".")
        #Setting up timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message to offender
        await bot.send_message(target, embed=embed)

        #Writing within server
        #creating eulogy
        spoken_eulogy = eulogy.rememberence(name, verdict)
        #creating base embed
        embed = discord.Embed(title="🔔 **A Member Has Been Executed** 🔔", description= spoken_eulogy, footer= "foot",
                              color=0x7d4a86)
        #Setting up embed timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message for chat
        await bot.say(embed=embed)

#MUTE
@bot.command(name="mute", pass_context=True)
@has_permissions(ban_members=True)
async def mute(ctx):
    #Setup
    verdict = "mute"
    requester = ctx.message.author
    mute = discord.utils.get(ctx.message.server.roles, name="Executioner's Mute")
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #checks to see if mute role exists, creates one if not
        if mute is None:
            perms = discord.Permissions(send_messages=False, read_messages=True, add_reactions=False)
            await bot.create_role(ctx.message.author.server, name="Executioner's Mute", permissions=perms)
            await bot.say("An `Executioner's Mute` role was created.")
        #checks if target is already muted
        elif mute in target.roles:
            await bot.say(name + " is already muted.")

        #muting process starts
        else:
            await bot.say(choice(responses))
            mute = discord.utils.get(ctx.message.server.roles, name="Executioner's Mute")
            await bot.add_roles(ctx.message.mentions[0], mute)

            #Sending message to target
            #getting server name that request was made
            server_of_origin = ctx.message.server
            #creating base embed
            embed = discord.Embed(title="🔔 **Attention** 🔔", description= "You have been muted on the server "
                                  + str(server_of_origin) + ".")
            #Setting up timestamp
            time_of_action = datetime.datetime.now()
            embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
                time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
            #embed message to offender
            await bot.send_message(target, embed=embed)

            #Writing within server
            #creating eulogy
            spoken_eulogy = eulogy.rememberence(name, verdict)
            #creating base embed
            embed = discord.Embed(title="🔔 **A Member Has Been Muted** 🔔", description= spoken_eulogy, footer= "foot",
                                  color=0x7d4a86)
            #Setting up embed timestamp
            time_of_action = datetime.datetime.now()
            embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
                time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
            #embed message for chat
            await bot.say(embed=embed)

#UMUTE
@bot.command(name="unmute", pass_context=True)
@has_permissions(ban_members=True)
async def unmute(ctx):
    #Setup
    verdict = "unmute"
    requester = ctx.message.author
    mute = discord.utils.get(ctx.message.server.roles, name="Executioner's Mute")
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #checks to see if mute role exists, creates one if not
        if mute is None:
            perms = discord.Permissions(send_messages=False, read_messages=True, add_reactions=False)
            await bot.create_role(ctx.message.author.server, name="Executioner's Mute", permissions=perms)
            await bot.say("An `Executioner's Mute` role was created.")
        #checks if target is already muted
        elif mute not in target.roles:
            await bot.say(name + " is not muted.")

        #unmuting process starts
        else:
            await bot.say(choice(responses))
            mute = discord.utils.get(ctx.message.server.roles, name="Executioner's Mute")
            await bot.remove_roles(ctx.message.mentions[0], mute)

            #Sending message to target
            #getting server name that request was made
            server_of_origin = ctx.message.server
            #creating base embed
            embed = discord.Embed(title="🎺 **Attention** 🎺"
                                  , description="You have been pardoned and unmuted on the server "
                                  + str(server_of_origin) + ".")
            #Setting up timestamp
            time_of_action = datetime.datetime.now()
            embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
                time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
            #embed message to offender
            await bot.send_message(target, embed=embed)

            #Writing within server
            #creating base embed
            embed = discord.Embed(title="🎺 **A Member Has Been Pardoned** 🎺"
                                  , description=name + " has been pardoned and unmuted.",
                                  color=0x7d4a86)
            #Setting up embed timestamp
            time_of_action = datetime.datetime.now()
            embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
                time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
            #embed message for chat
            await bot.say(embed=embed)

#KICK
@bot.command(name="kick", pass_context=True)
@has_permissions(ban_members=True)
async def kick(ctx):
    #Setup
    verdict = "kick"
    requester = ctx.message.author
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #kicking process starts
        await bot.say(choice(responses))
        #Sending message to target
        #getting server name that request was made
        server_of_origin = ctx.message.server
        #creating base embed
        embed = discord.Embed(title="🔔 **Attention** 🔔", description= "You have been kicked from the server "
                              + str(server_of_origin) + ".")
        #Setting up timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message to offender
        await bot.send_message(target, embed=embed)

        #Writing within server
        #creating eulogy
        spoken_eulogy = eulogy.rememberence(name, verdict)
        #creating base embed
        embed = discord.Embed(title="🔔 **A Member Has Been Kicked** 🔔", description= spoken_eulogy, footer= "foot",
                              color=0x7d4a86)
        #Setting up embed timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message for chat
        await bot.say(embed=embed)
        #actually kicking the target
        await bot.kick(target)

#BAN
@bot.command(name="ban", pass_context=True)
@has_permissions(ban_members=True)
async def ban(ctx):
    #Setup
    verdict = "ban"
    requester = ctx.message.author
    msg = ctx.message.content.split(" ", 1)
    name = msg[1]
    all_clear = 0
    person_check = 0

    #Checking if target is single person or is in the list of members
    if name == "@everyone":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    if name == "@here":
        await bot.say("I *alone* cannot " + verdict + " so many.")
        person_check = 1
    try:
        target = ctx.message.mentions[0]
    except IndexError:
        if person_check < 1:
            await bot.say("Please select a person for me to " + verdict + ".")
            person_check = 1

    if target == bot.user:
        await bot.say("I cannot " + verdict + " *myself*.")
        person_check = 1

    if person_check < 1:
        if target in ctx.message.server.roles:
            await bot.say("I *alone* cannot " + verdict + " so many.")
        else:
            if ctx.message.mentions[0] not in ctx.message.server.members:
                await bot.say("I cannot " + verdict + " a person that is not here.")
            else:
                all_clear = 1

    if all_clear > 0:
        #kicking process starts
        await bot.say(choice(responses))
        #Sending message to target
        #getting server name that request was made
        server_of_origin = ctx.message.server
        #creating base embed
        embed = discord.Embed(title="🔔 **Attention** 🔔", description= "You have been banned from the server "
                              + str(server_of_origin) + ".")
        #Setting up timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message to offender
        await bot.send_message(target, embed=embed)

        #Writing within server
        #creating eulogy
        spoken_eulogy = eulogy.rememberence(name, verdict)
        #creating base embed
        embed = discord.Embed(title="🔔 **A Member Has Been banned** 🔔", description= spoken_eulogy, footer= "foot",
                              color=0x7d4a86)
        #Setting up embed timestamp
        time_of_action = datetime.datetime.now()
        embed.set_footer(text="Requested by: " + str(requester) + ", at: " + str(
            time_of_action.strftime("%a, %b %d, %Y, %I:%M %p")) + ".")
        #embed message for chat
        await bot.say(embed=embed)
        #actually kicking the target
        await bot.ban(target)

#TOKEN
#KEEP IT SECRET PEEPS
bot.run("SECRET")