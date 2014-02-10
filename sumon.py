import pyglet
from game.world import GameWorld
from game.resources import Resources
from game.gui import UIObject
from game.background import Background
from game.sumo import SumoWrestler

game_window = pyglet.window.Window(Resources.window_width, Resources.window_height)
game_window.set_caption("My Game")
game_window.set_location(Resources.center_x,Resources.center_y)
world = GameWorld()

@game_window.event
def on_draw():
	game_window.clear()
	for obj in world.get_game_objects():
		obj.draw()

def update(dt):
	for obj in world.get_game_objects():
		obj.update(dt)

def main():
	# Instantiation section #
	world.set_window(game_window)
	title_bg 	= Background(image = Resources.sprites['title_bg'])
	play_button = UIObject(image = Resources.sprites['play_button'],
						   x = Resources.window_width*0.5,
						   y = Resources.window_height*0.5)
	wrestler 	= SumoWrestler(wrestler_info = ('BLACK','JONOKUCHI'),
								x = 0,
								y = 0)
	
	# End of Instantiation #

	# Importation section #
	world.add_object(title_bg)
	world.add_object(play_button)
	world.add_object(wrestler)
	# End of Imporation #
	
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()

if __name__ == '__main__':
	main()