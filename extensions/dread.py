import discord
from discord import Color, Embed
from discord.ext import commands

import json
import textwrap

import nhentai as nh
from disputils import BotEmbedPaginator

wrapper = textwrap.TextWrapper(width=25)

data = json.load(open('data.json','r'))

class DoujinRead(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def read(self, ctx, code: int):
        if ctx.channel.is_nsfw() or ctx.channel.id in data['pseudo_nsfw']:
            if isinstance(code, int):
                try:
                    doujin = nh.get_doujin(code)

                    # Wrapping the title
                    title = doujin.titles['pretty']
                    titlelist = wrapper.wrap(text = title)
                    wrappedtitle = ''

                    for titlepart in titlelist:
                        wrappedtitle += f'{titlepart}\n'

                    pages = []

                    for page in doujin.pages:
                        embed = Embed(
                            title = f"Reading: {wrappedtitle}",
                            color =  Color.darker_gray()
                        )
                        embed.url = doujin.url

                        embed.set_image(url=page.url)
                        pages.append(embed)

                    paginator = BotEmbedPaginator(ctx, pages)
                    await paginator.run()

                except Exception as e:
                    print(e)
                    if str(e) == 'A doujin with the given id wasn\'t found':      
                        await ctx.send('`Sorry senpai, but the doujin was not found!`')

            else: await ctx.send('`I don\'t think thats a code, senpai....`')
        else: await ctx.send("`Sorry but senpai needs to be in a NSFW channel to read this :(`")
        

def setup(client):
    client.add_cog(DoujinRead(client))
