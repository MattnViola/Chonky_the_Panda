# Chonky the Panda, a Discord Bot
#### Video Demo: https://youtu.be/l60mQqmXJGM
#### Description:

This is a relatively simple discord chat bot I made for my personal server, as well as for the final project of CS50P. Chonky the Panda, a character my friends and I created long ago, is a simple minded panda, whose optimism and humbleness wins you over.

After I had interest in making a discord bot, I googled for a tutorial video that would start me off with the basics of using discord's API, as well as getting used to some of the new syntax with things like asyncronous functions, where specific operations start after reciept of a signal that the precious operation was completed. Unfortunately, the video's intention was to have someone absolutely unfamiliar with python be able to copy what is written, without any nuance as to what any line of code actually does, as well as being out of date for discords API.

I then delved into Discords quickstart guide, as well as it's own documentation to work through and get a moderate level of nuance on making a discord bot.

### Code walkthrough/thought process:

```
import os
import discord
from dotenv import load_dotenv
from random import randint
import requests
```
os and dotenv are used to load a .env file, to have a secure place to store my Discord and GIPHY token/key. Random and requests are used inside of the bot_gif() function. discord is used to connect to discord API.

```
load_dotenv()
TOKEN = os.getenv('TOKEN')
GIPHYKEY = os.getenv('GIPHY_KEY')
```

Loads a .env file in the same directory, and makes the computer think that the keys there are environment variables. Making them more securely hidden.

```
def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f"{client.user} is here!")
```

The beginning of main starts with a variable, intents, becoming the intents object in the discord API. This intents object determines the abilities/allowances of the bot. It's then modified by the default() method to have the default settings, and then has its message_content property set to True, making the bot able to see user messages on a discord server.

The client variable is the initialized client object, aka Chonky, and his intents is set to the intents variable, giving him the settings we just applied to the intents variable.

@client.event is a function that is called when an event happens in a server Chonky is in. on_ready() is called when the bot is successfully online. 

```
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
```

Async def on_message is called when a message is posted within a chatroom the bot has access to. The message is an object with various information attached. if message.author is the same as the bot, the function returns to prevent recursion from its own messages.

The bot then checks the message contents, and if any of the conditionals are proven true, it "await"s a post from itself in the same channel, containing the contents of the proceding function. 

client.run(TOKEN) starts the bot client, using the bots token. 

### Function Descriptions

bot_text_reply- where if the message content starts with !, but not !gif, if the message content is a key in a written dictionary, the function returns its value pair.

bot_gif- where if the message content starts with !gif, a random gif from 3 randomized tags is called from GIPHY's API, and a url is returned.

msg_reaction- where if the message is a key in the emoji_response dictionary, it returns its value pair.