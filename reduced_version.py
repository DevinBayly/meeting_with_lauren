from manim import *
import streamlit as st
import numpy as np

class CreateCircle(Scene):
    def construct(self):
        rand_xys = np.random.random((5,2)).tolist()
        print(rand_xys)
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
        # # range of theta is also an option
        sections = 100
        for i in range(0,sections+1):
            theta = np.pi*2/sections*i
            y = np.sin(theta)
            x = np.cos(theta)
            line = Line(start=(0,0,0),end=(x,y,0))
            self.wait(.1)
            self.add(line)

        # self.next_section("first section")
        

        

# st.title('Bare bones')
# config.save_sections = True
# config.renderer = "opengl"
c = CreateCircle()
c.render()
# st.video("media/videos/1080p60/CreateCircle.mp4")
