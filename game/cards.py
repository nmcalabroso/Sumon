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
		self.clicked = False

	def hit_test(self, x, y):
		if x > (self.x - (self.width*0.5)) and x < (self.x + (self.width*0.5)):
			if y > (self.y - self.height*0.5) and y < (self.y + (self.height*0.5)):
				return True

	def on_mouse_press(self, x, y, button, modifiers):
		if self.active and self.hit_test(x,y):
			if self.world.game_state == Resources.state['PLAYER1']:
				if not self.clicked:
					player = self.world.find_game_object('Player1')
					if player.mana > self.mana:
						player.mana -= self.mana
						mana = self.world.find_label('mana')
						mana.text = player.get_mana_label()
						self.world.program1.append(self)
						self.clicked = True
						self.x,self.y = Resources.card_pos2[len(self.world.program1)-1]
			elif self.world.game_state == Resources.state['PLAYER2']:
				if not self.clicked:
					player = self.world.find_game_object('Player2')
					if player.mana > self.mana:
						player.mana -= self.mana
						mana = self.world.find_label('mana')
						mana.text = player.get_mana_label()
						self.world.program2.append(self)
						self.clicked = True
						self.x,self.y = Resources.card_pos2[len(self.world.program2)-1]


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

