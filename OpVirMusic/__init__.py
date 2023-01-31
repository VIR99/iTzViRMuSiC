from OpVirMusic.core.bot import OpVirMusicBot
from OpVirMusic.core.dir import dirr
from OpVirMusic.core.git import git
from OpVirMusic.core.userbot import Userbot
from OpVirMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = OpVirMusicBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
