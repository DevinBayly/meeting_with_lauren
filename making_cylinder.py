from manim import *
import streamlit as st
import numpy as np

class AnotherTest(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        print("made change")
        cylinder = Cylinder(fill_color=RED,color=RED,radius=2, height=3,resolution=2,stroke_width=.05,checkerboard_colors=False)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, cylinder)
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen 

        # self.next_section("first section")
        

        


st.title('Bare bones')
# config.save_sections = True
# config.renderer = "opengl"
c = AnotherTest()
c.render()
st.video("media/videos/1080p60/AnotherTest.mp4")
