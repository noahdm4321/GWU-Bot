import datetime
from discord.ext import commands, tasks


class ClockChannel(commands.Cog, name='Clock Channel'):

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
		print(f'[{datetime.datetime.now()}] cogs.clock_channel online!')


	## Updates Server Clock Channel ##
	@tasks.loop(minutes=10)
	async def clock_name(self):
		if datetime.datetime.utcnow().strftime("%p") == 'PM':
			if datetime.datetime.utcnow().strftime("%I") == 12:
				reset = f'Reset±12'
			else:
				reset = f'Reset-{12-int(datetime.datetime.utcnow().strftime("%I"))}'
		elif datetime.datetime.utcnow().strftime("%p") == 'AM':
			if datetime.datetime.utcnow().strftime("%I") == 12:
				reset = f'Reset!!!'
			else:
				reset = f'Reset+{datetime.datetime.utcnow().strftime("%I")}'
		current_time = f'{reset}　|　{datetime.datetime.utcnow().strftime("%H:%M")} - UTC'
		await self.client.get_channel(self.channelclock).edit(name=current_time)
		print(f'Updated clock: {datetime.datetime.utcnow().strftime("%H:%M")}')


def setup(client):
	client.add_cog(ClockChannel(client))