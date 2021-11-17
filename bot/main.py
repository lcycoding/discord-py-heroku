import os
import discord
client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('擊潰廣告人')
    await client.change_presence(status=discord.Status.idle, activity=game)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if '@everyone' in message.content:
            if len(message.author.roles) <= 3:
                await message.delete()

TOKEN = os.getenv("DISCORD_TOKEN")

if __name__ == "__main__":
    client.run(TOKEN)
