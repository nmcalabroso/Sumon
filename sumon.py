import pyglet
from pyglet.media import Player as MediaPlayer
from pyglet.graphics import OrderedGroup
from game.resources import Resources
from game.world import GameWorld
from game.board import GameBoard
from game.gui import Button
from game.gui import TextWidget
from game.gui import Background
from game.gui import UILabel
from game.gui import MyRectangle
from game.gui import EndTurnButton
from game.gui import ProgramButton
from game.gui import ReturnButton
from game.gui import Terminal
from game.player import Player

game_window = pyglet.window.Window(Resources.window_width, Resources.window_height)
game_window.set_caption("SUMOn")
game_window.set_location(Resources.center_x,Resources.center_y)
game_window.set_vsync(True)

# Object Batches per state #
start_batch = pyglet.graphics.Batch()
player_batch = pyglet.graphics.Batch()
game_batch = pyglet.graphics.Batch()
programming_batch = pyglet.graphics.Batch()
text_batch_1 = pyglet.graphics.Batch()
text_batch_2 = pyglet.graphics.Batch()
end_batch = pyglet.graphics.Batch()
# End of Batches

world = GameWorld() #instantiate the main world
my_bg_1 = Background(name = 'my_bg_1',img =  Resources.sprites['title_bg_1'],x = 0,y = 0)
my_bg_2 = Background(name = 'my_bg_2',img =  Resources.sprites['title_bg_2'],x = my_bg_1.width,y=0)
mp = MediaPlayer()

@game_window.event
def on_draw():
	game_window.clear()
	my_bg_1.draw()
	my_bg_2.draw()
	if world.game_state == Resources.state['START']:
		start_batch.draw()
	elif world.game_state == Resources.state['PLAYER']:
		player_batch.draw()
	elif world.game_state == Resources.state['END']:
		end_batch.draw()
	else:
		game_batch.draw()
		if world.game_state == Resources.state['PROGRAMMING1'] or world.game_state == Resources.state['PROGRAMMING2']:
			programming_batch.draw()
			if world.game_state == Resources.state['PROGRAMMING1']:
				text_batch_1.draw()
			else:
				text_batch_2.draw()

		for obj in world.get_game_objects():
			obj.draw()
			if obj.name == "Player1" or obj.name == "Player2":
				for card in obj.cards:
					game_window.push_handlers(card)
					card.draw()
			elif obj.name == "game_board":
				for i in range(len(obj.my_grid)):
					for j in range(len(obj.my_grid[i])):
						obj.my_grid[i][j].draw()
						if obj.my_grid[i][j].wrestler != None:
							obj.my_grid[i][j].wrestler.draw()

						if obj.my_grid[i][j].glow is True:
							g = world.find_widget('glow')
							g.set_position(obj.my_grid[i][j].x,obj.my_grid[i][j].y)
							g.draw()

		if world.game_state == Resources.state['TILE1'] or world.game_state == Resources.state['TILE2']:
			b = world.find_widget('blocker')
			b.draw()

def update(dt):
	world.update(dt)
#--- STATES ----------------------------------------------------------------------------------------------------------------

def title_screen():
	mp.queue(Resources.audio['title_bgm'])
	start_button = Button(
						name = 'start_button',
						curr_state = 'START',
						target_state = 'PLAYER',
						world = world,
						img = Resources.sprites['start_button'],
						x = Resources.window_width*0.5,
						y = Resources.window_height*0.5-125,
						batch = start_batch)
	game_window.push_handlers(start_button)
	world.add_widget(start_button)

def player_screen():
	x1 = int((Resources.window_width*0.5)-200)
	y1 = int((Resources.window_height*0.5 - 80))

	input_p1 = pyglet.text.Label('Player 1:',
						x = x1,
						y = y1,
						anchor_y = 'bottom',
	                  	color = (57, 255, 20, 255),
	                  	batch = player_batch)

	text_p1 = TextWidget(text = '',
						x = x1+75,
						y = y1,
						width = 250,
						batch = player_batch,
						cursor = game_window.get_system_mouse_cursor('text'),
						curr_state = 'PLAYER',
						world = world,
						name = 'text_p1')
	
	input_p2 = pyglet.text.Label('Player 2:',
								x = x1,
								y = y1-50,
								anchor_y = 'bottom',
			                  	color = (57, 255, 20, 255),
			                  	batch = player_batch)

	text_p2 = TextWidget(text = '',
						x = x1+75,
						y = y1-50,
						width = 250,
						batch = player_batch,
						cursor = game_window.get_system_mouse_cursor('text'),
						curr_state = 'PLAYER',
						world = world,
						name = 'text_p2')

	play_button = Button(name = 'play_button',
						curr_state = 'PLAYER',
						target_state = 'SETUP',
						world = world,
						img = Resources.sprites['play_button'],
					   	x = Resources.window_width * 0.5,
						y = y1-90,
					   	batch = player_batch)

	game_window.push_handlers(play_button)
	game_window.push_handlers(text_p1)
	game_window.push_handlers(text_p2)

	world.add_label(input_p1)
	world.add_label(input_p2)
	world.add_widget(text_p1)
	world.add_widget(text_p2)
	world.add_widget(play_button)

