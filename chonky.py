import os
import discord
from dotenv import load_dotenv
from random import randint
import json
import requests

load_dotenv()
TOKEN = os.getenv('TOKEN')
GIPHYKEY = os.getenv('GIPHY_KEY')

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f"{client.user} is here!")

    @client.event
    async def on_message(message):
        #Does not trigger on bot's own messages
        if message.author == client.user:
            return

        if message.content.startswith('!gif'):
            await message.channel.send(bot_pandumplin_gif())
        elif message.content.startswith('!'):
            await message.channel.send(bot_text_reply(message.content))
        else:
            msg_reaction()


    client.run(TOKEN)

# Returns a silly reply based on a specific command in the channel
def bot_text_reply(msg):
    if 'hi' in msg:
        return 'Howdy, Dumplin!'
    elif 'carrot' in msg:
        return 'NOM NOM NOM NOM'
    elif 'hullo' in msg:
        return 'hullo, earth!'

# Returns random panda or dumpling, or watermelon gif link
def bot_pandumplin_gif():
    n = randint(0,2)
    if n == 0:
        response = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={GIPHYKEY}&tag=panda&rating=r")
        o = response.json()
        return o["data"]["images"]["original_mp4"]["mp4"]

    elif n == 1:
        response = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={GIPHYKEY}&tag=dumpling&rating=r")
        o = response.json()
        return o["data"]["images"]["original_mp4"]["mp4"]
        
    elif n == 2:
        response = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={GIPHYKEY}&tag=watermelon&rating=r")
        o = response.json()
        return o["data"]["images"]["original_mp4"]["mp4"]

def msg_reaction(msg):
    return

if __name__ == "__main__":
    main()