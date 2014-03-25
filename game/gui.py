import pyglet
from gameobject import GameObject
from pyglet.text import Label
from pyglet.text.layout import ScrollableTextLayout
from pyglet.window import mouse
from resources import Resources

__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

class UIObject(GameObject):
    def __init__(self,name,world,curr_state,*args,**kwargs):
        super(UIObject, self).__init__(name = name,*args, **kwargs)
        self.world = world
        self.curr_state = curr_state

class Button(UIObject):
    def __init__(self,name,curr_state,target_state,world,*args,**kwargs):
        super(Button, self).__init__(name = name, curr_state = curr_state, world = world,*args,**kwargs)
        self.name = name
        self.hand_cursor = world.window.get_system_mouse_cursor('hand')
        self.target_game_state = target_state

    def hit_test(self,x,y):
        if x > (self.x - (self.width*0.5)) and x < (self.x + (self.width*0.5)):
            if y > (self.y - self.height*0.5) and y < (self.y + (self.height*0.5)):
                return True

    def on_mouse_press(self, x, y, button, modifiers):
        if self.active and self.world.game_state == Resources.state[self.curr_state]:
            if button == mouse.LEFT:
                if self.hit_test(x,y):
                    # print "Button: Proceeding to",self.target_game_state,"STATE."
                    if self.target_game_state == 'PLAYER':
                        self.world.switch_to_player(self.batch)
                    elif self.target_game_state == 'SETUP':
                        self.world.switch_to_game(self.batch)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.active and self.world.game_state == Resources.state[self.curr_state]:
            if self.hit_test(x,y):
                # print "Entering Button:",self.name
                self.world.window.set_mouse_cursor(self.hand_cursor)

class EndTurnButton(UIObject):
    def __init__(self,name,curr_state,world,*args,**kwargs):
        super(EndTurnButton,self).__init__(name = name,
                                            curr_state = curr_state,
                                            world = world,
                                            *args,
                                            **kwargs)
        self.name = name
        self.hand_cursor = world.window.get_system_mouse_cursor('hand')

    def hit_test(self,x,y):
        if x > self.x and x < (self.x + (self.width)):
            if y > self.y and y < (self.y + (self.height)):
                return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.hit_test(x,y):
            self.image = Resources.sprites['end_turn_button2']
            
            if self.world.game_state == Resources.state['PLAYER1'] or self.world.game_state == Resources.state['PROGRAMMING1']:
                self.world.normal_phase()
                self.world.game_state = Resources.state['TRANSITION_PLAYER2']
                
            elif self.world.game_state == Resources.state['PLAYER2'] or self.world.game_state == Resources.state['PROGRAMMING2']:
                self.world.normal_phase()
                self.world.game_state = Resources.state['TRANSITION_BOARD']

            elif self.world.game_state == Resources.state['WAIT']:
                self.world.game_state = Resources.state['EXECUTE']

    def on_mouse_release(self,x,y,button,modifiers):
        if button == mouse.LEFT and self.hit_test(x,y):
            self.image = Resources.sprites['end_turn_button']

    def on_mouse_motion(self, x, y, dx, dy):
        if self.active and self.world.game_state == Resources.state[self.curr_state]:
            if self.hit_test(x,y):
                #print "Entering Button:",self.name
                self.world.window.set_mouse_cursor(self.hand_cursor)

