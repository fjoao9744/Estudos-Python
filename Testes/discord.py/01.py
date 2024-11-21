import discord

intents = discord.Intents.default()  # Isso inclui os intents padrões
intents.message_content = True  # Permite que o bot leia o conteúdo das mensagens
intents.members = True  # Permite que o bot acesse eventos relacionados a membros

# Criação do cliente do bot
client = discord.Client(intents=intents)

# Evento que ocorre quando o bot se conecta ao Discord
@client.event
async def on_ready():
    print(f'Bot {client.user} está online!')
    
    # Enviar uma mensagem para você em um canal específico
    # Aqui você usa o ID do servidor (guild) e o ID do canal
    guild_id = '1199119392030605444'  # Substitua pelo seu ID
    channel_id = '1199119393641205762'  # Substitua pelo ID do canal onde quer enviar a mensagem
    
    guild = client.get_guild(int(guild_id))
    if guild:
        channel = guild.get_channel(int(channel_id))
        if channel:
            await channel.send('smogon')

from dotenv import load_dotenv
import os

load_dotenv() # carrega as variaveis

token = os.getenv("DISCORD_SERVER_TOKEN") 

# Coloque o token do seu bot aqui
client.run(token)
