import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.messages = True
intents.guilds = True
intents.typing = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Predefined Gmail addresses and passwords
gmail_credentials = {
    'example1@gmail.com': 'password1',
    'example2@gmail.com': 'password2',
    'example3@gmail.com': 'password3'
}

# ID of the allowed channel
allowed_channel_id = 1126883292189302804

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def gen2(ctx):
    if ctx.channel.id != allowed_channel_id:
        return  # Do nothing if the command is used in a different channel
    
    if gmail_credentials:
        gmail_address, password = gmail_credentials.popitem()
        try:
            dm_channel = await ctx.author.create_dm()
            await dm_channel.send(f'Gmail address: {gmail_address}\nPassword: {password}')
            await ctx.send(f'Check DMs for the Gmail credentials, {ctx.author.mention}!')
        except discord.Forbidden:
            await ctx.send("I don't have permission to send you direct messages.")
        except discord.HTTPException:
            await ctx.send("An error occurred while trying to send you direct messages.")
    else:
        await ctx.send('No more credentials available.')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTEyNjg4NjM1MzkzNDc0NTYxMA.G5WkpO.v3i2IkKsNgaYTfD-Dd2rCcREdGQZ9-WTHPnZX8')