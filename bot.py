import discord
from discord.ext import commands
import os
import subprocess

# Load bot token from environment variables (Pella hosting best practice)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def edit_save(ctx, save_data: str):
    """Edits save data using BCSFE-Python."""
    try:
        # Run BCSFE-Python with the given save data
        process = subprocess.run(['python', 'bcsfe.py', 'edit_save', save_data], capture_output=True, text=True)
        result = process.stdout if process.stdout else process.stderr
        await ctx.send(f"Edited save data: {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command()
async def get_transfer_code(ctx):
    """Generates and sends a transfer code and confirmation code."""
    try:
        # Run BCSFE-Python to generate transfer and confirmation codes
        process = subprocess.run(['python', 'bcsfe.py', 'generate_transfer_codes'], capture_output=True, text=True)
        result = process.stdout if process.stdout else process.stderr
        await ctx.send(f"Transfer Code & Confirmation Code: {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Bot token not found. Set DISCORD_BOT_TOKEN in environment variables.")
