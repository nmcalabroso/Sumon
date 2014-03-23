from gameobject import GameObject

class Player(GameObject):
	def __init__(self,actual_name,name,*args,**kwargs):
		super(Player,self).__init__(name = name,*args,**kwargs)
		self.actual_name = actual_name 
		self.lives = 50
		self.mana = 10
		self.cards = []
		#self.power_cards = []
		#self.sumo_cards = []
		self.active = False
		self.visible = True
		self.opacity = 180

	def get_life_label(self):
		return str(self.lives)

	def get_mana_label(self):
		return str(self.mana)

	def set_life(self, n):
		self.lives = n

	def lose_life(self, n = 1):
		self.lives -= n

	def regain_mana(self, n = 10):
		self.mana += n

	def lose_mana(self, n):
		self.mana -= n

	def add_card(self, card):
		self.cards.append(card)

	def reset_cards(self):
		self.cards = []

	def activate(self):
		self.active = True
		for card in self.cards:
			card.active = True

	def deactivate(self):
		self.active = False
		for card in self.cards:
			card.active = False

	#def add_sumo_card(self, sumo_card):
	#	self.sumo_cards.append(sumo_card)

	#def add_power_card(self, power_card):
	#	self.power_card.append(power_card)
