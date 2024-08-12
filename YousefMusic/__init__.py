
from YousefMusic.core.bot import Zelzaly
from YousefMusic.core.dir import dirr
from YousefMusic.core.git import git
from YousefMusic.core.userbot import Userbot
from YousefMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
dbb()
git()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
YTB = YTM()
