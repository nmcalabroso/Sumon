from gameobject import GameObject
from resources import Resources

class GameBoard(GameObject):

	def __init__(self,name,*args,**kwargs):
		super(GameBoard,self).__init__(name = name, *args, **kwargs)
		self.my_grid = [[Tile(name = "Tile"+str(i)+str(j),row = i, col = j) for i in range(8)] for j in range(8)] #initial 8x8 logical grid

	def get_unit(self,row,col):
		pass

	def delete_unit(self,row,col):
		pass

	def add_unit(self,row,col):
		pass

	def apply_card(self,row,col):
		pass

class Tile(GameObject):
	def __init__(self,name,row,col,*args,**kwargs):
		super(Tile,self).__init__(name = name, img = Resources.sprites['tile'], *args,**kwargs)
		self.location = (row,col)
		self.wrestler = None

	def set_content(self,obj):
		self.wrestler = obj

	def remove_content(self,obj):
		self.wrestler = None