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
	# game states
	state = {'START':1,
			'PLAYER':2,
			'SETUP':3,
			'TRANSITION_PLAYER1':4,
			'PLAYER1':5,
			'TILE1':6,
			'TRANSITION_PLAYER2':7,
			'PLAYER2':8,
			'TILE2':9,
			'TRANSITION_BOARD':10,
			'BOARD':11,
			'EXECUTE':12,
			'WAIT':13,
			'REPLENISH':14,
			'END':15
			}

	player = {'RED':1,'BLUE':2} # player side
	wrestlers = ['jonokuchi','komusubi','sekiwake','ozeki','yokuzana']
	stype = {
			'JONOKUCHI':(1,1),
			'KOMUSUBI':(2,2),
			'SEKIWAKE':(4,3),
			'OZEKI':(7,6),
			'YOKUZANA':(13,10)
			} # sumo constants (weight,energy)

	card_priority = {
					'summon':3,
					'move':2,
					'card':1
					}

	board_grid = [[(5+i*80,7+j*80) for i in range(8)] for j in range(8)]

	#(x,y) positions for the cards at card_at_hand board
	card_pos1 = [(720,555),(845,555),(970,555),(1095,555),(1220,555),
				 (720,407),(845,407),(970,407),(1095,407),(1220,407)]

	#(x,y) positions for the cards at programming board
	card_pos2 = [(720,230),(845,230),(970,230),(1095,230),(1220,230),
				 (720,82),(845,82),(970,82),(1095,82),(1220,82)]

	window_width = 1300
	window_height = 655

	# 8x8 board
	# board_width = 640
	# board_height = 640 
	
	center_x,center_y = get_center_coordinates(window_width,window_height)

	# Declare all of your assets here #
	sprites = {}
	res_path = './assets/img'

	# UI Elements
	sprites['no_sprite'] 			= image.load(join(res_path,'blank.png'))
	#sprites['default_cursor'] 		= image.load(join(res_path,'default_cursor.PNG'))
	#sprites['active_cursor'] 		= image.load(join(res_path,'active_cursor.PNG'))
	#sprites['hand_cursor'] 		= image.load(join(res_path,'hand_cursor.PNG'))
	sprites['start_button']  		= center_image(image.load(join(res_path,'start_button.png')))
	sprites['play_button']  		= center_image(image.load(join(res_path,'play_button.png')))
	sprites['end_turn_button']		= image.load(join(res_path,'endturn_button.png'))
	sprites['end_turn_button2']		= image.load(join(res_path,'endturn_button_active.png'))
	sprites['title_bg'] 			= image.load(join(res_path,'title_bg.png'))
	sprites['main_bg'] 				= image.load(join(res_path,'main_bg.png'))
	sprites['game_over'] 			= image.load(join(res_path,'game_over.png'))
	sprites['game_board']			= image.load(join(res_path,'game_board.png'))
	sprites['tile']					= image.load(join(res_path,'tile.png'))
	sprites['tile_glow']			= image.load(join(res_path,'tile_glow.png'))
	sprites['programming_board'] 	= image.load(join(res_path,'programming_board.png'))
	sprites['blocker']				= image.load(join(res_path,'blocker.png'))
	# Ability Cards
	sprites['card_avatar']			= center_image(image.load(join(res_path,'cards/avatar.jpg')))
	sprites['card_fatup']			= center_image(image.load(join(res_path,'cards/fatup.jpg')))
	sprites['card_hex']				= center_image(image.load(join(res_path,'cards/hex.jpg')))
	sprites['card_jump']			= center_image(image.load(join(res_path,'cards/jump.jpg')))
	sprites['card_kamikaze']		= center_image(image.load(join(res_path,'cards/kamikaze.jpg')))
	sprites['card_reverse']			= center_image(image.load(join(res_path,'cards/reverse.jpg')))
	sprites['card_swap']			= center_image(image.load(join(res_path,'cards/swap.jpg')))
	sprites['card_takedown']		= center_image(image.load(join(res_path,'cards/takedown.jpg')))
	sprites['card_move']			= center_image(image.load(join(res_path,'cards/move.jpg')))

	# Wrestler Cards
	sprites['card_jonokuchi']		= center_image(image.load(join(res_path,'cards/coh_level1-blue.jpg')))
	sprites['card_komusubi']		= center_image(image.load(join(res_path,'cards/coh_level2-blue.jpg')))
	sprites['card_sekiwake']		= center_image(image.load(join(res_path,'cards/coh_level3-blue.jpg')))
	sprites['card_ozeki']			= center_image(image.load(join(res_path,'cards/coh_level4-blue.jpg')))
	sprites['card_yokuzana']		= center_image(image.load(join(res_path,'cards/coh_level5-blue.jpg')))

	sprites['card_jonokuchi_red']		= center_image(image.load(join(res_path,'cards/coh_level1-red.jpg')))
	sprites['card_komusubi_red']		= center_image(image.load(join(res_path,'cards/coh_level2-red.jpg')))
	sprites['card_sekiwake_red']		= center_image(image.load(join(res_path,'cards/coh_level3-red.jpg')))
	sprites['card_ozeki_red']			= center_image(image.load(join(res_path,'cards/coh_level4-red.jpg')))
	sprites['card_yokuzana_red']		= center_image(image.load(join(res_path,'cards/coh_level5-red.jpg')))

	# Wrestler Sprites
	sprites['wrestler_jonokuchi_blue']	= image.load(join(res_path,'wrestlers/sumo-blue.png'))
	sprites['wrestler_komusubi_blue']	= image.load(join(res_path,'wrestlers/sumo-blue.png'))
	sprites['wrestler_sekiwake_blue']	= image.load(join(res_path,'wrestlers/sumo-blue.png'))
	sprites['wrestler_ozeki_blue']		= image.load(join(res_path,'wrestlers/sumo-blue.png'))
	sprites['wrestler_yokuzana_blue']	= image.load(join(res_path,'wrestlers/sumo-blue.png'))

	sprites['wrestler_jonokuchi_red']	= image.load(join(res_path,'wrestlers/sumo-red.png'))
	sprites['wrestler_komusubi_red']	= image.load(join(res_path,'wrestlers/sumo-red.png'))
	sprites['wrestler_sekiwake_red']	= image.load(join(res_path,'wrestlers/sumo-red.png'))
	sprites['wrestler_ozeki_red']		= image.load(join(res_path,'wrestlers/sumo-red.png'))
	sprites['wrestler_yokuzana_red']	= image.load(join(res_path,'wrestlers/sumo-red.png'))





