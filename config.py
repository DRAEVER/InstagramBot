import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
You can Download almost anything From your Instagram Account.

<b>What Can Be Downloaded?:</b>

• All posts of any Profile. (Both Public and Private,for private profiles you need to be a follower.)
• Stories of any profile (Both Public and Private,for private profiles you need to be a follower.)
• DP of any profile (No need to follow)
• IGTV videos.
• Highlights from any profiles.
• Any Public Post from Link(Post/Reels/IGTV)


<b>How to Download:</b>

Its Easy!!
You Need to login into your account by /login. 

You have two Options:

1. From Username:
Just send any instagram username.

For Example:
<code>itz_.programmer</code>

2. From URL:

You can also sent a post link to download the post or video.

For Example:
<code>https://www.instagram.com/p/CL4QbUiLRNW/?utm_medium=copy_link</code>
<code>https://www.instagram.com/taylorswift/p/CWds7zapgHn/?utm_medium=copy_link</code>


<b>Available Commands and Usage</b>

/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/login - Login into your account.
/logout - Logout of your account.
/account - Shows the details of logged in account.

/posts <username> - Download posts of any username. Use /posts to download own posts or <code> /posts <username> </code>for others.
Example : <code>/posts samantharuthprabhuoffl</code>

/igtv <username> - Download IGTV videos from given username. If no username given, downloads your IGTV.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Example: <code>/saved 10</code> to download latest 10 saved posts.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/highlights <username> - Downloads highlights from given username, If nothing given your highlights will be downloaded.


"""
    HOME_TEXT = """
<b>Helo, [{}](tg://user?id={})
I am Personal Bot only for someUsers.
This is paid bot.

© @Alone_loverboy
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
I am your assistant to manage your Instagram account.

Use /help to know what I can do for you.</b>
"""

