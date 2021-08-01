import datetime
from discord.ext import commands, tasks


## These are the events for the server ##

class ServerEvents(commands.Cog, name='Server Events'):

	def __init__(self, client):
		self.client = client
		for guild in self.client.guilds:
			if guild.id == 446550730640195586:
				self.channelclock = 775870306798534696
				break
			elif guild.id == 843186186344464414:
				self.channelclock = 843186187018436618
				break
		self.clock_name.start()
	print(f'[{datetime.datetime.now()}] cogs.server_events online!')


	## Updates Server Clock Channel ##
	@tasks.loop(minutes=1)
	async def clock_name(self):
		if datetime.datetime.now().strftime("%p") == 'PM':
			reset = f'Reset-{12-int(datetime.datetime.now().strftime("%-I"))}'
		elif datetime.datetime.now().strftime("%p") == 'AM':
			reset = f'Reset+{datetime.datetime.now().strftime("%-I")}'
		current_time = f'{reset}　|　{datetime.datetime.now().strftime("%H:%M")} - UTC'
		await self.client.get_channel(self.channelclock).edit(name=current_time)


def setup(client):
	client.add_cog(ServerEvents(client))