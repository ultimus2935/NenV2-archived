from discord.ext import commands
import json

data = json.load(open('data.json', 'r'))

class helpText(commands.Cog):
    def __init__(self, client):
        self.client = client


    main_title = "General Help"
    mainhelp = f"""
**Please use `n.help [category]` for more information**

**`n.nen`: Default Command**

**Categories:**
**`Doujin Info/Search:`** `n.help doujin`
**`Read Doujins:`** `n.help read`
**`Miscalleneous:`** `n.help misc`
**`Reddit Commands:`** `n.help reddit`

**[Join the official server for support and updates]({data["support"]})**
    ```
Doujin covers/images maybe swapped out for images   
saying "NSFW" if you are not in an NSFW or one of 
the Pseudo-NSFW channels (custom made for the bot)
    
Please use the command in an NSFW or Pseudo-NSFW  
channel to be able to see the images 
    ```
    **```
Nen is currently under development
If you find any issues, or have suggestions,
please feel free to join the official server
    ```**
*all doujins and their respective information is provided by [nhentai.net](https://nhentai.net)*
    """ # not indent mistake its meant to be that way


    doujin_title = "Get information about doujins"
    doujinhelp = """
`n.info [code]`: **Provides you full information on the doujin**
`n.tags [code]`: **Provides the tags associated with the doujin**

`n.random`: **Provides a random existent doujin**

`n.search "[query]" [optional: page number upto 10]`: 
**Allows you to search for doujin based upon query**
    """

    read_title = "Read Doujins on discord"
    readhelp = """
**Nen's Special Feature!!**

`n.read [code]`: 
Special feature of Nen where you can read
any doujin of you choice on discord itself

It has special embeds and reaction controls
to make your reading experience as enjoyable
and easy as possible

The function of the reaction controls are as follows:
**Jump to first page:** ⏮️
**Previous page:** ◀️
**Next page:** ▶️
**Jump to last page:** ⏭️
**Delete embed:** ⏹️
    """

    misc_title = "Miscalleneous"
    mischelp = """
`n.invite`: **Invite Nen into any server you want**
`n.vote`: **Vote for Nen so that we can top the charts!**
`n.embed "[title]" "[description]"`: **Create custom embeds on the flow**
    """

    # Reddit Commands are currently disabled 
    reddit_title = "Reddit Commands"
    reddithelp = """
***REDDIT COMMANDS ARE CURRENTLY DISABLED DUE TO ISSUES WITH THE API***

`n.hentai`: **Displays random post from r/hentai**
    """

def setup(client):
    client.add_cog(helpText(client))