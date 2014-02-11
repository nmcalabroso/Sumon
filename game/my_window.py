class MyWindow(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super(MyWindow,self).__init__(*args,**kwargs)
        self.focus = None
        self.set_focus(self.widgets[0])

    def set_focus(self, focus):
        if self.focus:
            self.focus.caret.visible = False
            self.focus.caret.mark = self.focus.caret.position = 0
        self.focus = focus
        if self.focus:
            self.focus.caret.visible = True
            self.focus.caret.mark = 0
            self.focus.caret.position = len(self.focus.document.text)

