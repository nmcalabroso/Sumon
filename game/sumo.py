from gameobject import GameObject
from game.resources import Resources

class Wrestler(GameObject):
	def __init__(self,title,sprite_color,name,*args,**kwargs):
		super(Wrestler,self).__init__(name = name, 
									img = Resources.sprites['no_sprite'],
									*args,
									**kwargs)
		self.title = title
		self.sprite_color = sprite_color
		self.set_wrestler()

	def set_wrestler(self):
		self.image = Resources.sprites['wrestler_' + self.title + '_' + self.sprite_color]
		self.weight,self.mana = Resources.stype[self.title.upper()]
		self.original_weight = self.weight
		self.reverse = False
		self.avatar = False