def game_screen():
	background = OrderedGroup(0)
	foreground = OrderedGroup(1)

	mp.queue(Resources.audio['game_bgm'])

	hand_board = MyRectangle(name = 'hand_board',
							curr_state = "GAME",
							opacity = 255,
							x = 650,
							y = 330,
							img = Resources.sprites['hand_board'],
							batch = game_batch,
							group = background)

	prog_board = MyRectangle(name = 'prog_board',
							curr_state = "GAME",
							opacity = 255,
							x = 650,
							y = 5,
							img = Resources.sprites['programming_board'],
							batch = game_batch,
							group = background)

	player1 = Player(actual_name = 'Player',
					name = 'Player1',
					img = Resources.sprites['no_sprite'],
					x = (Resources.window_width*0.5) - 150,
					y = Resources.window_height*0.5)
	
	player2 = Player(actual_name = 'Player',
					name = 'Player2',
					img = Resources.sprites['no_sprite'],
					x = Resources.window_width*0.5+100,
					y = Resources.window_height*0.5)

	label_player =  UILabel(name = 'player',
							text = 'Player2:',
							x = hand_board.x+9,
							y = hand_board.y+hand_board.height-2,
							anchor_y = 'top',
                          	color = (57, 255, 20, 255),
                          	batch = game_batch,
                          	group = foreground)

	player_name = UILabel(name = 'player_name',
						text = player1.name,
						x = hand_board.x + 75,
						y = label_player.y,
						anchor_y = 'top',
						color = (57,255,20,255),
						batch = game_batch,
						group = foreground)

	label_hand_card = UILabel(name = 'label_hand_card',
						text = 'Card at Hand',
						x = hand_board.x + (hand_board.x/2) - 55,
						y = label_player.y,
						anchor_y = 'top',
						color = (57,255,20,255),
						batch = game_batch,
						group = foreground)

	label_prog_card = UILabel(name = 'label_prog_card',
						text = 'Programming Board',
						x = hand_board.x + (hand_board.x/2) - 80,
						y = prog_board.y+prog_board.height,
						anchor_y = 'top',
						color = (57,255,20,255),
						batch = game_batch,
						group = foreground)

	label_lives =  UILabel(name = 'label_lives',
						text = 'Lives: ',
						x = hand_board.x+hand_board.width-170,
						y = hand_board.y+hand_board.height-2,
						anchor_y = 'top',
                  		color = (57, 255, 20, 255),
                  		batch = game_batch,
                  		group = foreground)

	lives =  UILabel(name = 'lives',
					text = player1.get_life_label(),
					x = label_lives.x+55,
					y = label_lives.y,
					anchor_y = 'top',
                  	color = (57, 255, 20, 255),
                  	batch = game_batch,
                  	group = foreground)

	label_mana =  UILabel(name = 'label_mana',
						text = 'Mana: ',
						x = hand_board.x+hand_board.width-80+2,
						y = hand_board.y+hand_board.height-2,
						anchor_y = 'top',
                      	color = (57, 255, 20, 255),
                      	batch = game_batch,
                      	group = foreground)

	mana =  UILabel(name = 'mana',
					text = player1.get_mana_label(),
					x = hand_board.x+hand_board.width-30+2,
					y = hand_board.y+hand_board.height-2,
					anchor_y = 'top',
                  	color = (57, 255, 20, 255),
                  	batch = game_batch,
                  	group = foreground)

	end_turn_button = EndTurnButton(name = 'end_turn_button',
									curr_state = 'PLAYER1',
									world = world,
									img = Resources.sprites['end_turn_button'],
					   				x = mana.x - 46,
									y = label_prog_card.y - 20,
					   				batch = game_batch,
					   				group = foreground)

	program_button = ProgramButton(name = 'program_button',
								curr_state = 'PLAYER1',
								world = world,
								img = Resources.sprites['program_button'],
								x = prog_board.x+9,
								y = end_turn_button.y,
								batch = game_batch,
								group = foreground)

	game_board = GameBoard(name = 'game_board',
						world = world,
						x = 5,
						y = 7,
						img = Resources.sprites['game_board'])

	blocker = MyRectangle(name = 'blocker',
						curr_state = "GAME",
						opacity = 200,
						x = 650,
						y = 5,
						img = Resources.sprites['blocker'])

	glow = MyRectangle(name = 'glow',
					curr_state = "GAME",
					opacity = 255,
					x = 0,
					y = 0,
					img = Resources.sprites['tile_glow'])
	
	glow.image.anchor_x += 20
	glow.image.anchor_y += 20

	#for manual programming
	terminal = Terminal(name = 'terminal',
						curr_state = 'PLAYER1',
						world = world,
						img = Resources.sprites['terminal'],
						x = prog_board.x + 20,
						y = prog_board.y + 109,
						batch = programming_batch)

	line_widget_1 = TextWidget(name = 'line_widget_1',
						text = '',
						x = terminal.x - 7,
						y = terminal.y - 35,
						width = 500,
						cursor = game_window.get_system_mouse_cursor('text'),
						curr_state = 'PROGRAMMING1',
						world = world,
						batch = text_batch_1)

	line_widget_2 = TextWidget(name = 'line_widget_2',
						text = '',
						x = terminal.x - 7,
						y = terminal.y - 35,
						width = 500,
						cursor = game_window.get_system_mouse_cursor('text'),
						curr_state = 'PROGRAMMING2',
						world = world,
						batch = text_batch_2)

	return_button = ReturnButton(name = 'return_button',
								curr_state = 'PLAYER1',
								world = world,
								img = Resources.sprites['return_button'],
								x = line_widget_1.x+500+13,
								y = line_widget_1.y - 3,
								batch = programming_batch)

	game_window.push_handlers(player1)
	game_window.push_handlers(player2)
	game_window.push_handlers(game_board)
	game_window.push_handlers(end_turn_button)
	game_window.push_handlers(program_button)
	game_window.push_handlers(line_widget_1)
	game_window.push_handlers(line_widget_2)
	game_window.push_handlers(return_button)
	
	world.add_game_object(game_board)
	world.add_widget(blocker)
	world.add_widget(glow)
	world.add_widget(end_turn_button)
	world.add_widget(program_button)
	world.add_widget(terminal)
	world.add_widget(line_widget_1)
	world.add_widget(line_widget_2)
	world.add_widget(return_button)
	world.add_widget(world)
	world.add_widget(hand_board)
	world.add_widget(prog_board)

	world.add_game_object(player1)
	world.add_game_object(player2)
	
	world.add_label(label_player)
	world.add_label(player_name)
	world.add_label(label_hand_card)
	world.add_label(label_prog_card)
	world.add_label(label_lives)
	world.add_label(lives)
	world.add_label(label_mana)
	world.add_label(mana)

