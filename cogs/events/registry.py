import discord
import datetime
from discord.ext import commands


class Registry(commands.Cog, name='Member Registry'):

	def __init__(self, client):
		self.client = client
		print(f'[{datetime.datetime.now()}] cogs.registry online!')


	## Sends user join message ##
	@commands.Cog.listener()
	async def on_member_join(self, member):
		embed = discord.Embed(description=f"📥 {member.mention} joined the server!", color=58880, timestamp=datetime.datetime.utcnow())
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="Joined on")
		embed.add_field(name="Member Count", value=member.guild.member_count, inline=False)
		await self.client.get_channel(879009713281462329).send(embed=embed)
	
	## Sends user leave message ##
	@commands.Cog.listener()
	async def on_member_remove(self, member):
		embed = discord.Embed(description=f"📤 {member.mention} left the server!", color=15073281, timestamp=datetime.datetime.utcnow())
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="Left on")
		embed.add_field(name="Member Count", value=member.guild.member_count, inline=False)
		await self.client.get_channel(879009713281462329).send(embed=embed)


def setup(client):
	client.add_cog(Registry(client))