class ProgramButton(UIObject):
    def __init__(self,name,curr_state,world,*args,**kwargs):
        super(ProgramButton,self).__init__(name = name,
                                            curr_state = curr_state,
                                            world = world,
                                            *args,
                                            **kwargs)
        self.name = name
        self.hand_cursor = world.window.get_system_mouse_cursor('hand')

    def hit_test(self,x,y):
        if x > self.x and x < (self.x + (self.width)):
            if y > self.y and y < (self.y + (self.height)):
                return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.hit_test(x,y):
            self.image = Resources.sprites['program_button2']
            
            if self.world.game_state == Resources.state['PLAYER1']:
                self.world.programming_phase()
                self.world.game_state = Resources.state['PROGRAMMING1']
                
            elif self.world.game_state == Resources.state['PLAYER2']:
                self.world.programming_phase()
                self.world.game_state = Resources.state['PROGRAMMING2']

    def on_mouse_release(self,x,y,button,modifiers):
        if button == mouse.LEFT and self.hit_test(x,y):
            self.image = Resources.sprites['program_button']

    def on_mouse_motion(self, x, y, dx, dy):
        if self.active and self.world.game_state == Resources.state[self.curr_state]:
            if self.hit_test(x,y):
                #print "Entering Button:",self.name
                self.world.window.set_mouse_cursor(self.hand_cursor)

class UILabel(Label):
    def __init__(self,name,*args,**kwargs):
        super(UILabel, self).__init__(*args,**kwargs)
        self.name = name

class MyRectangle(UIObject):
    def __init__(self,name,opacity,curr_state,*args,**kwargs):
        super(MyRectangle, self).__init__(name = name, curr_state = curr_state, world = None,*args,**kwargs)
        self.opacity = opacity

    def set_image(self,img):
        self.image = img

