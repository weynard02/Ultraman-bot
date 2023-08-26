import os
import discord
import requests
import json
import random
import asyncio
import textwrap
from gpt import chatgpt_response
from replit import db
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

curse_words_space = [
  "fak ", "shit ", "cuk ", "bangke ", "jancuk ", "cok ", "wtf ", "ngentd ",
  "memek ", "kntl ", "idiot ", "bgst ", "goblok ", "noob ", "tolol ", "meki ",
  "jnck ", "kimak ", "qmak ", "fuck ", "n00b ", "jancok ", "cog ", "kuntul ",
  "kontol ", "bangsat ", "asu ", "bangsad ", "ngentot ", "fk "
]

curse_words_anti_space = [
  " fak", " shit", " cuk", " bangke", " jancuk", " cok", " wtf", " ngentd",
  " memek", " kntl", " idiot", " bgst", " goblok", " noob", " tolol", " meki",
  " jnck", " kimak", " qmak", " fuck", " n00b", " jancok", " cog", " kuntul",
  " kontol", " bangsat", " asu", " bangsad", " ngentot", " fk"
]

curse_words = [
  "fak", "shit", "cuk", "bangke", "jancuk", "cok", "wtf", "ngentd", "memek",
  "kntl", "idiot", "bgst", "goblok", "noob", "tolol", "meki", "jnck", "kimak",
  "qmak", "fuck", "n00b", "jancok", "cog", "kuntul", "kontol", "bangsat",
  "asu", "bangsad", "ngentot", "fk"
]

sad_words = [
  "sedih", "depresi", "males", "ngamuk", "bunuh diri", "bundir", "malas",
  "cape", "capek", "kms", "kys"
]

laugh_words = ["kekw", "wkwk", "lol", "haha"]

starter_encouragement = [
  "Don't give up!", "Use your ultra heart to believe!", "I know you can do it!"
]

starter_anticurse = [
  "Hey, watch your language!", "Im not Indonesian, but sounds a bad word!",
  "Haha will never use that word!", "I will send you The Rumbling",
  "Hey hey don't ngeGAS"
]

#khusus louis
louis = [
  "meso ae lou lou", "Hey, watch your language!",
  "Im not Indonesian, but sounds a bad word!",
  "Ultramen will never use that word!", "I will send you The Rumbling",
  "Hey hey don't ngeGAS", "Louis sabarlah sedikit, kasihan temen-temenmu itu"
]

melvin = ["Anya tidak suka melvin"]
if "responding" not in db.keys():
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  #q = quote; a = author
  return (quote)


def get_dadjoke():
  response = requests.get("https://https://icanhazdadjoke.com/random/joke")
  json_data = json.loads(response.text)
  dadjoke = json_data[0]['d']
  return (dadjoke)


