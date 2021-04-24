import discord
from discord import Embed
from discord import Color
from discord.ext import commands

import json

from extensions.helptext import helpText as ht

data = json.load(open('data.json', 'r'))

class   Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *, param = ''):


        embed = Embed()
        embed.color = Color.darker_gray()

        # n.help doujin
        if param == 'doujin': 
            embed.title = f'Nen sent senpai some help!\n\n{ht.doujin_title}'
            embed.description = ht.doujinhelp

        # n.help read
        elif param == 'read': 
            embed.title = f'Nen sent senpai some help!\n\n{ht.read_title}'
            embed.description = ht.readhelp

        # n.help misc
        elif param == 'misc': 
            embed.title = f'Nen sent senpai some help!\n\n{ht.misc_title}'
            embed.description = ht.mischelp

        # n.help reddit --- currently disabled
        elif param == 'reddit':
            embed.title = f'Nen sent senpai some help!\n\n{ht.reddit_title}'
            embed.description = ht.reddithelp

        # n.help
        else: 
            embed.title = f'Nen sent senpai some help!\n\n{ht.main_title}'
            embed.description = ht.mainhelp
            

        embed.set_footer(text = f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url = ctx.author.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
