from gameobject import GameObject
from resources import Resources

class GameBoard(GameObject):
	def __init__(self,name,world,*args,**kwargs):
		super(GameBoard,self).__init__(name = name, *args, **kwargs)
		self.world = world
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
		self.glow = False

	def set_content(self,obj):
		self.wrestler = obj

	def remove_content(self):
		self.wrestler = None

	def hit_test(self,x,y):
		if x > self.x and x < (self.x + (self.width)):
			if y > self.y and y < (self.y + (self.height)):
				return True
		return False

	def on_mouse_press(self,x,y,button,modifiers):
		if self.hit_test(x,y):
			if self.world.game_state == Resources.state['SWAP1']:
				command = self.world.commands1.pop(-1)
				command = command + " " + str(self.row) + " " + str(self.col)
				self.world.commands1.append(command)
				self.image = self.world.current_summon
				self.world.virtual_list.append(self)
				self.opacity = 175
				self.world.game_state = Resources.state['TILE1']

			elif self.world.game_state == Resources.state['SWAP2']:
				command = self.world.commands2.pop(-1)
				command = command + " " + str(self.row) + " " + str(self.col)
				self.world.commands2.append(command)
				self.image = self.world.current_summon
				self.world.virtual_list.append(self)
				self.opacity = 175
				self.world.game_state = Resources.state['TILE2']

			elif self.world.game_state == Resources.state['TILE1']:
				command = self.world.commands1.pop(-1)
				words = command.split(" ")
				if words[0] == "summon":
					command = command + " " + str(self.col) + "\n"
				else:
					command = command + " " + str(self.row) + " " + str(self.col) + "\n"

				self.world.commands1.append(command)
				if self.world.current_summon != None:
					self.image = self.world.current_summon
				self.world.virtual_list.append(self)
				self.opacity = 175
				self.world.game_state = Resources.state['PLAYER1']

			elif self.world.game_state == Resources.state['TILE2']:
				command = self.world.commands2.pop(-1)
				words = command.split(" ")
				if words[0] == "summon":
					command = command + " " + str(self.col) + "\n"
				else:
					command = command + " " + str(self.row) + " " + str(self.col) + "\n"

				self.world.commands2.append(command)
				if self.world.current_summon != None:
					self.image = self.world.current_summon
				self.opacity = 175
				self.world.virtual_list.append(self)
				self.world.game_state = Resources.state['PLAYER2']

	def on_mouse_motion(self,x,y,dx,dy):
		if self.hit_test(x,y):
			if self.world.game_state == Resources.state['TILE1'] or self.world.game_state == Resources.state['TILE2']:
				self.glow = True
				return

			if self.world.game_state == Resources.state['SWAP1'] or self.world.game_state == Resources.state['SWAP2']:
				self.glow = True
				return

		self.glow = False