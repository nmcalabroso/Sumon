import pyglet
from gameobject import GameObject
from pyglet.window import mouse
from resources import Resources

__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

class UIObject(GameObject):
	def __init__(self,world,*args,**kwargs):
		super(UIObject, self).__init__(name = 'UIObject',*args, **kwargs)
		self.world = world

class StartButton(UIObject):
	def __init__(self,world,*args,**kwargs):
		super(StartButton, self).__init__(world = world,*args,**kwargs)
		self.name = 'StartButton'

	def on_mouse_press(self, x, y, button, modifiers):
		if self.active:
			if button == mouse.LEFT:
		   		if x > (self.x - (self.width*0.5)) and x < (self.x + (self.width*0.5)):
		   			if y > (self.y - self.height*0.5) and y < (self.y + (self.height*0.5)):
		   				print "StartButton: Proceeding to PLAYER_STATE."
                        self.world.game_state = Resources.state['PLAYER']
                        self.active = False
		   				
class Rectangle(object):
    '''Draws a rectangle into a batch.'''
    def __init__(self, x1, y1, x2, y2, batch):
        self.vertex_list = batch.add(4, pyglet.gl.GL_QUADS, None,
            ('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
            ('c4B', [200, 200, 220, 255] * 4)
        )

class TextWidget(UIObject):
    def __init__(self, text, x, y, width, batch, cursor, world,*args,**kwargs):
        super(TextWidget,self).__init__(img = Resources.sprites['no_sprite'],
                                        x = x,
                                        y = y,
                                        batch = batch,
                                        world = world,
                                        *args,
                                        **kwargs
                                        )

        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), 
            dict(color=(0, 0, 0, 255))
        )
        font = self.document.get_font()
        height = font.ascent - font.descent

        self.layout = pyglet.text.layout.IncrementalTextLayout(
            self.document, width, height, multiline=False, batch=batch)
        self.caret = pyglet.text.caret.Caret(self.layout)

        self.layout.x = x
        self.layout.y = y

        self.text_cursor = cursor

        self.world = world

        # Rectangular outline
        pad = 2
        self.rectangle = Rectangle(x - pad, y - pad, 
                                   x + width + pad, y + height + pad, batch)

    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
            0 < y - self.layout.y < self.layout.height)

    def on_mouse_motion(self, x, y, dx, dy):
        for widget in self.world.widgets:
            if widget.hit_test(x, y):
                print 'Entering TextWidget.'
                self.world.window.set_mouse_cursor(self.text_cursor)
                break
        else:
            self.world.window.set_mouse_cursor(None)

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.world.widgets:
            if widget.hit_test(x, y):
                print 'Focusing TextWidget.'
                self.world.set_focus(widget)
                break
        else:
            self.world.set_focus(None)

        if self.world.focus:
            self.world.focus.caret.on_mouse_press(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.world.focus:
            self.world.focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_text(self, text):
        if self.world.focus:
            self.world.focus.caret.on_text(text)

    def on_text_motion(self, motion):
        if self.world.focus:
            self.world.focus.caret.on_text_motion(motion)
      
    def on_text_motion_select(self, motion):
        if self.world.focus:
            self.world.focus.caret.on_text_motion_select(motion)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.TAB:
            if modifiers & pyglet.window.key.MOD_SHIFT:
                dir = -1
            else:
                dir = 1

            if self.world.focus in self.world.widgets:
                i = self.world.widgets.index(self.focus)
            else:
                i = 0
                dir = 0
            self.world.set_focus(self.world.widgets[(i + dir) % len(self.world.widgets)])