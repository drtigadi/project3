import kivy
from kivy.app import App
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import Ellipse, Rectangle
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget

class DisparityDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ballSize=dp(50)
        self.rectsize=dp(100)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.BackGround = Rectangle(pos=(0,0),size=(self.rectsize,self.rectsize))
            Color(1,0,0,1)
            self.theBouncingBall = Ellipse(pos=(self.width/2,self.height/2),size =(self.ballSize,self.ballSize))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self,*args):#this funciton is written becase default size of canvas is 100*100 when done from code
        #print("on size : "+ str(self.width) +","+str(self.height))
        self.theBouncingBall.pos = (self.center_x-self.ballSize/2,self.center_y-self.ballSize/2)
        self.BackGround.size=(self.width,self.height)
    def update(self,dt):
        #print("Moved")
        x, y = self.theBouncingBall.pos

        if (x + self.ballSize >= self.width):
            self.vx = self.vx * (-1)
        if (x <= 0):
            self.vx = self.vx * (-1)
        if (y + self.ballSize >= self.height):
            self.vy = self.vy * (-1)
        if (y <= 0):
            self.vy = self.vy * (-1)

        x += self.vx
        y += self.vy

        self.theBouncingBall.pos = (x, y)
        #print(kivy.__version__)

class bounce(App):
    pass

bounce().run()