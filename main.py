import datetime
import discord, asyncio
from config import token # Create a file named config.py in the same folder and put your config there
from discord import app_commands
from discord.ext import tasks

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "secimvakti", description = "Ne kadar vaktimiz var gör")
async def first_command(interaction):
    await interaction.response.send_message(await secim())

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')
    if not loop.is_running():
        loop.start()
    

async def ch_pr():
    await client.wait_until_ready()
    status = await secim()
    await client.change_presence(activity=discord.Game(name=status))

    await asyncio.sleep(5)

@tasks.loop(seconds=5)
async def loop():
    await ch_pr()

async def secim():
    today = datetime.datetime.today()
    secim = datetime.datetime(2023, 5, 14)
    diff = secim - today
    time = str(diff).split(".")[0]
    time = time.replace("days", "gün")
    return(f"Kurtulmamıza {time} kaldı")


client.run(token)