def end_screen():
	game_over = MyRectangle(name = 'game_over_logo',
						curr_state = "END",
						opacity = 255,
						x = 650-428,
						y = 290,
						img = Resources.sprites['game_over'],
						batch = end_batch)
	
	player_end =  UILabel(name = 'player_end',
						text = 'PLAYERX WINS!',
						x = game_over.x + game_over.width/3 + 55,
						y = game_over.y - 35,
						anchor_y = 'top',
                  		color = (57, 255, 20, 255),
                  		bold = True,
                  		font_size = 15.0,
                  		batch = end_batch)

	label_mana =  UILabel(name = 'label_mana_end',
						text = 'MANA LEFT:',
						x = player_end.x,
						y = player_end.y - 20,
						anchor_y = 'top',
                  		color = (57, 255, 20, 255),
                  		batch = end_batch)

	mana =  UILabel(name = 'mana_end',
						text = '6969',
						x = label_mana.x + 105,
						y = label_mana.y,
						anchor_y = 'top',
                  		color = (57, 255, 20, 255),
                  		batch = end_batch)

	label_rounds =  UILabel(name = 'label_rounds_end',
						text = 'ROUNDS:',
						x = label_mana.x,
						y = label_mana.y - 20,
						anchor_y = 'top',
                  		color = (57, 255, 20, 255),
                  		batch = end_batch)

	rounds =  UILabel(name = 'rounds_end',
						text = '6969',
						x = mana.x,
						y = label_rounds.y,
						anchor_y = 'top',
                  		color = (57, 255, 20, 255),
                  		batch = end_batch)

	world.add_widget(game_over)
	world.add_label(player_end)
	world.add_label(label_mana)
	world.add_label(mana)
	world.add_label(label_rounds)
	world.add_label(rounds)

#--- MAIN ----------------------------------------------------------------------------------------------------------------

def main():
	world.set_window(game_window)
	world.set_media_player(mp)
	world.add_widget(my_bg_1)
	world.add_widget(my_bg_2)

	title_screen()
	player_screen()
	game_screen()
	end_screen()

	game_window.push_handlers(world)
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.clock.set_fps_limit(120)
	pyglet.app.run()

if __name__ == '__main__':
	main()