def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  command, user_message = None, None

  if db["responding"]:
    #announce
    if msg.startswith('$hello'):
      await message.channel.send('Waku waku')

    if msg.startswith('$quote'):
      quote = get_quote()
      await message.channel.send(quote)

    if msg.startswith('$simp'):
      if str(message.author) == "BODREX#1318":
        await message.channel.send(file=discord.File("pdktrexy.jpg"))
      else:
        path = random.choice(os.listdir('simp/'))
        await message.channel.send(file=discord.File("simp/" + path))

    if msg.startswith('$dadjoke'):
      dadjoke = get_dadjoke()
      await message.channel.send(dadjoke)

    if msg.startswith('$meme'):
      await message.channel.send(file=discord.File("meme.gif"))

    if msg.startswith('$ul'):
      pathul = random.choice(os.listdir('Ultraman_Card/'))
      await message.channel.send(file=discord.File("Ultraman_Card/" + pathul))
    if ':v' in msg.lower():
      await message.channel.send("One of Chichi :v")

    if 'pokedraw' in msg.lower():
      await message.channel.send("Get some help, melvin ajg")

    if msg.startswith("$moyai"):
      await message.channel.send(":moyai:")

    if msg.startswith("Oh Lexy"):
      await message.channel.send(file=discord.File("Oh_Lexy.jpg"))

    if 'nonton' in msg.lower():
      await message.channel.send("SPY WARS!!!")

    if 'smh' in msg.lower() and not msg == 'smh':
      await message.channel.send("Get some help from Ultraman!")

    if msg == 'smh':
      await message.channel.send("santuy Dyno")

    if 'petra' in msg.lower() or 'ukp' in msg.lower() or 'pcu' in msg.lower():
      await message.channel.send("Worst School, you should not be there")

    if message.content.startswith('$anya'):
      command = msg.split(' ')[0]
      user_message = msg.replace('$anya', '')
      print(command, user_message)

    if command == '$anya':
      async with message.channel.typing():
        bot_response = chatgpt_response(prompt=user_message)
      chunks = textwrap.wrap(bot_response, width=2000)
      i = 0
      for chunk in chunks:
        print(i)
        i += 1
        await message.channel.send(f'{message.author.mention} {chunk}')

    if msg.startswith("$wgg"):
      await message.channel.send("Semangat WGG!!!")

    if msg.startswith("$katabijak"):
      await message.channel.send(file=discord.File("toxic.mp4"))

    if msg.startswith("$jpop"):
      await message.channel.send("Updating")

    if msg.startswith("$kpop"):
      await message.channel.send("updating")

    if 'tatakae' in msg.lower():
      if str(message.author) == "darrellcr#2600":
        await message.channel.send(file=discord.File("DarrellEren.jpg"))
      elif str(message.author) == "Cools#5256":
        await message.channel.send(file=discord.File("brimstonekenny.jpg"))
      else:
        await message.channel.send(file=discord.File("Eren.jpg"))

    if 'kartika' in msg.lower() and str(message.author) == "0new4y#9371":
      await message.channel.send(file=discord.File("RumblingAdi.jpeg"))

    if 'kontol' in msg.lower():
      await message.channel.send("Apa itu? Jenis pisang yang baru?")

    #di bawah ini untuk sad_words response
    options = starter_encouragement
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])

    if any(word in msg.lower() for word in sad_words):
      await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
      encouraging_message = msg.split("$new ", 1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New Encouraging message added")

    if msg.startswith("$del"):
      encouragements = []
      if "encouragements" in db.keys():
        index = int(msg.split("$del", 1)[1])
        delete_encouragements(index)
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)

    if msg.startswith("$list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)

    if any(word in msg.lower() for word in curse_words_space):
      if str(message.author) == "Cyanide#4771":
        await message.channel.send(random.choice(louis))
      elif str(message.author) == "arisa#0001":
        await message.channel.send(random.choice(melvin))
      else:
        await message.channel.send(random.choice(starter_anticurse))
      if 'anya' in msg.lower():
        await message.channel.send(str(message.author.name) + " baka!!!")

    elif any(word in msg.lower() for word in curse_words_anti_space):
      if str(message.author) == "Cyanide#4771":
        await message.channel.send(random.choice(louis))
      elif str(message.author) == "arisa#0001":
        await message.channel.send(random.choice(melvin))
      else:
        await message.channel.send(random.choice(starter_anticurse))
      if 'anya' in msg.lower():
        await message.channel.send(str(message.author.name) + " baka!!!")

    if any(msg.lower() == word for word in curse_words):
      if str(message.author) == "Cyanide#4771":
        await message.channel.send(random.choice(louis))
      else:
        await message.channel.send(random.choice(starter_anticurse))

    if 'cok' in msg.lower() and not message.author.bot:
      global cok
      file = open("counterfile.txt", "r+")
      cok = int(file.read())
      cok += 1
      await message.channel.send("**cok** Global Counter: " + str(cok))
      if cok % 100 == 0:
        await message.channel.send("Congrats we surpassed " + str(cok) +
                                   " cok @everyone")
        if cok > 500:
          await message.channel.send("Coming soon for 1000th special cok")
      file.close()
      file = open("counterfile.txt", "w+")
      file.write(str(cok))
      file.close()

    if ':ded:' in msg.lower():
      global ded
      file = open("counterfile_ded.txt", "r+")
      ded = int(file.read())
      if message.author.bot and str(message.author) != "YAGPDB.xyz#8760":
        ded += 1
        await message.channel.send("How many **ded**: " + str(ded))

        if ded % 100 == 0:
          await message.channel.send("Unfortunately, we surpassed " +
                                     str(ded) + " **ded** @everyone")
      file.close()
      file = open("counterfile_ded.txt", "w+")
      file.write(str(ded))
      file.close()

  # if any(word in msg.lower() for word in laugh_words):
  #  await message.channel.send("Human/bot's Laughter is beautiful")
    if msg.startswith("$counter"):
      file = open("counterfile.txt", "r+")
      file2 = open("counterfile_ded.txt", "r+")
      cok = int(file.read())
      ded = int(file2.read())
      await message.channel.send("**cok** Global Counter: " + str(cok))
      await message.channel.send("How many **ded**: " + str(ded))
      file.close()
      file2.close()

  if msg.startswith("$responding"):
    value = msg.split("$responding ", 1)[1]
    if value.lower() == "on":
      db["responding"] = True
      await message.channel.send("Responding ON")
    elif value.lower() == 'off':
      db["responding"] = False
      await message.channel.send("Responding OFF")

  if msg.startswith('$guide'):
    await message.channel.send(
      "```HOW TO USE ANYA\n$hello for say hello to ANYA\n$quote for getting random quote\n$simp to show your favorite vtuber(dasar simp)\n$meme for our favorite meme\n$ul to show my ultramen friends\n$jpop to see the latest top J-Pop\n$kpop to see the latest top K-Pop\n$moyai for :moyai:\n$katabijak for kata bijak\n$responding ON to turn on the bot\n$responding OFF to turn off the bot\n$new for new encourage message\n$del for deleting encourage message\n$list to show the list of encourage messages\nAny curse words or sad words, will get responded by me\nThere we go, enjoy!\n\nAnyway say the magic words to see a magic 'Oh Lexy'```"
    )


keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)  #butuh token
