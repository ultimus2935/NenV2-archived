import discord
from discord import Color, Embed, File
from discord.ext import commands

import json
import string

import nhentai as nh

data = json.load(open('data.json', 'r'))

class DoujinSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tags(self, ctx, code: int):
        if ctx.author.id in data['bannedids']:
            await ctx.send(':no_entry_sign: **Sorry, but you are banned from using Nen!**\n **Please contact the owner on the official server to appeal for unban**')
            return

        if isinstance(code, int):
            nsfwlogo = File("assets/images/nsfwlogo.png", filename="nsfwlogo.png")

            try: 
                doujin = nh.get_doujin(code)
                title = doujin.titles['pretty']

                tagmsg = ''

                for tag in doujin.tags:
                    if tag.count > 999: tagnum = str(tag.count)[:-3] + 'k'
                    else: tagnum = str(tag.count)

                    tagmsg += f'**`{tag.name}: `**`{tagnum},`   '

                embed = Embed(
                    title = f'Tags of {code}',
                    color = Color.darker_gray() 
                )

                embed.url = doujin.url

                embed.add_field(name = 'Tags of doujin:', value = tagmsg, inline = False)

                if ctx.channel.is_nsfw() or ctx.channel.id in data['pseudo_nsfw']: embed.set_thumbnail(url = doujin.thumbnail)
                else: embed.set_thumbnail(url = 'attachment://nsfwlogo.png')

                embed.set_footer(
                    text = f'Requested by {ctx.author.name}#{ctx.author.discriminator}', 
                    icon_url = ctx.author.avatar_url
                )

                if ctx.channel.is_nsfw() or ctx.channel.id in data['pseudo_nsfw']: await ctx.send(embed = embed)
                else: await ctx.send(file = nsfwlogo, embed = embed)

            except Exception as e:
                print(e)
                if str(e) == 'A doujin with the given id wasn\'t found': 
                    await ctx.send('`Sorry senpai, but the doujin was not found!`')
        
        else: await ctx.send('`I don\'t think thats a code, senpai....`')

    @commands.command()
    async def random(self, ctx):
        if ctx.author.id in data['bannedids']:
            await ctx.send(':no_entry_sign: **Sorry, but you are banned from using Nen!**\n **Please contact the owner on the official server to appeal for unban**')
            return

        code = nh.get_random_id()

        await self.info(ctx, code)

    @commands.command()
    async def info(self, ctx, code: int):
        if ctx.author.id in data['bannedids']:
            await ctx.send(':no_entry_sign: **Sorry, but you are banned from using Nen!**\n **Please contact the owner on the official server to appeal for unban**')
            return

        if isinstance(code, int):
            nsfwlogo = File("assets/images/nsfwlogo.png", filename="nsfwlogo.png")

            try:
                doujin = nh.get_doujin(code)

                title = doujin.titles['pretty']
                engtitle = doujin.titles['english']
                japtitle = doujin.titles['japanese']

                language = ''
                
                for tag in doujin.tags:
                    if tag.type == 'language':
                        language += tag.name.capitalize() + ' \n'

                artist = ''

                for tag in doujin.tags:
                    if tag.type == 'artist':
                        artist += string.capwords(tag.name) + ' \n'

                pagecount = 0

                for page in doujin.pages:
                    pagecount += 1

                tagcount = 0

                for tag in doujin.tags:
                    tagcount += 1

                tagmsg = ''

                for tag in doujin.tags:
                    if tag.count > 999: tagnum = str(tag.count)[:-3] + 'k'
                    else: tagnum = str(tag.count)

                    tagmsg += f'**`{tag.name}: `**`{tagnum},`   '

                embed = Embed(
                    title = f'{title}',
                    description = f'Full English Title: `{engtitle}`\nJapanese Title: `{japtitle}`\n\u200b',
                    color = Color.darker_gray()
                )

                embed.url = doujin.url

                embed.add_field(name = 'Code', value = doujin.id, inline= True)
                embed.add_field(name = 'Media ID', value = doujin.media_id, inline= True)
                embed.add_field(name = 'Artist', value  = artist, inline = True)
                embed.add_field(name =  'Language', value = language, inline = True)
                embed.add_field(name = 'Pages', value = pagecount, inline= True)
                embed.add_field(name = 'Favorites', value = doujin.favorites, inline= True)

                embed.add_field(name =  'Tags', value = tagmsg, inline = False)

                if ctx.channel.is_nsfw() or ctx.channel.id in data['pseudo_nsfw']: embed.set_thumbnail(url = doujin.thumbnail)
                else: embed.set_thumbnail(url = 'attachment://nsfwlogo.png')

                embed.set_footer(
                    text = f'Requested by {ctx.author.name}#{ctx.author.discriminator}', 
                    icon_url = ctx.author.avatar_url
                )

                if ctx.channel.is_nsfw() or ctx.channel.id in data['pseudo_nsfw']: await ctx.send(embed = embed)
                else: await ctx.send(file = nsfwlogo, embed = embed)

            except Exception as e:
                print(e)
                if str(e) == 'A doujin with the given id wasn\'t found': 
                    await ctx.send('`Sorry senpai, but the doujin was not found!`')
        
        else: await ctx.send('`I don\'t think thats a code, senpai....`')

    @commands.command()
    async def search(self, ctx, query, pageno = 1):
        if ctx.author.id in data['bannedids']:
            await ctx.send(':no_entry_sign: **Sorry, but you are banned from using Nen!**\n **Please contact the owner on the official server to appeal for unban**')
            return

        doujinlist = []
        doujinlist.extend(nh.search(query = query, page = 1, sort_by = 'popular'))
        doujinlist.extend(nh.search(query = query, page = 2, sort_by = 'popular'))

        partitions = int(len(doujinlist) / 5)

        titlegroups = []

        for i in range(partitions):
            i += 1

            start = (i * 5) - 5
            end = i * 5

            titlegroup = []

            for index in range(len(doujinlist)):
                if index >= start and index < end:
                    doujin = doujinlist[index]
                    title = doujin.titles["pretty"]
                    
                    titlemsg =  f'`{title}: `**`{doujin.id}`**\n'

                    titlegroup.append(titlemsg)

            titlegroups.append(titlegroup)

            i -= 1

        if len(titlegroups) == 0:
            await ctx.send('`No results where found, senpai!`')

        else:
            embed = Embed(
                title = f'Search Results for: \"{query}\"',
                color = Color.darker_gray()
            )

            embed.set_footer(
                text = f'Requested by {ctx.author.name}#{ctx.author.discriminator}, Page: {pageno}', 
                icon_url = ctx.author.avatar_url
            )

            titlegroup = titlegroups[pageno]

            titlemsg = ''
            
            for title in titlegroup:
                titlemsg += title

            embed.description =  f'{titlemsg}'

            await ctx.send(embed = embed)
            

def setup(client):
    client.add_cog(DoujinSearch(client))
