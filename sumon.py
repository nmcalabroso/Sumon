import pyglet
from game.world import GameWorld
from game.resources import Resources
from game.gui import StartButton
from game.gui import TextWidget
from game.background import Background
#from game.sumo import SumoWrestler

game_window = pyglet.window.Window(Resources.window_width, Resources.window_height)
game_window.set_caption("My Game")
game_window.set_location(Resources.center_x,Resources.center_y)

document = pyglet.text.document.FormattedDocument()
layout = pyglet.text.layout.IncrementalTextLayout(document, 800, 500)
caret = pyglet.text.caret.Caret(layout)
game_window.push_handlers(caret)

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
		for obj in world.get_game_objects():
			obj.draw()

def update(dt):
	for obj in world.get_game_objects():
		obj.update(dt)

#--- STATES ----------------------------------------------------------------------------------------------------------------
def title_screen():
	# Instantiation section #
	title_bg 	= Background('title_bg',
							img =  Resources.sprites['title_bg'],
							batch = start_batch)

	play_button = StartButton(world = world,
							img = Resources.sprites['play_button'],
						   	x = Resources.window_width*0.5,
						   	y = Resources.window_height*0.5,
						   	batch = start_batch)
	# End of Instantiation #

	# Handler specification #
	game_window.push_handlers(play_button)
	# End of specification #

	# Importation section #
	world.add_object(title_bg)

	# End of importation #

def player_screen():
	x1 = int((Resources.window_width*0.5)-200)
	y1 = int((Resources.window_height*0.5)+50)

	player_bg = Background('player_bg',
						img =  Resources.sprites['player_bg'],
						batch = player_batch)

	label_p1 =  pyglet.text.Label('Player 1:',
								x = x1,
								y = y1,
								anchor_y='bottom',
                              	color=(57, 255, 20, 255),
                              	batch=player_batch)

	text_p1 = TextWidget(text = '',
						x = x1+75,
						y = y1,
						width = 250,
						batch = player_batch,
						cursor = game_window.get_system_mouse_cursor('text'),
						world = world)

	label_p2 =  pyglet.text.Label('Player 2:',
								x = x1,
								y = y1-50,
								anchor_y='bottom',
                              	color=(57, 255, 20, 255),
                              	batch=player_batch)

	text_p2 = TextWidget(text = '',
						x = x1+75,
						y = y1-50,
						width = 250,
						batch = player_batch,
						cursor = game_window.get_system_mouse_cursor('text'),
						world = world)
	
	# Handler specification #
	game_window.push_handlers(text_p1)
	game_window.push_handlers(text_p2)
	# End of specification #

	# Importation section #
	world.add_object(player_bg)
	world.add_widget(text_p1)
	world.add_widget(text_p2)
	# End of importation #

def game_screen():
	pass

def end_screen():
	pass
#--- MAIN ----------------------------------------------------------------------------------------------------------------

def main():
	world.set_window(game_window)
	game_window.push_handlers(world)

	title_screen()
	player_screen()
	game_screen()
	end_screen()

	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()

if __name__ == '__main__':
	main()