import discord
import asyncio

# permissões(intents) que o bot vai ter
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia  mensagens
intents.members = True  # Permite que o bot acesse eventos relacionados a membros

# Criação do cliente do bot
client = discord.Client(intents=intents)


# Evento que ocorre quando o bot se conecta ao Discord
@client.event
async def on_ready():
    print(f'Bot {client.user} está online!')
    
    # Enviar uma mensagem para você em um canal específico
    guild_id = 1308916432012181554  # ID do servidor
    channel_id = 1308916432452456510  # ID do canal
    
    guild = client.get_guild(guild_id)
    if guild:
        channel = guild.get_channel(channel_id)
        if channel:
            await repeat("smogon", channel)

async def repeat(message: str, channel):
    while True:
        await asyncio.sleep(1)
        await channel.send(message)

from dotenv import load_dotenv
import os

load_dotenv() # carrega as variaveis

token = os.getenv("DISCORD_BOT_TOKEN_TEST") 

# Coloque o token do seu bot aqui
client.run(token)
