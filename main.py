import os
import discord
import datetime
import random
from keep_alive import keep_alive
from discord.ext import commands


client = commands.Bot(
	command_prefix=".",
	case_insensitive=True
)

client.author_id = 243543671293739008
client.guild_id = 843186186344464414
def is_it_me(ctx):
	return ctx.author.id == client.author_id


@client.event 
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name='for . commands', type=discord.ActivityType.listening))
	print(f'[{datetime.datetime.now()}] Bot is ready: {client.user}')

## Sends user join message ##
@client.event 
async def on_member_join(member):
	print('join')
	print(f'[{datetime.datetime.now()}] {member} has joined the server.')

## Sends user leave message ##
@client.event 
async def on_member_remove(member):
	print('leave')
	print(f'[{datetime.datetime.now()}] {member} has left the server.')

## Log user messages ##
#@client.event 
#async def on_message(ctx):
#	print(f'[{datetime.datetime.now()}] {ctx.author} sent {ctx.id} in #{ctx.channel}')


## Test command - Welcome message ##
@client.command()
@commands.check(is_it_me)
async def test(ctx):
	first = [f'<@!{ctx.author.id}>, welcome to Guild Wars 2 University!', 
		f'Welcome <@!{ctx.author.id}> to Guild Wars 2 University!', 
		f'Welcome <@!{ctx.author.id}>!', 
		f'Welcome to Guild Wars 2 University, <@!{ctx.author.id}>!']
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
	await ctx.send(f'{random.choice(first)} {random.choice(last)}')
	print(f'[{datetime.datetime.now()}] {ctx.author} tested in #{ctx.channel}')


extensions = [
	'cogs.cog_commands',  # Same name as it would be if you were importing it
	'cogs.mod_commands',
	'cogs.mod_events',
	'cogs.server_commands']

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		client.load_extension(extension)  # Loades every extension.


keep_alive()
client.run(os.environ['DISCORD_BOT_SECRET'])