from dotenv import load_dotenv
import os
import discord

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
    # Aqui você usa o ID do servidor (guild) e o ID do canal
    guild_id = '1308916432012181554'  # Substitua pelo seu ID
    channel_id = '1308916432452456510'  # Substitua pelo ID do canal onde quer enviar a mensagem
    
    guild = client.get_guild(int(guild_id))
    if guild:
        channel = guild.get_channel(int(channel_id))
        if channel:
            await channel.send('smogon')


load_dotenv() # carrega as variaveis

token = os.getenv("DISCORD_BOT_TOKEN_TEST") 

# Coloque o token do seu bot aqui
client.run(token)
