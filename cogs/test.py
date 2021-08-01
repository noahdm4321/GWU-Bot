import discord
import datetime
#import asyncio
from discord.ext import commands, tasks


## These are the commands for testing ##

class ModCommands(commands.Cog, name='Test'):
	
	def __init__(self, client):
		self.client = client
	print(f'[{datetime.datetime.now()}] cogs.test online!')

	## The default check for this cog whenever a command is used. Returns True if the command is allowed. ##
	async def cog_check(self, ctx):  
		return ctx.author.id == self.client.author_id

	



def setup(client):
	client.add_cog(ModCommands(client))