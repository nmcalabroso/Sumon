from gameobject import GameObject
from game.resources import Resources

class SumoWrestler(GameObject):
	def __init__(self,wrestler_info,*args, **kwargs):
		self.race,self.type = wrestler_info
		self.weight,self.summoning_energy = Resources.stype[self.type]
		image = Resources.sprites[self.race+'_'+self.type]
		super(SumoWrestler, self).__init__(img = image,*args, **kwargs)
		self.velocity_x = 100
		self.velocity_y = 100

	def update(self,dt):
		super(SumoWrestler, self).update(dt)
		self.x += self.velocity_x*dt
		self.y += self.velocity_y*dt
