from pyglet import image
from pyglet import media
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
			'PROGRAMMING1':6,
			'SWAP1':7,
			'TILE1':8,
			'DELETE1':9,
			'TRANSITION_PLAYER2':10,
			'PLAYER2':11,
			'PROGRAMMING2':12,
			'SWAP2':13,
			'TILE2':14,
			'DELETE2':15,
			'TRANSITION_BOARD':16,
			'BOARD':17,
			'EXECUTE':18,
			'WAIT':19,
			'REPLENISH':20,
			'END':21
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

	special_cards = ['avatar','fat up','hex','jump','kamikaze','reverse','swap']#,'take down']
	special_cards_det = {'AVATAR':(6,"Allied wrestler will become invulnerable to any enemy. This will last until the round ends."),
						 'FAT UP':(3,"Increases weight of an allied wrestler by a random value between [0,5]"),
						 'HEX':(7,"Turns an enemy wrestler into an animal, lowering its weight to 0."),
						 'JUMP':(3,"Allied wrestler jumps and skips one tile within the lane."),
						 'KAMIKAZE':(5, "Allied wrestler commits suicide while also killing all the adjacent enemy wrestlers."),
						 'REVERSE':(4, "Reverses the current direction of any wrestler."),
						 'SWAP':(7,"Swaps an allied wrestler with an enemy wrestler."),
						 'TAKE DOWN':(4,"Disables all the power cards and moves applied to the enemy wrestler.")
						}

	card_priority = {
					'summon':3,
					'move':2,
					'special':1
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
	audio = {}
	sfx_path = './assets/sfx'
	#Sound Effects
	audio['ost']					= media.load(join(sfx_path,'ost.mp3'))

	sprites = {}
	res_path = './assets/img'

	# UI Elements
	sprites['no_sprite'] 			= image.load(join(res_path,'blank.png'))
	sprites['start_button']  		= center_image(image.load(join(res_path,'start_button.png')))
	sprites['play_button']  		= center_image(image.load(join(res_path,'play_button.png')))
	sprites['end_turn_button']		= image.load(join(res_path,'endturn_button.png'))
	sprites['end_turn_button2']		= image.load(join(res_path,'endturn_button_active.png'))
	sprites['program_button']		= image.load(join(res_path,'program_button.png'))
	sprites['program_button2']		= image.load(join(res_path,'program_button_active.png'))
	sprites['return_button']		= image.load(join(res_path,'return_button.png'))
	sprites['return_button2']		= image.load(join(res_path,'return_button_active.png'))
	sprites['title_bg'] 			= image.load(join(res_path,'title_bg.png'))
	sprites['main_bg'] 				= image.load(join(res_path,'main_bg.png'))
	sprites['game_over'] 			= image.load(join(res_path,'game_over.png'))
	sprites['game_board']			= image.load(join(res_path,'game_board.png'))
	sprites['tile']					= image.load(join(res_path,'tile.png'))
	sprites['tile_glow']			= image.load(join(res_path,'tile_glow.png'))
	sprites['hand_board']			= image.load(join(res_path,'hand_board.png'))
	sprites['programming_board'] 	= image.load(join(res_path,'programming_board.png'))
	sprites['programming_board2'] 	= image.load(join(res_path,'programming_board2.png'))
	sprites['terminal'] 			= image.load(join(res_path,'terminal.png'))
	sprites['blocker']				= image.load(join(res_path,'blocker.png'))

	# Ability Cards
	sprites['card_avatar']			= center_image(image.load(join(res_path,'cards/coh_sp-avatar.jpg')))
	sprites['card_fatup']			= center_image(image.load(join(res_path,'cards/coh_sp-fatup.jpg')))
	sprites['card_hex']				= center_image(image.load(join(res_path,'cards/coh_sp-hex.jpg')))
	sprites['card_jump']			= center_image(image.load(join(res_path,'cards/coh_sp-jump.jpg')))
	sprites['card_kamikaze']		= center_image(image.load(join(res_path,'cards/coh_sp-kamikaze.jpg')))
	sprites['card_reverse']			= center_image(image.load(join(res_path,'cards/coh_sp-reverse.jpg')))
	sprites['card_swap']			= center_image(image.load(join(res_path,'cards/coh_sp-swap.jpg')))
	sprites['card_takedown']		= center_image(image.load(join(res_path,'cards/coh_sp-takedown.jpg')))

	# Move Cards
	sprites['card_move_1']			= center_image(image.load(join(res_path,'cards/coh_move-1.jpg')))
	sprites['card_move_2']			= center_image(image.load(join(res_path,'cards/coh_move-2.jpg')))
	sprites['card_move_3']			= center_image(image.load(join(res_path,'cards/coh_move-3.jpg')))
	sprites['card_move_4']			= center_image(image.load(join(res_path,'cards/coh_move-4.jpg')))
	sprites['card_move_5']			= center_image(image.load(join(res_path,'cards/coh_move-5.jpg')))

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
	sprites['wrestler_jonokuchi_blue']	= image.load(join(res_path,'wrestlers/icon_level1-blue.png'))
	sprites['wrestler_komusubi_blue']	= image.load(join(res_path,'wrestlers/icon_level2-blue.png'))
	sprites['wrestler_sekiwake_blue']	= image.load(join(res_path,'wrestlers/icon_level3-blue.png'))
	sprites['wrestler_ozeki_blue']		= image.load(join(res_path,'wrestlers/icon_level4-blue.png'))
	sprites['wrestler_yokuzana_blue']	= image.load(join(res_path,'wrestlers/icon_level5-blue.png'))

	sprites['wrestler_jonokuchi_red']	= image.load(join(res_path,'wrestlers/icon_level1-red.png'))
	sprites['wrestler_komusubi_red']	= image.load(join(res_path,'wrestlers/icon_level2-red.png'))
	sprites['wrestler_sekiwake_red']	= image.load(join(res_path,'wrestlers/icon_level3-red.png'))
	sprites['wrestler_ozeki_red']		= image.load(join(res_path,'wrestlers/icon_level4-red.png'))
	sprites['wrestler_yokuzana_red']	= image.load(join(res_path,'wrestlers/icon_level5-red.png'))


