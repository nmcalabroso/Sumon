from gameobject import GameObject
from game.resources import Resources
from random import randint
from random import choice

class Card(GameObject):
	def __init__(self,title,description,name = "card",mana = 0,*args, **kwargs):
		super(Card,self).__init__(name = name,*args,**kwargs)
		self.title = title
		self.description = description
		self.mana = mana
		self.active = True

class MoveCard(Card):
	def __init__(self,*args,**kwargs):
		tile_count = randint(1,5)
		description = "Move a sumo wrestler "+str(tile_count)+" tiles forward."
		super(MoveCard,self).__init__(title = "Move",
									description = description,
									mana = tile_count,
									img = Resources.sprites['card_move'],
									*args,
									**kwargs)
		self.tile_count = tile_count

	def set_tile_count(self):
		self.tile_count = randint(1,5)
		self.description = "Move a sumo wrestler "+str(self.tile_count)+" tiles forward."

class WrestlerCard(Card):
	def __init__(self,*args,**kwargs):
		super(WrestlerCard,self).__init__(title = "None",
										description = "None",
										mana = 0,
										img = Resources.sprites['no_sprite'],
										*args,
										**kwargs)
		self.set_card()

	def set_card(self):
		self.title = choice(Resources.wrestlers)
		self.image = Resources.sprites['card_'+self.title]
		self.weight,self.mana = Resources.stype[self.title.upper()]
		self.description = "Summons a "+self.title.upper()+" wrestler."