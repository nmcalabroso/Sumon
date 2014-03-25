from gameobject import GameObject
from resources import Resources
from cards import MoveCard
from cards import WrestlerCard
from cards import SpecialCard
from sumo import Wrestler
from random import randint

class GameWorld(GameObject):
	def __init__(self,*args,**kwargs):
		super(GameWorld,self).__init__(name = 'World',img = Resources.sprites['no_sprite'], *args,**kwargs)
		self.game_state = Resources.state['START']
		self.game_objects = [] #gameobject pool
		self.widgets = [] #gui pool
		self.labels = [] #label pool
		self.window = None #game window
		self.active = True
		self.visible = False
		self.cursor_name = 'default_cursor'
		self.focus = None
		self.set_focus(None)
		self.round = 0
		self.start_round = False
		self.tile_clicked = False
		self.program1 = []
		self.program2 = []
		self.commands1 = []
		self.commands2 = []
		self.sequence = []
		self.additional_mana1 = 0
		self.additional_mana2 = 0
		self.current_summon = None
		self.virtual_list = []

	# --- SWITCH ------------------------------------------------------------------------------------------------------

	def switch_to_player(self,batch):
		#bg = self.find_widget('my_bg')
		#bg.set_image(Resources.sprites['title_bg'])
		self.delete_widgets_by_batch(batch)
		self.game_state = Resources.state['PLAYER']

	def switch_to_game(self,batch):
		bg = self.find_widget('my_bg')
		bg.set_image(Resources.sprites['main_bg'])
		self.set_player_names()
		self.delete_widgets_by_batch(batch)
		#print "before:",self.labels
		self.delete_labels_by_batch(batch)
		#print "after:",self.labels
		self.game_state = Resources.state['SETUP']
		self.start_round = True

	def switch_to_end(self):
		o = self.find_widget('end_turn_button')
		batch = o.batch
		self.delete_widgets_by_batch(batch)
		self.delete_labels_by_batch(batch)
		self.game_state = Resources.state['END']
		
	# --- SETUP -------------------------------------------------------------------------------------------------------

	def generate_cards(self, player):
		def randomize_card():
			base = randint(0,100)
			if base<=60:
				return WrestlerCard()
			elif base>=61 and base<=80:
				return MoveCard()
			else:
				return SpecialCard()

		player_title = player
		player = self.find_game_object(player)
		player.reset_cards()

		for i in range(10):
			card = randomize_card()
			card.x,card.y = Resources.card_pos1[i]
			card.world = self
			if player_title == 'Player2' and card.type == 'wrestler':
				card.image = Resources.sprites['card_'+card.title+'_red']
			player.add_card(card)

		player.card_pos = [1]*10

	def set_player_names(self):
		p1 = self.find_game_object('Player1')
		p1.actual_name = self.find_widget('text_p1').document.text
		p2 = self.find_game_object('Player2')
		p2.actual_name = self.find_widget('text_p2').document.text

		print "Player Names:"
		print "Player1:",p1.actual_name
		print "Player2:",p2.actual_name
		
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

	# --- SETUP: GAME OBJECTS -----------------------------------------------------------------------------------------

	def add_game_object(self,obj):
		obj.active = True
		self.game_objects.append(obj)

	def find_game_objects(self,name):
		found_objects = []
		for obj in self.game_objects:
			if obj.name == name:
				found_objects.append(obj)
		return found_objects

	def find_game_object(self,name):
		for obj in self.game_objects:
			if obj.name == name:
				return obj
		return None
 
	def get_game_objects(self,active = True):
		new_pool = []
		for obj in self.game_objects:
			if active and obj.active:
				new_pool.append(obj)
			elif not active and not obj.active:
				new_pool.append(obj)
		return new_pool

	def get_objects_by_batch(self,batch):
		new_pool = []
		for obj in self.game_objects:
			if obj.batch is batch:
				new_pool.append(obj)

	def delete_game_object(self,name):
		for i in range(len(self.game_objects)):
			if self.game_objects[i].name == name:
				obj = self.game_objects[i]
				obj.delete()
				del self.game_objects[i]
				break

	# --- SETUP: LABELS -----------------------------------------------------------------------------------------------

	def add_label(self,label):
		self.labels.append(label)

	def find_label(self,name):
		for label in self.labels:
			if label.name == name:
				return label

	def delete_label(self,text):
		for i in range(len(self.labels)):
			if self.labels[i].text == text:
				label = self.labels[i]
				label.delete()
				del self.labels[i]
				break

	def get_labels(self,batch):
		new_labels = []
		for label in self.labels:
			if label.batch is batch:
				new_labels.append(label)

	def delete_labels_by_batch(self,batch):
		delete_labels = []
		for label in self.labels:
			if label.batch is batch:
				delete_labels.append(label)

		for label in delete_labels:
			self.window.remove_handlers(label)
			label.delete()
			self.labels.remove(label)

	def update_label(self,name,newtext):
		label = self.find_label(name)
		label.text = newtext

	# --- SETUP: WIDGETS ----------------------------------------------------------------------------------------------

	def add_widget(self,widget):
		widget.active = True
		self.widgets.append(widget)

	def find_widget(self,name):
		for widget in self.widgets:
			if widget.name == name:
				return widget
		return None

	def get_widgets(self,active = True):
		new_pool = []
		for obj in self.widgets:
			if obj.name != 'my_bg':
				if active and obj.active:
					new_pool.append(obj)
				elif not active and not obj.active:
					new_pool.append(obj)
		return new_pool

	def get_text_widgets(self,active = True):
		new_pool = []
		for obj in self.widgets:
			if obj.name != 'my_bg' and obj.__class__.__name__ == 'TextWidget':
				if active and obj.active:
					new_pool.append(obj)
				elif not active and not obj.active:
					new_pool.append(obj)
		return new_pool

	def get_widgets_by_batch(self,batch):
		new_pool = []
		for widget in self.widgets:
			if widget.batch is batch:
				new_pool.append(widget)		

	def delete_widget(self,name):
		for i in range(len(self.widgets)):
			if self.widgets[i].name == name:
				widget = self.widgets[i]
				widget.delete()
				del self.widgets[i]
				break

	def delete_widgets_by_batch(self,batch):
		delete_widgets = []
		for widget in self.widgets:
			if widget.batch is batch and widget.name != 'my_bg':
				delete_widgets.append(widget)

		for widget in delete_widgets:
			self.window.remove_handlers(widget)
			widget.delete()
			self.widgets.remove(widget)

	# --- GAME LOGIC --------------------------------------------------------------------------------------------------
	
	def reset_virtual_list(self):
		for tile in self.virtual_list:
			tile.image = Resources.sprites['no_sprite']

	def move_wrestler(self, tile, sumo):
		if sumo != None:
			tile.set_content(sumo)
			tile.wrestler.x = tile.x
			tile.wrestler.y = tile.y

	def execute(self, action, board, player1, player2):
		action_color = action[0]
		action_type = action[1]
		action_mana = int(action[2])
		wrestler_list = []
		total_weight = 0
		temp = None
		wrestler = None

		if action_type == 'summon':
			wrestler_type = action[3]
			row = int(action[4])
			col = int(action[5])
			sumo = Wrestler(sprite_color = action_color, title = wrestler_type, name = 'Wrestler')
			tile = board.my_grid[row][col]
			if tile.wrestler == None:
				self.move_wrestler(tile, sumo)

		elif action_type == 'move':
			row = int(action[3])
			col = int(action[4])
			tile = board.my_grid[row][col]
			sumo = tile.wrestler
			if sumo == None:
				pass
			tile.remove_content()

			# get tile positions
			if action_color == 'blue':
				for i in range(1,action_mana+1):
					wrestler_list = []
					total_weight = 0
					if row-i < 0:
						tile.remove_content()
						player2.lives -= sumo.weight
						return
					
					tile = board.my_grid[row-i][col]
					if tile.wrestler != None:
						for j in range(action_mana-i+2):
							if row-i-j < 0:
								break
							temp = board.my_grid[row-i-j][col]
							if temp.wrestler == None:
								break
							total_weight += temp.wrestler.weight
							wrestler_list.append(temp.wrestler)
							temp.remove_content()

						if total_weight < sumo.weight: # move all forward by one tile
							if tile.wrestler == None:
								self.move_wrestler(tile,sumo)

							j = 1
							for wrestler in wrestler_list:
								if row-i-j < 0:
									player2.lives -= wrestler.weight
								else:
									temp = board.my_grid[row-i-j][col]
									if temp.wrestler == None:
										self.move_wrestler(temp,wrestler)
								j += 1

						else: # stay in position
							tile = board.my_grid[row-i+1][col]
							if tile.wrestler == None:
								self.move_wrestler(tile,sumo)

							j = 0
							for wrestler in wrestler_list:
								temp = board.my_grid[row-i-j][col]
								if temp.wrestler == None:
									self.move_wrestler(temp,wrestler)
								j += 1
							return

			else:
				for i in range(1,action_mana+1):
					wrestler_list = []
					total_weight = 0
					if row+i > 7:
						print tile.row, tile.col
						tile.remove_content()
						print tile.wrestler
						player1.lives -= sumo.weight
						return

					tile = board.my_grid[row+i][col]
					if tile.wrestler != None:
						for j in range(action_mana-i+2):
							if row+i+j > 7:
								break
							temp = board.my_grid[row+i+j][col]
							if temp.wrestler == None:
								break
							total_weight += temp.wrestler.weight
							wrestler_list.append(temp.wrestler)
							temp.remove_content()

						if total_weight < sumo.weight: # move all forward by one tile
							if tile.wrestler == None:
								self.move_wrestler(tile,sumo)

							j = 1
							for wrestler in wrestler_list:
								if row+i+j > 7:
									player1.lives -= wrestler.weight
								else:
									temp = board.my_grid[row+i+j][col]
									if temp.wrestler == None:
										self.move_wrestler(temp,wrestler)
								j += 1

						else: # stay in position
							tile = board.my_grid[row+i-1][col]
							if tile.wrestler == None:
								self.move_wrestler(tile,sumo)

							j = 0
							for wrestler in wrestler_list:
								temp = board.my_grid[row+i+j][col]
								if temp.wrestler == None:
									self.move_wrestler(temp,wrestler)
								j += 1

							return

			if tile.wrestler == None:
				self.move_wrestler(tile,sumo)

		# elif action_type == 'special':

		self.game_state = Resources.state['WAIT']

	def on_mouse_motion(self,x,y,dx,dy):
		self.window.set_mouse_cursor(None)

	def change_player(self):
		player1 = self.find_game_object('Player1')
		player2 = self.find_game_object('Player2')
		label_player = self.find_label('player')
		name = self.find_label('player_name')
		lives = self.find_label('lives')
		mana = self.find_label('mana')

		if self.game_state == Resources.state['TRANSITION_PLAYER1']:
			player1.activate()
			player2.deactivate()
			label_player.text = "Player1:"
			player = player1

		else:
			player2.activate()
			player1.deactivate()
			label_player.text = "Player2:"
			name.text = player2.actual_name
			player = player2

		name.text = player.actual_name
		lives.text = player.get_life_label()
		mana.text = player.get_mana_label()
			
	def update(self,dt): #game logic loop
		# Transition states are for setting up the next state. SETUP is also a transition state.
		# Use boolean self.start_round to execute once during any state.
		# Player input should be in their respective classes.
		# (e.g what to do when clicking a card should be seen in cards.py)
		
		if self.game_state == Resources.state['SETUP']:
			self.round+=1
			self.start_round = True
			self.program1 = []
			self.program2 = []
			self.game_state = Resources.state['TRANSITION_PLAYER1']

		elif self.game_state == Resources.state['TRANSITION_PLAYER1']:
			self.virtual_list = []
			self.round += 1
			self.start_round = False
			self.generate_cards('Player1')
			self.change_player()
			self.commands1 = []
			self.commands2 = []
			self.game_state = Resources.state['PLAYER1']

		# elif self.game_state == Resources.state['PLAYER1']:
		# 	self.start_round = True

		elif self.game_state == Resources.state['DELETE1']:
			for i, card in enumerate(self.program1):
				card.x, card.y = Resources.card_pos2[i]
			
			self.game_state = Resources.state['PLAYER1']

		elif self.game_state == Resources.state['TRANSITION_PLAYER2']:
			self.reset_virtual_list()
			self.virtual_list = []
			self.start_round = False
			self.generate_cards('Player2')
			self.change_player()

			self.player_program = open("player1_program.txt", "w")
			for command in self.commands1:
				self.player_program.write(command)
			self.player_program.close()

			self.game_state = Resources.state['PLAYER2']
	
		# elif self.game_state == Resources.state['PLAYER2']:
		# 	self.start_round = True

		elif self.game_state == Resources.state['DELETE2']:
			for i, card in enumerate(self.program2):
				card.x, card.y = Resources.card_pos2[i]
			
			self.game_state = Resources.state['PLAYER2']

		elif self.game_state == Resources.state['TRANSITION_BOARD']:
			self.reset_virtual_list()
			player1 = self.find_game_object('Player1')
			player2 = self.find_game_object('Player2')
			player1.deactivate()
			player2.deactivate()

			self.player_program = open("player2_program.txt", "w")
			for command in self.commands2:
				self.player_program.write(command)
			self.player_program.close()

			label_player = self.find_label('player')
			name = self.find_label('player_name')
			lives = self.find_label('lives')
			mana = self.find_label('mana')

			label_player.text = ''
			name.text = ''
			lives.text = ''
			mana.text = ''
			self.game_state = Resources.state['BOARD']

		elif self.game_state == Resources.state['BOARD']:
			# format: <card_type> <mana> <parameters>
			# example: move 5 row col
			# example: summon 1 jonokuchi row col

			self.start_round = False
			self.program1 = []
			self.program2 = []
			self.sequence = []

			#get commands from both programs
			player_program1 = open("player1_program.txt", "r")
			player_program2 = open("player2_program.txt", "r")
			self.program1 = player_program1.readlines()
			self.program2 = player_program2.readlines()
			player_program1.close()
			player_program2.close()

			#get max number of commands
			if len(self.program1) > len(self.program2):
				max = len(self.program1)
			else:
				max = len(self.program2)

			#for each command
			for i in range(max):
				action1 = None
				action2 = None

				#get command from self.program1
				if i < len(self.program1):
					action1 = self.program1[i]
					action1 = action1.split()
					action1.insert(0, 'blue')

				#get command from self.program2
				if i < len(self.program2):
					action2 = self.program2[i]
					action2 = action2.split()
					action2.insert(0, 'red')

				# compare priorities and do both commands (assumes action1 and action2 are not null)
				if action1 != None and action2 != None:
					if Resources.card_priority[action1[1]] > Resources.card_priority[action2[1]]:
						turn = (action1, action2)
					elif Resources.card_priority[action1[1]] < Resources.card_priority[action2[1]]:
						turn = (action2, action1)
					else: # equal priority; compare mana
						if action1[2] > action2[2]:
							turn = (action1, action2)
						if action1[2] < action2[2]:
							turn = (action2, action1)
						else: #random
							rand = randint(0,100)
							if rand < 50:
								turn = (action1, action2)
							else:
								turn = (action2, action1)

				# else if one is null
				elif action1 != None:
					turn = (action1,)
				else:
					turn = (action2,)

				self.sequence.append(turn)

			self.game_state = Resources.state['EXECUTE']

		elif self.game_state == Resources.state['EXECUTE']:
			player1 = self.find_game_object('Player1')
			player2 = self.find_game_object('Player2')

			if player1.lives <= 0 or player2.lives <=0:
				self.switch_to_end()
				return

			if self.sequence == []:
				self.game_state = Resources.state['REPLENISH']
			else:
				player1 = self.find_game_object('Player1')
				player2 = self.find_game_object('Player2')
				board = self.find_game_object('game_board')
				turn = self.sequence.pop(0)
				for action in turn:
					self.execute(action, board, player1, player2)

		elif self.game_state == Resources.state['REPLENISH']:
			player1 = self.find_game_object('Player1')
			player2 = self.find_game_object('Player2')
			player1.mana += 5
			player2.mana += 5
			self.game_state = Resources.state['SETUP']

		elif self.game_state == Resources.state['END']:
			player1 = self.find_game_object('Player1')
			player2 = self.find_game_object('Player2')

			# print "GAME OVER!"
			if player1.lives <= 0:
				winner = player2.actual_name
				mana_left = player2.get_mana_label()
			else:
				winner = player1.actual_name
				mana_left = player1.get_mana_label()
			
			rounds = str(self.round-1)

			# print winner+" WINS!"
			self.update_label("player_end",winner+" WINS!")
			# print "Mana left: "+mana_left
			self.update_label("mana_end",mana_left)
			# print "Total Rounds: "+rounds
			self.update_label("rounds_end",rounds)
