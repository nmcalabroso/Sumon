from gameobject import GameObject

class Background(GameObject):
	def __init__(self,image, *args, **kwargs):
		super(Background, self).__init__(img = image,*args, **kwargs)
		self.name = "BG"