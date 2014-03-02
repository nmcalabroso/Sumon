from gameobject import GameObject
from resources import Resources
from cards import MoveCard
from cards import WrestlerCard
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
		self.round = 1
		self.start_round = False

	def switch_to_player(self,batch):
		bg = self.find_widget('my_bg')
		bg.set_image(Resources.sprites['title_bg'])
		self.delete_widgets_by_batch(batch)
		self.game_state = Resources.state['PLAYER']

	def switch_to_game(self,batch):
		bg = self.find_widget('my_bg')
		bg.set_image(Resources.sprites['title_bg'])
		self.set_player_names()
		self.delete_widgets_by_batch(batch)
		#print "before:",self.labels
		self.delete_labels_by_batch(batch)
		#print "after:",self.labels
		self.game_state = Resources.state['GAME']
		self.start_round = True

	def switch_to_end(self):
		pass

	def generate_cards(self):
		def randomize_card():
			base = randint(0,100)
			if base<=40:
				return WrestlerCard()
			elif base>=41 and base<=80:
				return MoveCard()
			else:
				return MoveCard() #change this to powercard later

		player_1 = self.find_game_object('Player1')
		player_2 = self.find_game_object('Player2')
		player_1.reset_cards()
		player_2.reset_cards()

		for i in range(10):
			card = randomize_card()
			card.x,card.y = Resources.card_pos1[i]
			player_1.add_card(card)

		for i in range(10):
			card = randomize_card()
			card.x,card.y = Resources.card_pos1[i]
			player_2.add_card(card)

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

	def update_label(self,text,newtext):
		label = self.find_label(text)
		label.text = newtext

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

	def on_mouse_motion(self,x,y,dx,dy):
		self.window.set_mouse_cursor(None)

	def change_player(self):
		player1 = self.find_game_object('Player1')
		player2 = self.find_game_object('Player2')
		label_player = self.find_label('player')
		name = self.find_label('player_name')
		lives = self.find_label('lives')
		mana = self.find_label('mana')

		if self.round % 2 != 0:
			player1.active = True
			player2.active = False
			label_player.text = "Player1:"
			player = player1
		else:
			player1.active = False
			player2.active = True
			label_player.text = "Player2:"
			name.text = player2.actual_name
			player = player2

		name.text = player.actual_name
		lives.text = player.get_life_label()
		mana.text = player.get_mana_label()
			
	def update(self,dt): #game logic loop
		if self.game_state == Resources.state['GAME']:
			if self.start_round:
				self.generate_cards()
				self.change_player()
				self.start_round = False
			self.round += 1


