from gameobject import GameObject

class Player(GameObject):
	def __init__(self,name,*args,**kwargs):
		super(Player,self).__init__(*args,**kwargs)
		self.name = "Player"
		self.actual_name = name
		self.lives = 20
		self.mana = 3
		self.summoning_energy = 5

	def set_lives(self,n):
		self.lives+=n

	def set_mana(self,n):
		self.mana+=n

	def set_summoning_energy(self,n):
		self.summoning_energy+=n