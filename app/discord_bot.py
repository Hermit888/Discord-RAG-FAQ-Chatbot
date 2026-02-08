import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv


"""Discord Bot that interacts with users"""

# get token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_URL = os.getenv('API_URL')

# Set up Discord intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize Discord client
client = discord.Client(intents=intents)

def chunk_message(text, chunk_size=1900):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Define command prefix
@client.event
async def on_ready():
    print(f'Logged in as a bot {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!py"):
        question = message.content.replace("!py", "").strip()
        
        payload = {
            'user_id': str(message.author.id),
            'query': question
        }

        res = requests.post(API_URL, json=payload)

        answer = res.json()['answer']

        chunks = chunk_message(answer)
        for chunk in chunks:
            await message.channel.send(chunk)

client.run(TOKEN)