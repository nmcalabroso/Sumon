import pyglet
from game.world import GameWorld
from game.board import GameBoard
from game.resources import Resources
from game.gui import Button
from game.gui import TextWidget
from game.gui import Background
from game.player import Player
from game.gui import MyRectangle

game_window = pyglet.window.Window(Resources.window_width, Resources.window_height)
game_window.set_caption("SUMOn")
game_window.set_location(Resources.center_x,Resources.center_y)
fps = pyglet.clock.ClockDisplay()

# Object Batches per state #
start_batch = pyglet.graphics.Batch()
player_batch = pyglet.graphics.Batch()
game_batch = pyglet.graphics.Batch()
end_batch = pyglet.graphics.Batch()
# End of Batches

world = GameWorld() #instantiate the main world
my_bg = Background(
				name = 'my_bg',
				img =  Resources.sprites['title_bg'],
				)

@game_window.event
def on_draw():
	game_window.clear()
	my_bg.draw()
	if world.game_state == Resources.state['START']:
		start_batch.draw()
	elif world.game_state == Resources.state['PLAYER']:
		player_batch.draw()
	elif world.game_state == Resources.state['END']:
		end_batch.draw()
	else:
		game_batch.draw()
	fps.draw()

def update(dt):
	for obj in world.get_game_objects():
		obj.update(dt)

	for widget in world.get_widgets():
		widget.update(dt)


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

	# End of Instantiation #

	# Handler specification #
	game_window.push_handlers(start_button)
	# End of specification #

	# Importation section #
	world.add_widget(start_button)
	# End of importation #

def player_screen():
	x1 = int((Resources.window_width*0.5)-200)
	y1 = int((Resources.window_height*0.5)+50)

	input_p1 = pyglet.text.Label(
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
						world = world,
						name = 'text_p1')
	
	input_p2 = pyglet.text.Label(
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
						world = world,
						name = 'text_p2')

	play_button = Button(
					name = 'play_button',
					curr_state = 'PLAYER',
					target_state = 'GAME',
					world = world,
					img = Resources.sprites['play_button'],
				   	x = Resources.window_width * 0.5,
					y = y1-115,
				   	batch = player_batch)

	# Handler specification #
	game_window.push_handlers(play_button)
	game_window.push_handlers(text_p1)
	game_window.push_handlers(text_p2)
	# End of specification #

	# Importation section #
	world.add_label(input_p1)
	world.add_label(input_p2)
	world.add_widget(text_p1)
	world.add_widget(text_p2)
	world.add_widget(play_button)
	# End of importation #

def game_screen():
	# Declaration Section #
	prog_board_p1 = MyRectangle(name = 'p1_board',curr_state = "GAME", x = 650, y = 330, img = Resources.sprites['programming_board'],batch = game_batch)
	prog_board_p2 = MyRectangle(name = 'p2_board',curr_state = "GAME", x = 650, y = 5, img = Resources.sprites['programming_board'],batch = game_batch)
	
	player1 = Player(
				actual_name = 'Player',
				name = 'Player1',
				img = Resources.sprites['no_sprite'],
				x = (Resources.window_width*0.5) - 150,
				y = Resources.window_height*0.5,
				batch = game_batch)


	label_p1 =  pyglet.text.Label(
								text = 'Player1: ',
								x = prog_board_p1.x+2,
								y = prog_board_p1.y+prog_board_p1.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	lives_label_p1 =  pyglet.text.Label(
								text = 'Lives: ',
								x = prog_board_p1.x+prog_board_p1.width-150+2,
								y = prog_board_p1.y+prog_board_p1.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	lives_p1 =  pyglet.text.Label(
								text = player1.get_life_label(),
								x = prog_board_p1.x+prog_board_p1.width-100+2,
								y = prog_board_p1.y+prog_board_p1.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	mana_label_p1 =  pyglet.text.Label(
								text = 'Mana: ',
								x = prog_board_p1.x+prog_board_p1.width-80+2,
								y = prog_board_p1.y+prog_board_p1.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	mana_p1 =  pyglet.text.Label(
								text = player1.get_mana_label(),
								x = prog_board_p1.x+prog_board_p1.width-30+2,
								y = prog_board_p1.y+prog_board_p1.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	player2 = Player(
				actual_name = 'Player',
				name = 'Player2',
				img = Resources.sprites['no_sprite'],
				x = Resources.window_width*0.5+100,
				y = Resources.window_height*0.5,
				batch = game_batch)

	label_p2 =  pyglet.text.Label(
								text = 'Player2: ',
								x = prog_board_p2.x+2,
								y = prog_board_p2.y+prog_board_p2.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	lives_label_p2 =  pyglet.text.Label(
								text = 'Lives: ',
								x = prog_board_p2.x+prog_board_p2.width-150+2,
								y = prog_board_p2.y+prog_board_p2.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	lives_p2 =  pyglet.text.Label(
								text = player2.get_life_label(),
								x = prog_board_p2.x+prog_board_p2.width-100+2,
								y = prog_board_p2.y+prog_board_p2.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	mana_label_p2 =  pyglet.text.Label(
								text = 'Mana: ',
								x = prog_board_p2.x+prog_board_p2.width-80+2,
								y = prog_board_p2.y+prog_board_p2.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	mana_p2 =  pyglet.text.Label(
								text = player2.get_mana_label(),
								x = prog_board_p2.x+prog_board_p2.width-30+2,
								y = prog_board_p2.y+prog_board_p2.height-2,
								anchor_y = 'top',
                              	color = (57, 255, 20, 255),
                              	batch = game_batch)

	game_board = GameBoard(name = 'game_board',x = 5,y = 5, img = Resources.sprites['game_board'],batch = game_batch)
	# End of Declaration #

	# Handler specification #
	game_window.push_handlers(player1)
	game_window.push_handlers(player2)
	game_window.push_handlers(game_board)
	# End of specification #

	# Importation section #
	world.add_game_object(game_board)

	world.add_game_object(prog_board_p1)
	world.add_game_object(prog_board_p2)

	world.add_game_object(player1)
	world.add_label(label_p1)
	world.add_label(lives_p1)
	world.add_label(lives_label_p1)
	world.add_label(mana_label_p1)
	world.add_label(mana_p1)

	world.add_game_object(player2)
	world.add_label(label_p2)
	world.add_label(lives_label_p2)
	world.add_label(lives_p2)
	world.add_label(mana_label_p2)
	world.add_label(mana_p2)
	# End of importation #

def end_screen():
	pass
#--- MAIN ----------------------------------------------------------------------------------------------------------------

def main():
	world.set_window(game_window)
	world.add_widget(my_bg)
	title_screen()
	player_screen()
	game_screen()
	#end_screen()
	game_window.push_handlers(world)

	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.clock.set_fps_limit(120)
	pyglet.app.run()

if __name__ == '__main__':
	main()