import discord
import datetime
from discord.ext import commands
from threading import Timer


## These are the commands for testing ##

class ModCommands(commands.Cog, name='Test'):
	
	def __init__(self, client):
		self.client = client
	print(f'[{datetime.datetime.now()}] cogs.test online!')

	## The default check for this cog whenever a command is used. Returns True if the command is allowed. ##
#	async def cog_check(self, ctx):  
#		return ctx.author.id == self.client.author_id

	def current_time(self):
		return datetime.datetime.now().strftime("%a, %H:%M - UTC")

	## Change time channel ##
	@commands.Cog.listener()
	async def on_ready(self):
		self.threading.Timer(60, self.current_time).start()
		await self.client.get_channel(843186187018436618).edit(name=self.current_time())
		print(self.current_time())


def setup(client):
	client.add_cog(ModCommands(client))