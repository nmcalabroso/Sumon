from resources import Resources
from game.gameobject import GameObject
import pyglet
class GameWorld(GameObject):

	def __init__(self,*args,**kwargs):
		super(GameWorld,self).__init__(img = Resources.sprites['no_sprite'], *args,**kwargs)
		self.game_state = Resources.state['START']
		self.pool = [] #gameobject pool
		self.window = None #game window
		self.active = False
		self.cursor_name = 'default_cursor'

	def set_window(self,window):
		self.window = window

	def add_object(self,obj):
		self.pool.append(obj)

	def find_game_objects(self,name):
		found_objects = []
		for obj in self.pool:
			if obj.name == name:
				found_objects.append(obj)
		return found_objects

	def find_game_object(self,name):
		for obj in self.pool:
			if obj.name == name:
				return obj
		return None
 
	def get_game_objects(self,active = True):
		new_pool = []
		for obj in self.pool:
			if active and obj.active:
				new_pool.append(obj)
			elif not active and not obj.active:
				new_pool.append(obj)
		return new_pool

	def on_mouse_motion(self,x,y,dx,dy):
		if self.game_state == Resources.state['START']:
			start_button = self.find_game_object('StartButton')
			if x > (start_button.x - (start_button.width*0.5)) and x < (start_button.x + (start_button.width*0.5)):
	  			if y > (start_button.y - start_button.height*0.5) and y < (start_button.y + (start_button.height*0.5)):
	  				self.cursor_name = 'active_cursor'
	  			else:
	  				self.cursor_name = 'default_cursor'
	  		else:
	  			self.cursor_name = 'default_cursor'
	  	cursor = pyglet.window.ImageMouseCursor(Resources.sprites[self.cursor_name],16,8)
		self.window.set_mouse_cursor(cursor)
