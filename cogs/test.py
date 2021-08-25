#import discord
import datetime
#import asyncio
from discord.ext import commands#, tasks
from database import data
#from discord_components import DiscordComponents, ComponentsBot, Button


## This cog is for testing new programs ##

class Test(commands.Cog, name='Test'):
	
	def __init__(self, client):
		self.client = client
	print(f'[{datetime.datetime.now()}] cogs.test online!')

	## The default check for this cog whenever a command is used. Returns True if the command is allowed. ##
	async def author_check(self, ctx):  
		return ctx.author.id in self.client.author_id

	



def setup(client):
	client.add_cog(Test(client))