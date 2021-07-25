import discord
import datetime
from discord.ext import commands, tasks


## These are the events for server moderation ##

class ModEvents(commands.Cog, name='Moderator Events'):

	def __init__(self, client):
		self.client = client
	print(f'[{datetime.datetime.now()}] cogs.mod_events online!')



@tasks.loop(minutes=1)
async def time_update(self):
	time = datetime.datetime.now().strftime("%a, %H:%M - UTC")
	await self.client.get_channel(843186187018436618).edit(name=time)
	print(time)


## Sends user join message ##
@commands.Cog.listener()
async def on_member_join(self, member):
	print(f'[{datetime.datetime.now()}] {member} has joined the server.')

## Sends user leave message ##
@commands.Cog.listener()
async def on_member_remove(self, member):
	print(f'[{datetime.datetime.now()}] {member} has left the server.')


def setup(client):
	client.add_cog(ModEvents(client))