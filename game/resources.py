from pyglet import image
from pyglet import window
from os.path import join

def get_center_coordinates(window_width,window_height):
	screen = window.get_platform().get_default_display().get_default_screen()
	x = (screen.width*0.5)-(window_width*0.5)
	y = (screen.height*0.5)-(window_height*0.5)
	return int(x),int(y)

def center_image(image):
	image.anchor_x = int(image.width*0.5)
	image.anchor_y = int(image.height*0.5)
	return image

class Resources:
	state = {'START':1,'PLAYER':2,'GAME':3,'END':4} #game states
	race = {'BLACK':1,'WHITE':2} #player side
	stype = {
			'JONOKUCHI':(1,0),
			'KOMUSUBI':(2,2),
			'SEKIWAKE':(4,3),
			'OZEKI':(7,5),
			'YOKUZANA':(13,10)
			} #sumo constants (weight,energy)

	window_width = 1280
	window_height = 650
	center_x,center_y = get_center_coordinates(window_width,window_height)

	sprites = {}
	res_path = './assets/img'
	sprites['no_sprite'] 			= image.load(join(res_path,'blank.png'))
	sprites['default_cursor'] 		= image.load(join(res_path,'default_cursor.PNG'))
	sprites['active_cursor'] 		= image.load(join(res_path,'active_cursor.PNG'))
	sprites['hand_cursor'] 			= image.load(join(res_path,'hand_cursor.PNG'))
	sprites['play_button']  		= center_image(image.load(join(res_path,'play_button.png')))
	sprites['title_bg'] 			= image.load(join(res_path,'title_bg.png'))
	sprites['player_bg'] 			= center_image(image.load(join(res_path,'player_bg.jpg')))
	sprites['sumo']		    		= center_image(image.load(join(res_path,'sumo_title.gif')))

	sprites['BLACK_JONOKUCHI']		= center_image(image.load(join(res_path,'sumo_title.gif')))
	sprites['KOMUSUBI']				= center_image(image.load(join(res_path,'sumo_title.gif')))
	sprites['SEKIWAKE']				= center_image(image.load(join(res_path,'sumo_title.gif')))
	sprites['OZEKI']				= center_image(image.load(join(res_path,'sumo_title.gif')))
	sprites['YOKUZANA']				= center_image(image.load(join(res_path,'sumo_title.gif')))