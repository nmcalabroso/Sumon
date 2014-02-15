#import pyglet
from game.gameobject import GameObject
from resources import Resources

class GameWorld(GameObject):

	def __init__(self,*args,**kwargs):
		super(GameWorld,self).__init__(name = 'World',img = Resources.sprites['no_sprite'], *args,**kwargs)
		self.game_state = Resources.state['START']
		self.pool = [] #gameobject pool
		self.widgets = [] #UIObject pool
		self.labels = [] #label pool
		self.window = None #game window
		self.active = True
		self.visible = False
		self.cursor_name = 'default_cursor'
		self.focus = None
		self.set_focus(None)

	def switch_to_player(self):
		self.game_state = Resources.state['PLAYER']
		bg = self.find_game_object('my_bg')
		bg.set_image(Resources.sprites['title_bg'])

	def switch_to_game(self):
		self.game_state = Resources.state['GAME']
		bg = self.find_game_object('my_bg')
		bg.set_image(Resources.sprites['title_bg'])
		self.set_player_names()

	def switch_to_end(self):
		pass

	def set_player_names(self):
		p1 = self.find_game_object('Player1')
		p1.name = self.widgets[0].document.text
		p2 = self.find_game_object('Player2')
		p2.name = self.widgets[1].document.text

		self.labels[0].text += p1.name
		self.labels[1].text += p2.name

		print "Player Names:"
		print "Player1:",p1.name
		print "Player2:",p2.name
		
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
		obj.active = True
		self.pool.append(obj)

	def add_label(self,label):
		self.labels.append(label)

	def add_widget(self,wid):
		wid.active = True
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

	def on_mouse_motion(self,x,y,dx,dy):
		self.window.set_mouse_cursor(None)