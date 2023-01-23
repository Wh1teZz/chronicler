import discord

TOKEN = 'MTA2NjYzMDY5NDUwOTQ5NDI4Mg.Gw-Ikc.8MmLcCFVGQv-HjN4eHC2jL1bI8se4gl-A-ajlc'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as", client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print (f'{username} sent: {user_message}')

    if username == "JZT":
        await message.channel.send(f'Hello world!')
        return

    if user_message.lower() == "hello bot":
        await message.channel.send(f'Hello {username}!')
        return

client.run(TOKEN)