import os
import discord
import datetime
import asyncio
from keep_alive import keep_alive
from discord.ext import commands


client = commands.Bot(command_prefix=[".", "<@!868102182128472075> "], case_insensitive=True, intents = discord.Intents.all())

client.author_id = 243543671293739008
def author(ctx):
	return ctx.author.id == client.author_id



@client.event 
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name='for . commands', type=discord.ActivityType.listening))
	print(f'[{datetime.datetime.now()}] Bot is ready: {client.user}')

## Error messages ##
@client.event 
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Missing required arguments.')
	elif isinstance(error, commands.TooManyArguments):
		await ctx.send("What's that last bit for? Now you're confusing me.")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send('You do not have permission to use that command.')
	elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
		await ctx.send('You do not have the proper roles to use that command.')
	elif isinstance(error, commands.NotOwner):
		await ctx.send("That command can only be used by my programmer. And you're not him, are you?")
	elif isinstance(error, (commands.CheckFailure, commands.CheckAnyFailure)):
		await ctx.send('No')
	elif isinstance(error, commands.CommandNotFound):
		await ctx.send('There is no such command in my code. Check your spelling and try again.')
	elif isinstance(error, commands.UserNotFound):
		await ctx.send('User does not exist. Please double check and try again.')
	elif isinstance(error, commands.MessageNotFound):
		await ctx.send('Message does not exist. Please double check and try again.')
	elif isinstance(error, commands.ChannelNotFound):
		await ctx.send('Channel does not exist. Please double check and try again.')
	elif isinstance(error, commands.EmojiNotFound):
		await ctx.send('Emoji does not exist. Please double check and try again.')
	elif isinstance(error, commands.RoleNotFound):
		await ctx.send('Role does not exist. Please double check and try again.')
	elif isinstance(error, commands.GuildNotFound):
		await ctx.send('Server does not exist. Please double check and try again.')
	elif isinstance(error, (commands.BadArgument, commands.BadBoolArgument)):
		await ctx.send('Unrecognizable argument type. Please try again.')
	elif isinstance(error, commands.CommandOnCooldown):
		await ctx.send('Alright, alright. Give me a second. Geez.')
	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send("What did you say? I didn't quite get that.")
	elif isinstance(error, commands.DisabledCommand):
		await ctx.send('That command is no longer supported. Sorry.')
	elif isinstance(error, (commands.ExpectedClosingQuoteError, commands.InvalidEndOfQuotedStringError)):
		await ctx.send("Wait. That's it? You can't leave me hanging like that.")
	elif isinstance(error, commands.UnexpectedQuoteError):
		await ctx.send("Ok. I don't need your sass right now. Try again without quotes.")
	elif isinstance(error, (commands.ExtensionError, commands.ExtensionFailed)):
		await ctx.send('Everything is failing! This is the end for me. Goodbye.')
		await ctx.sent('https://tenor.com/view/everything-is-fine-dog-fire-burning-nothing-wrong-gif-15379714')
		await asyncio.sleep(5)
		await client.change_presence(status=discord.Status.offline)
	elif isinstance(error, commands.ExtensionAlreadyLoaded):
		await ctx.send('I already did that. You want me to do it again?')
	elif isinstance(error, (commands.ExtensionNotFound, commands.ExtensionNotLoaded)):
		await ctx.send("What's that? Sounds pretty cool.")
	elif isinstance(error, commands.NoPrivateMessage):
		await ctx.send('Try asking me on the sever. That might work better.')
		await asyncio.sleep(5)
		await ctx.send('Maybe...')
		await asyncio.sleep(3)
		await ctx.send('Worth a shot at least.')
	elif isinstance(error, commands.PrivateMessageOnly):
		await ctx.send("Let's move this conversation to a private channel. Away from prying eyes.")
	elif isinstance(error, commands.NSFWChannelRequired):
		await ctx.send(":open_mouth: How lewd! I'm afraid my conscience won't allow me to do that.")
		await asyncio.sleep(5)
		await ctx.send("Just because I'm a bot doesn't mean I'm morally indigent.")
	else:
		await ctx.send(f"Unknow error. Ask <@!{client.author_id}>. He'll figure it out.")


## Log user join message ##
@client.event 
async def on_member_join(member):
	print(f'[{datetime.datetime.now()}] {member} has joined the server.')

## Log user leave message ##
@client.event 
async def on_member_remove(member):
	print(f'[{datetime.datetime.now()}] {member} has left the server.')

## Log messages deleted ##
@client.event 
async def on_message_delete(message):
	print(f'[{datetime.datetime.now()}] Message from {message.author} deleted in #{message.channel}: "{message.clean_content}"')



## Extensions to load on startup ##
extensions = ['cogs.cog_commands', 
	'cogs.mod_commands',
	'cogs.mod_events',
	'cogs.server_commands',
	'cogs.server_events']

## Ensures this is the file being ran ##
if __name__ == '__main__':
	for extension in extensions:
		client.load_extension(extension)

## Start Webserver ##
keep_alive()

## Start Bot ##
client.run(os.environ['DISCORD_BOT_TOKEN'])