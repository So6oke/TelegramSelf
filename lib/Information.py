from .library import *

admin_user_id = 7522524886 #<--- آیدی ادمین
api_id = 28276540 #<--- آی پی آی آیدی
api_hash = '79256a6149566f43430e2f48833a5322' #<--- ای پی آی هش
helper_username = 'Controllermmdbot' #<--- یوزر ربات هلپر بدون @
bot_token = '8321960548:AAHL9qrSxJBi19wzSQzww_hrQ7dDOmeAeLQ' #<--- توکن ربات هلپر

client_id = '01e7dc6b41c3471b94efe87abeb05919'
client_secret = '4f5f93af1ced4b0d9ba8440606803639'

client = TelegramClient('TRself-MT', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
