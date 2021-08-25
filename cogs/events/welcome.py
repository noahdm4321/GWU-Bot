import datetime
import random
import json
from discord.ext import commands
from database import data


class WelcomeMessage(commands.Cog, name='Welcome Message'):

	def __init__(self, client):
		self.client = client
		self.channel = client.get_channel(879009714069962843)
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
			'Are you excited for the new expansion, End of Dragons?', 
			'Do you have a favorite gamemode or playstyle?', 
			'It is recommend to change your discord nickname to your Gw2 account name, so that people can identify you in-game.']
		await self.channel.send(f'{random.choice(first)} {random.choice(last)}')
		message = data.read('id', 'welcome')
		await self.channel.fetch_massage(message).delete
		m = await self.channel.send("New to Guild Wars 2? Check out our <#797318280826191922>. New to Discord? Check out our <#875232316010668082>.\nIf you still have questions about the Guid Wars 2 or Discord, you can ask in <#736254186353721454>.\nWe have events scheduled in our <#852189307031781426>. Be sure to you have the correct <#735989626455457894> to attend them.")
		data.write('id', 'welcome', m)


def setup(client):
	client.add_cog(WelcomeMessage(client))