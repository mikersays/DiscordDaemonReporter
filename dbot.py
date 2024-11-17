import discord
import subprocess

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent to read messages
client = discord.Client(intents=intents)

# Function to check if both 'service1' and 'service2' are running as processes
def check_services():
    try:
        # Check if 'service1' is running by exact process name match
        service1_status = subprocess.run(['pgrep', '-x', '<service name>'], capture_output=True, text=True)
        service1_online = bool(service1_status.stdout.strip())

        # Check if 'realmd' is running by exact process name match
        service2_status= subprocess.run(['pgrep', '-x', '<service name>'], capture_output=True, text=True)
        service2_online= bool(service2_status.stdout.strip())

        if service1_online and service2_online:
            return "✅ <replaceme> is online."
        else:
            return "❌ <replaceme> is offline. Please check the scripts."
    except Exception as e:
        return f"⚠️ Error checking <replaceme>'s status: {str(e)}"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the user has sent the command to check the services
    if message.content.lower() == '!status':
        service_status = check_services()
        await message.channel.send(service_status)

# Run the bot
client.run(TOKEN)

