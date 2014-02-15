from gameobject import GameObject
from resources import Resources

class Background(GameObject):
	def __init__(self,name,*args, **kwargs):
		super(Background, self).__init__(name = name,*args, **kwargs)
		self.x = Resources.window_width * 0.5
		self.y = Resources.window_height * 0.5

	def set_image(self,img):
		self.image = img
