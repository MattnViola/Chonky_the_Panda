import os
import discord
from dotenv import load_dotenv
import cowsay

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is here!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hullo'):
        await message.channel.send('hullo, earth!')

    if message.content.startswith('!carrot'):
        await message.channel.send('NOM NOM NOM NOM')
    
    if message.content.startswith('hi'):
        await message.channel.send('Howdy, Dumplin!')
    
    


client.run(TOKEN)
