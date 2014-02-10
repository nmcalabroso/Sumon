from resources import Resources

class GameWorld:

	def __init__(self):
		self.game_state = Resources.state['START']
		self.pool = [] #gameobject pool
		self.window = None #game window

	def set_window(self,window):
		self.widnow = window

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