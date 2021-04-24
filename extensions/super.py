import discord
from discord.ext import commands

import os
import json

data = json.load(open('data.json', 'r'))     

class Super(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    # Load all Extensions
    def loadCogs(self):
        for filename in os.listdir("extensions"):
            if filename.endswith(".py"):
                try: 
                    extname = f"extensions.{filename[:-3]}"                            
                    self.client.load_extension(extname)
                    print(f" * '{extname}'  has been loaded")
                except Exception as e: print(e)   

    # Unload all Extensions
    def unloadCogs(self):
        for filename in os.listdir("extensions"):
            if filename.endswith(".py"):
                try: 
                    extname = f"extensions.{filename[:-3]}" 

                    if extname != 'extensions.super':
                        print(f" * '{extname}'  has been unloaded")                           
                        self.client.unload_extension(extname)

                    else: pass

                except Exception as e: print(e)
    
    # Discord command to load all Extensions
    @commands.command(aliases=['ld'])
    async def load(self, ctx, extension:str):
        if ctx.author.id in data['superids']:
            try:
                if extension == 'all':
                    self.loadCogs()
                    await ctx.send('`All Extensions have been loaded, senpai!`') 

                else: 
                    self.client.load_extension(f'extensions.{extension}')
                    await ctx.send('`The extension has been loaded, senpai!`')
                
            except:
                await ctx.send('`Please provide the extension to load, senpai!`')
        
        else: await ctx.send('`Senpai, only the devs can use this command!`')


    # Discord command to unload all Extensions
    @commands.command(aliases=['uld'])
    async def unload(self, ctx, extension:str):
        if ctx.author.id in data['superids']:
            try:
                if extension == 'all':
                    self.unloadCogs()
                    await ctx.send('`All Extensions have been unloaded, senpai!`') 
     
                else:
                    if extension != 'super':  
                        self.client.unload_extension(f'extensions.{extension}')
                        await ctx.send('`The extension has been unloaded, senpai!`')

                    else:
                        await ctx.send('`Senpai you can\'t unload that!`')

            except:
                await ctx.send('`Please provide the extension to unload, senpai!`')
        
        else: await ctx.send('`Senpai, only the devs can use this command!`')


    # Discord command to reload all Extensions
    @commands.command(aliases=['rld'])
    async def reload(self, ctx, extension:str):
        if ctx.author.id in data['superids']:
            try: 
                if extension == 'all':
                    self.unloadCogs()
                    self.loadCogs()

                    await ctx.send('`All Extensions have been reloaded, senpai!`')

                else: 
                    if extension != 'super':
                        self.client.unload_extension(f'extensions.{extension}')
                        self.client.load_extension(f'extensions.{extension}')
                        await ctx.send('`The extension has been reloaded, senpai!`')

                    else:
                        await ctx.send('`Senpai you can\'t unload that!`')

            except Exception as e:
                await ctx.send('`Please provide the extension to reload, senpai!`')
                print(e)
        
        else: await ctx.send('`Senpai, only the devs can use this command!`')


def setup(client):
    client.add_cog(Super(client))
