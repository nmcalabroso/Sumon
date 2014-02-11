#import pyglet
from resources import Resources
from game.gameobject import GameObject

class GameWorld(GameObject):

	def __init__(self,*args,**kwargs):
		super(GameWorld,self).__init__(name = 'World',img = Resources.sprites['no_sprite'], *args,**kwargs)
		self.game_state = Resources.state['START']
		self.pool = [] #gameobject pool
		self.widgets = [] #UIObject pool
		self.window = None #game window
		self.active = False
		self.cursor_name = 'default_cursor'
		self.focus = None
		self.set_focus(None)
		
	def set_window(self,window):
		self.window = window

	def set_focus(self,focus):
		if self.focus:
			self.focus.caret.visible = False
			self.focus.caret.mark = self.focus.caret.position = 0
		
		self.focus = focus
		if self.focus:
			self.focus.caret.visible = True
			self.focus.caret.mark = 0
			self.focus.caret.position = len(self.focus.document.text)

	def add_object(self,obj):
		self.pool.append(obj)

	def add_widget(self,wid):
		self.widgets.append(wid)

	def find_widget(self,name):
		for wid in self.widgets:
			if wid.name == name:
				return wid
		return None

	def get_widgets(self,active = True):
		new_pool = []
		for obj in self.widgets:
			if active and obj.active:
				new_pool.append(obj)
			elif not active and not obj.active:
				new_pool.append(obj)
		return new_pool

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

	"""def on_mouse_motion(self,x,y,dx,dy):
		self.cursor_name = 'default_cursor'
		if self.game_state == Resources.state['START']:
			start_button = self.find_game_object('StartButton')
			if x > (start_button.x - (start_button.width*0.5)) and x < (start_button.x + (start_button.width*0.5)):
	  			if y > (start_button.y - start_button.height*0.5) and y < (start_button.y + (start_button.height*0.5)):
	  				self.cursor_name = 'active_cursor'
	  	#elif self.game_state == Resources.state['PLAYER']:
	  	cursor = pyglet.window.ImageMouseCursor(Resources.sprites[self.cursor_name],16,8)
		self.window.set_mouse_cursor(cursor)"""
