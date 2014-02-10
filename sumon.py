import pyglet
from game.world import GameWorld
from game.resources import Resources
from game.gui import StartButton
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
	world.add_object(play_button)
	# End of importation #

def player_screen():
	player_bg = Background('player_bg',
						img =  Resources.sprites['player_bg'],
						batch = player_batch)

	# Handler specification #

	# End of specification #

	# Importation section #
	world.add_object(player_bg)
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