import pyglet
from game.world import GameWorld
from game.resources import Resources
from game.gui import Button
from game.gui import PlayerButton
from game.gui import TextWidget
from game.background import Background
from game.player import Player

game_window = pyglet.window.Window(Resources.window_width, Resources.window_height)
game_window.set_caption("SUMOn")
game_window.set_location(Resources.center_x,Resources.center_y)

# Object Batches per state #
start_batch = pyglet.graphics.Batch()
player_batch = pyglet.graphics.Batch()
game_batch = pyglet.graphics.Batch()
end_batch = pyglet.graphics.Batch()
# End of Batches

world = GameWorld() #instantiate the main world

@game_window.event
def on_draw():
	game_window.clear()
	if world.game_state == Resources.state['START']:
		start_batch.draw()
	elif world.game_state == Resources.state['PLAYER']:
		player_batch.draw()
	elif world.game_state == Resources.state['END']:
		end_batch.draw()
	else:
		game_batch.draw()

def update(dt):
	for obj in world.get_game_objects():
		obj.update(dt)

#--- STATES ----------------------------------------------------------------------------------------------------------------
def title_screen():
	# Instantiation section #
	start_button = Button(
						name = 'start_button',
						curr_state = 'START',
						target_state = 'PLAYER',
						world = world,
						img = Resources.sprites['start_button'],
						x = Resources.window_width*0.5,
						y = Resources.window_height*0.5,
						batch = start_batch)

	title_bg 	= Background(
							name = 'title_bg',
							img =  Resources.sprites['title_bg'],
							batch = start_batch)

	# End of Instantiation #

	# Handler specification #
	game_window.push_handlers(start_button)
	# End of specification #

	# Importation section #
	world.add_object(title_bg)
	world.add_object(start_button)
	# End of importation #

def player_screen():
	x1 = int((Resources.window_width*0.5)-200)
	y1 = int((Resources.window_height*0.5)+50)

	label_p1 =  pyglet.text.Label(
								'Player 1:',
								x = x1,
								y = y1,
								anchor_y = 'bottom',
                              	color = (57, 255, 20, 255),
                              	batch = player_batch)
	text_p1 = TextWidget(
						text = '',
						x = x1+75,
						y = y1,
						width = 250,
						batch = player_batch,
						cursor = game_window.get_system_mouse_cursor('text'),
						curr_state = 'PLAYER',
						world = world)
	
	label_p2 =  pyglet.text.Label(
								'Player 2:',
								x = x1,
								y = y1-50,
								anchor_y = 'bottom',
                              	color = (57, 255, 20, 255),
                              	batch = player_batch)

	text_p2 = TextWidget(
						text = '',
						x = x1+75,
						y = y1-50,
						width = 250,
						batch = player_batch,
						cursor = game_window.get_system_mouse_cursor('text'),
						curr_state = 'PLAYER',
						world = world)

	play_button = PlayerButton(
						name = 'play_button',
						curr_state = 'PLAYER',
						target_state = 'GAME',
						world = world,
						img = Resources.sprites['play_button'],
					   	x = Resources.window_width * 0.5,
						y = y1-115,
					   	batch = player_batch)
	

	player_bg = Background(
						name = 'player_bg',
						img =  Resources.sprites['player_bg'],
						batch = player_batch)

	# Handler specification #
	game_window.push_handlers(text_p1)
	game_window.push_handlers(text_p2)
	game_window.push_handlers(play_button)
	
	# End of specification #

	# Importation section #
	world.add_object(player_bg)
	world.add_object(play_button)
	world.add_widget(text_p1)
	world.add_widget(text_p2)
	# End of importation #

def game_screen():

	player1 = Player(
				actual_name = 'Player',
				name = 'Player1',
				img = Resources.sprites['player1_avatar'],
				x = (Resources.window_width*0.5) - 150,
				y = Resources.window_height*0.5,
				batch = game_batch)

	label_p1 =  pyglet.text.Label(
								'Player1: ',
								x = Resources.window_width*0.5 - 220,
								y = Resources.window_height*0.5 + 185,
								anchor_y = 'bottom',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	player2 = Player(
				actual_name = 'Player',
				name = 'Player2',
				img = Resources.sprites['player2_avatar'],
				x = Resources.window_width*0.5+100,
				y = Resources.window_height*0.5,
				batch = game_batch)

	label_p2 =  pyglet.text.Label(
								'Player2: ',
								x = Resources.window_width*0.5 + 20,
								y = Resources.window_height*0.5 + 185,
								anchor_y = 'bottom',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)
	game_bg = Background(
						name = 'player_bg',
						img =  Resources.sprites['player_bg'],
						batch = game_batch)

	# Handler specification #
	game_window.push_handlers(player1)
	game_window.push_handlers(player2)
	# End of specification #

	# Importation section #
	world.add_object(game_bg)
	world.add_object(player1)
	world.add_object(player2)
	world.add_label(label_p1)
	world.add_label(label_p2)
	# End of importation #

def end_screen():
	pass
#--- MAIN ----------------------------------------------------------------------------------------------------------------

def main():
	world.set_window(game_window)
	game_window.push_handlers(world)

	title_screen()
	player_screen()
	game_screen()
	#end_screen()

	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()

if __name__ == '__main__':
	main()