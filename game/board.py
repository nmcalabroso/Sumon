from gameobject import GameObject
from resources import Resources

class GameBoard(GameObject):

	def __init__(self,name,world,*args,**kwargs):
		super(GameBoard,self).__init__(name = name, *args, **kwargs)
		self.world = world
		"""self.my_grid = [[Tile(name = "Tile"+str(i)+str(j),
							row = i,
							col = j,
							x = Resources.board_grid[i][j][0],
							y = Resources.board_grid[i][j][1])
						for i in range(8)] for j in range(8)] #initial 8x8 logical grid"""
		self.my_grid = None
		self.set_grid()

	def set_grid(self):
		grid = []
		for i in range(8):
			row = []
			for j in range(8):
				x = Tile(name = "Tile"+str(i)+str(j),
						row = i,
						col = j,
						world = self.world,
						x = Resources.board_grid[i][j][0],
						y = Resources.board_grid[i][j][1])
				row.append(x)
				self.world.window.push_handlers(x)
			grid.append(row)

		self.my_grid = grid

	def hit_test(self,x,y):
		if x > (self.x - (self.width)) and x < (self.x + (self.width)):
			if y > (self.y - self.height) and y < (self.y + (self.height)):
				return True
		return False

	def on_mouse_press(self,x,y,button,modifiers):
		pass

	def on_mouse_motion(self,x,y,dx,dy):
		pass

	def get_unit(self,row,col):
		pass

	def delete_unit(self,row,col):
		pass

	def add_unit(self,row,col):
		pass

	def apply_card(self,row,col):
		pass

class Tile(GameObject):
	def __init__(self,name,row,col,world,*args,**kwargs):
		super(Tile,self).__init__(name = name, img = Resources.sprites['tile'], *args,**kwargs)
		self.location = (row,col)
		self.wrestler = None
		self.world = world
		self.row = row
		self.col = col
		
	def set_content(self,obj):
		self.wrestler = obj

	def remove_content(self,obj):
		self.wrestler = None

	def hit_test(self,x,y):
		if x > self.x and x < (self.x + (self.width)):
			if y > self.y and y < (self.y + (self.height)):
				return True
		return False

	def on_mouse_press(self,x,y,button,modifiers):
		if self.hit_test(x,y):
			# print "Tile:",self.name,"x=",self.x,"y=",self.y,"width=",self.width,"height:",self.height
			if self.world.game_state == Resources.state['TILE1']:
				self.world.player_program.write(" " + str(self.row) + " " + str(self.col) + "\n")
				self.world.game_state = Resources.state['PLAYER1']

			elif self.world.game_state == Resources.state['TILE2']:
				self.world.player_program.write(" " + str(self.row) + " " + str(self.col) + "\n")
				self.world.game_state = Resources.state['PLAYER2']

