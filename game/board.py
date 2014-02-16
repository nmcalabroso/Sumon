from gameobject import GameObject

class GameBoard(GameObject):

	def __init__(self,name,*args,**kwargs):
		super(GameBoard,self).__init__(name = name, *args, **kwargs)
		self.my_grid = [[i for i in range(8)] for j in range(8)] #initial 8x8 logical grid

	def get_unit(self,row,col):
		pass

	def delete_unit(self,row,col):
		pass

	def add_unit(self,row,col):
		pass

	def apply_card(self,row,col):
		pass