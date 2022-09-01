#MTAwNzE3Mzc1OTYyMDM2MjI2MQ.G_IyAs.WlIua0f17b03-wUaV2r4eD0KFSKT9X5Pl9Mzdk

# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from tokenize import Token
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
GUILD = os.getenv('DISCORD_GUILD')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
client = discord.Client(intents=discord.Intents.default())

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run('MTAwNzE3Mzc1OTYyMDM2MjI2MQ.G_IyAs.WlIua0f17b03-wUaV2r4eD0KFSKT9X5Pl9Mzdk'
)