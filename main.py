import discord
import os
import requests
import json

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "lonely", "angry", "misurable", "depressing"]

starter_encouragements = [
  "Cheer Up!"
  "Hang in there"
  "You are a great person"
  "You are gorgeous"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0] ['q']  + " -" + json_data[0] ['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('hey'):
    await message.channel.send('Hello! My boy!')
  
  if message.content.startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any (wrong in msg for word in sad_words):await message.channel.send(random_choise(starter_encouragements))

client.run(os.getenv('TOKEN'))
