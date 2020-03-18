import discord
import json
import SocketInterface

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('Hey Friday,'):
		msg = message.content[10:].strip()
		result = "Cannot Think Right now"
		try:
			sock.send(msg)
			result = sock.recv()[0]
		except:
			print('Unable to send')

		await message.channel.send(result.decode('utf-8'))

config_file = open("config.json", "r")
config = json.loads(config_file.read())

sock = SocketInterface.Socket()
sock.connect("localhost", 7201)

client.run(config['token'])
