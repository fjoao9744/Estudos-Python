from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente
load_dotenv()

# Definir as permissões (intents) que o bot vai ter
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia mensagens
intents.members = True  # Permite que o bot acesse eventos relacionados a membros

# Criar o bot com o prefixo "!s"
bot = commands.Bot(command_prefix="! ", intents=intents)

# Evento que ocorre quando o bot se conecta ao Discord
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

# Comando "propos"
@bot.command()
async def repete(ctx, *, message: str):
    await ctx.send(message)

# Rodar o bot com o token
token = os.getenv("DISCORD_BOT_TOKEN_TEST")
bot.run(token)
