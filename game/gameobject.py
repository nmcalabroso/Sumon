from pyglet.sprite import Sprite

class GameObject(Sprite):

	def __init__(self,*args,**kwargs):
		super(GameObject, self).__init__(*args, **kwargs)
		self.active = True
		self.velocity_x = 0
		self.velocity_y = 0

	def update(self,dt):
		pass