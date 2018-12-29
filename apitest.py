import urllib.request
import re
import ui
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from objc_util import *


#spotify api
client_id = 'f3c388352fac463e9b16f2bc8d004a22'
client_secret = '19ac8b2c9b294058b432b9e5e5f33cf7'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'


#spotify 検索
def search(sender):
	out = sender.superview['textfield1'].text	
	
	if len(sys.argv) > 1:
	    name = ' '.join(sys.argv[1:])
	else:
	    name = out
	#アーティスト情報取得
	results = spotify.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
		global artist
		artist = items[0]	
	#画像画面
	UIScreen = ObjCClass('UIScreen')
	view = ui.View()
	view.name = 'アーティスト'
	view.size_to_fit()
	imageView = ui.ImageView()
	#画像の取得とサイズ
	def load_image(): 
		
		try:
			imageView.load_from_url(artist['images'][0]['url'])
		except:
			
			imageView.load_from_url('https://dl.dropboxusercontent.com/s/jf9vinaojo6n2by/%E5%86%99%E7%9C%9F%202018-12-28%2010%2010%2027.png')
			error = 'spotifyではみつかりませんでした。'
			print(error)

	
		
	imageView.flex = 'WH'
	imageView.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
	#とじるボタン
	def button_tapped(sender):
		view.close()
	button = ui.Button(title='[とじる]')
	button.flex = 'TRL'
	button.center = (view.width * 0.5, view.height * 0.5)
	button.action = button_tapped
	#delayしないと動かなくなる
	view.add_subview(imageView)
	view.add_subview(button)
	view.present(style='full_screen', hide_title_bar=True, orientations=('portrait',))
	ui.delay(load_image,0.5)

v = ui.load_view()
v.present('sheet')

