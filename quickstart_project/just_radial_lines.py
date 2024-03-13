from manim import *
import numpy as np 

class CreateCircle1(Scene):
    def construct(self):
# 
        circle = Circle()
        circle.set_fill(WHITE, opacity = 1.0)
        circle.set_stroke(color=WHITE, width=1)
        self.play(Create(circle))
        self.wait(1)
        print("addign in lines to fill 2d circle")
        sections = 101
        for i in range(0,sections+1):
            theta = np.pi*2/sections*i
            x = np.cos(theta)
            y=np.sin(theta)
            line = Line(start=(0,0,0), end=(x,y,0),color=RED)
            self.wait(.1)
            # self.play(Create(line))
            self.add(line)

        self.wait(1) 

        # slices = 12
        # for i in range(0,slices+1):
        #  disc = Circle().shift(i*0.1*OUT)
        #  disc.set_fill(GREEN, opacity=1.0)
        #  disc.set_stroke(color=WHITE, width=1)
        #  self.add(disc)
        #  self.wait(.01)



c = CreateCircle1()
config.max_files_cached=800
c.render()