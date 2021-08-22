import datetime
import random
from discord.ext import commands


class WelcomeMessage(commands.Cog, name='Welcome Message'):

	def __init__(self, client):
		self.client = client
		print(f'[{datetime.datetime.now()}] cogs.welcome_message online!')


	## Sends user welcome message ##
	@commands.Cog.listener()
	async def on_member_join(self, member):
		first = [f'<@!{member.id}>, welcome to Guild Wars 2 University!', 
			f'Welcome <@!{member.id}> to Guild Wars 2 University!', 
			f'Welcome <@!{member.id}>!', 
			f'Welcome to Guild Wars 2 University, <@!{member.id}>!']
		last = ['Feel free to introduce yourself.', 
			'Feel free to introduce yourself here if you want.', 
			'Please introduce yourself here.', 
			'Please introduce yourself here if you want.', 
			'What is your favorite class in the game?', 
			'How long have you been playing Guild Wars 2?', 
			'You can ask any questions you have in <#736254186353721454>.', 
			'Check out our Guild Wars 2 guide in <#797318280826191922>.', 
			'Go to <#735989626455457894> to get roles so you can be notified about specific groups and see related channels.', 
			'It is recommend to change your discord nickname to your Gw2 account name, so that people can identify you in-game.', 
			'Go to <#852189307031781426> to see when regular events happen.']
		await self.client.get_channel(879009714069962843).send(f'{random.choice(first)} {random.choice(last)}')


def setup(client):
	client.add_cog(WelcomeMessage(client))