from gameobject import GameObject

class UIObject(GameObject):
	def __init__(self,image,*args,**kwargs):
		super(UIObject, self).__init__(img = image,*args, **kwargs)
		self.name = 'UIObject'
