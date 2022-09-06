import os
import discord
from dotenv import load_dotenv
from random import randint
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
            await message.channel.send(bot_gif())
        elif message.content.startswith('!'):
            await message.channel.send(bot_text_reply(message.content))
        elif msg_reaction(message.content):
            await message.add_reaction(msg_reaction(message.content))


    client.run(TOKEN)

# Returns a silly reply based on a specific command in the channel
def bot_text_reply(msg):
    response = {
        "hi": "Howdy, Dumplin!", "carrot": "NOM NOM NOM NOM", "hullo": "hullo, earth!",
        "muah": "MUAH MUAH MUAH MUAH!", "failed": "looks like it work to me!", "pull": "*FEIGNS DEATH*",
        "aggro": "TUNT! ***ROARS***"
    }
    msg = msg.lstrip('!').lower()
    if msg in response:
        return response[msg]

    else:
        return "Idk what's goin on..."

# Returns random panda or dumpling, or watermelon gif link
def bot_gif():
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

# Adds a reaction to a message event, based on message content
def msg_reaction(msg):
    emoji_response = {
        "dumpling": "🐢", "honey": "😍", "hog": "🐽", "melon": "🍉",
        "chonky": "🐼"
    }
    if msg.lower() in emoji_response:
        return emoji_response[msg.lower()]
        

if __name__ == "__main__":
    main()