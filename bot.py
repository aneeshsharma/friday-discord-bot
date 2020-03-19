import discord
import json
import SocketInterface
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hey Friday,'):
        msg = message.content[11:].strip()
        result = "Cannot Think Right now"
        try:
            sock.send(msg)
            result = sock.recv()[0]
        except:
            print('Unable to send')

        await message.channel.send(result.decode('utf-8'))

dir = os.path.dirname(__file__)
config_filename = "config.json"

abs_path = os.path.join(dir, config_filename)

config_file = open(abs_path, "r")
config = json.loads(config_file.read())

sock = SocketInterface.Socket()
sock.connect("localhost", 7201)

client.run(config['token'])
