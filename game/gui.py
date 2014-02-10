from gameobject import GameObject
from pyglet.window import mouse
from resources import Resources

class UIObject(GameObject):
	def __init__(self,world,image,*args,**kwargs):
		super(UIObject, self).__init__(img = image,*args, **kwargs)
		self.name = 'UIObject'
		self.world = world

class StartButton(UIObject):
	def __init__(self,world,image,*args,**kwargs):
		super(StartButton, self).__init__(world = world,image = image,*args,**kwargs)
		self.name = 'StartButton'

	def on_mouse_press(self, x, y, button, modifiers):
		if button == mouse.LEFT:
	   		if x > (self.x - (self.width*0.5)) and x < (self.x + (self.width*0.5)):
	   			if y > (self.y - self.height*0.5) and y < (self.y + (self.height*0.5)):
	   				self.world.game_state = Resources.state['GAME']

	def update(self,dt):
		if self.world.game_state != Resources.state['START']:
			self.active = False