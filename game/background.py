from gameobject import GameObject

class Background(GameObject):
	def __init__(self,name,*args, **kwargs):
		super(Background, self).__init__(name = name,*args, **kwargs)