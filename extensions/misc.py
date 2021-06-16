import discord
from discord import Embed, Color
from discord.ext import commands

import json

data = json.load(open('data.json', 'r'))

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client   

    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        if ctx.author.id in data['bannedids']:
            await ctx.send(':no_entry_sign: **Sorry, but you are banned from using Nen!**\n **Please contact the owner on the official server to appeal for unban**')
            return
            
        embed = Embed(
            title = 'Invite Nen',
            description = f'**Senpai can invite Nen into their own servers\' and help me grow!**\n**[Invite me senpai!]({data["invite"]} "Invite Nen to any server you want, senpai!")**', 
            color = Color.darker_gray()
        )

        embed.url = data['invite']
        embed.set_thumbnail(url = self.client.user.avatar_url)
        embed.set_footer(text = f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url = ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        embed = Embed(
            title = f'Vote for Nen!',
            description = f'**Senpai can vote for Nen at top.gg!**\n**[Vote Here!]({data["vote"]})**\nBy voting you can help Nen grow and find its home\nin many servers!', 
            color = Color.darker_gray()
        )

        embed.url = data['vote']
        embed.set_thumbnail(url = self.client.user.avatar_url)
        embed.set_footer(text = f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url = ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def embed(self, ctx, title, desc):
        if ctx.author.id in data['bannedids']:
            await ctx.send(':no_entry_sign: **Sorry, but you are banned from using Nen!**\n **Please contact the owner on the official server to appeal for unban**')
            return
            
        embed = Embed(
            title = title, 
            description = desc, 
            color = discord.Color.darker_gray()
        )
        await ctx.send(embed = embed)
        
    @commands.command(aliases=["stats"])
    async def status(self,ctx):
        latency = self.client.latency
        guildcount = len(self.client.guilds)

        membercount = 0
        for guild in self.client.guilds:
          membercount += len(guild.members)

        channelcount = 0
        for guild in self.client.guilds:
          channelcount += len(guild.channels)

        embed = Embed(
            title = "Nen\'s Status",
            description=f"Latency: **{round(latency*1000)}ms**\nServers: **{guildcount}**\nMembers: **{membercount}**\nChannels: **{channelcount}**"
        )
        await ctx.send(embed=embed)

    @commands.command(aliases = ['cred'])
    async def credits(self, ctx):
      await ctx.send('`Nen was made by Ultimus-senpai and Weeblet-kun`\n`Doujins are provided by nhentai.net`')

def setup(client):
    client.add_cog(Misc(client))
