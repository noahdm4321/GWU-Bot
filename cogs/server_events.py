import discord
import datetime
from discord.ext import commands, tasks


## These are the events for the server ##

class ServerEvents(commands.Cog, name='Server Events'):

	def __init__(self, client):
		self.client = client
	print(f'[{datetime.datetime.now()}] cogs.server_events online!')





def setup(client):
	client.add_cog(ServerEvents(client))