class Rectangle(object):
    '''Draws a rectangle into a batch.'''
    def __init__(self, x1, y1, x2, y2, batch):
        self.vertex_list = batch.add(4, pyglet.gl.GL_QUADS, None,
            ('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
            ('c4B', [200, 200, 220, 255] * 4)
        )

class TextWidget(UIObject):
    def __init__(self, text, x, y, width, batch, cursor, curr_state, world, name, *args,**kwargs):
        super(TextWidget,self).__init__(
                                        name = name,
                                        img = Resources.sprites['no_sprite'],
                                        x = x,
                                        y = y,
                                        batch = batch,
                                        curr_state = curr_state,
                                        world = world,
                                        *args,
                                        **kwargs
                                        )
        self.batch = batch
        self.text_cursor = cursor
        self.world = world

        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), 
            dict(color=(0, 0, 0, 255))
        )
        font = self.document.get_font()
        height = font.ascent - font.descent
        self.layout = pyglet.text.layout.IncrementalTextLayout(
                                                            self.document,
                                                            width,
                                                            height,
                                                            multiline=False,
                                                            batch=batch)
        self.caret = pyglet.text.caret.Caret(self.layout)

        self.layout.x = x
        self.layout.y = y

        # Rectangular outline
        pad = 2
        self.rectangle = Rectangle(x - pad, y - pad,
                                   x + width + pad,
                                   y + height + pad, 
                                   batch)

    def hit_test(self, x, y):
        if self.active and self.world.game_state == Resources.state[self.curr_state]:
            return (0 < x - self.layout.x < self.layout.width and
                    0 < y - self.layout.y < self.layout.height)
        return False

    def on_mouse_motion(self, x, y, dx, dy):
        if self.hit_test(x, y):
            # print 'Hovering TextWidget:',self.name
            self.world.window.set_mouse_cursor(self.text_cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.hit_test(x, y):
                # print 'Focusing TextWidget:',self.name
                self.world.set_focus(self)

        if self.world.focus is self:
            self.world.focus.caret.on_mouse_press(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.world.focus is self:
            self.world.focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_text(self, text):
        if self.world.focus is self:
            self.world.focus.caret.on_text(text)

    def on_text_motion(self, motion):
        if self.world.focus is self:
            self.world.focus.caret.on_text_motion(motion)
      
    def on_text_motion_select(self, motion):
        if self.world.focus is self:
            self.world.focus.caret.on_text_motion_select(motion)

class Background(GameObject):
    def __init__(self,name,*args, **kwargs):
        super(Background, self).__init__(name = name,*args, **kwargs)
        self.x = 0
        self.y = 0
        
    def set_image(self,img):
        self.image = img

class Terminal(UIObject):
    def __init__(self,name,curr_state,world,*args,**kwargs):
        super(Terminal,self).__init__(name = name,
                                            curr_state = curr_state,
                                            world = world,
                                            *args,
                                            **kwargs)
        self.name = name
        self.opacity = 0
        #self.doc = pyglet.text.decode_text('player@sumon: Start Round'.ljust(50))
        text = 'admin@sumon:Start Round'+"\n"+"\n"
        self.doc = pyglet.text.document.UnformattedDocument(text)
        self.doc.set_style(0,len(self.doc.text),dict(color=(57, 255, 20, 255)))

        self.layout = ScrollableTextLayout(document = self.doc,
                                            width = self.width,
                                            height = self.height,
                                            multiline = True,
                                            batch = self.batch)

        self.layout.x,self.layout.y = self.x,self.y

    def add_message(self,name,msg):
        txt = name+"@sumon:"+msg+"\n"
        self.doc.insert_text(-1,txt)
        self.layout.view_y = -self.layout.content_height

class ReturnButton(UIObject):
    def __init__(self,name,curr_state,world,*args,**kwargs):
        super(ReturnButton,self).__init__(name = name,
                                            curr_state = curr_state,
                                            world = world,
                                            *args,
                                            **kwargs)
        self.name = name
        self.hand_cursor = world.window.get_system_mouse_cursor('hand')

    def hit_test(self,x,y):
        if x > self.x and x < (self.x + (self.width)):
            if y > self.y and y < (self.y + (self.height)):
                return True
        return False

    def get_mana_cost(self, words):
        if words[0] == 'summon':
            return Resources.stype[words[1].upper()][1]
        elif words[0] == 'move':
            return int(words[1])
            print mana_cost
        elif words[0] == 'special':
            return Resources.special_cards_det[words[1].upper()][0]

        return 0

    def command_exists(self, words):
        if len(words) < 3:
            return False

        command = words[0] + " " + words[1]
        if command in self.world.commands_list:
            self.world.commands_list.remove(command)
            return True

        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.hit_test(x,y):
            self.image = Resources.sprites['return_button2']
            
            if self.world.game_state == Resources.state['PROGRAMMING1']:
                terminal = self.world.find_widget('terminal')
                player1 = self.world.find_game_object('Player1')
                textx = self.world.find_widget('line_widget_1')

                words = textx.document.text.split(" ")
                mana_cost = self.get_mana_cost(words)

                if mana_cost <= player1.mana and len(textx.document.text) > 0 and self.command_exists(words):
                    player1.mana -= mana_cost
                    mana = self.world.find_label('mana')
                    mana.text = player1.get_mana_label()
                    self.world.commands1.append(textx.document.text + "\n")
                    terminal.add_message(player1.actual_name,textx.document.text)
                    textx.document.text = ""

            elif self.world.game_state == Resources.state['PROGRAMMING2']:
                terminal = self.world.find_widget('terminal')
                player2 = self.world.find_game_object('Player2')
                textx = self.world.find_widget('line_widget_2')

                words = textx.document.text.split(" ")
                mana_cost = self.get_mana_cost(words)

                if mana_cost <= player2.mana and len(textx.document.text) > 0 and self.command_exists(words):
                    player2.mana -= mana_cost
                    mana = self.world.find_label('mana')
                    mana.text = player2.get_mana_label()
                    self.world.commands2.append(textx.document.text + "\n")
                    terminal.add_message(player2.actual_name,textx.document.text)
                    textx.document.text = ""
                
    def on_mouse_release(self,x,y,button,modifiers):
        if button == mouse.LEFT and self.hit_test(x,y):
            self.image = Resources.sprites['return_button']

    def on_mouse_motion(self, x, y, dx, dy):
        if self.active and self.world.game_state == Resources.state[self.curr_state]:
            if self.hit_test(x,y):
                #print "Entering Button:",self.name
                self.world.window.set_mouse_cursor(self.hand_cursor)
