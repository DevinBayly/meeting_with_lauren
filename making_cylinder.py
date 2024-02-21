from manim import *
import streamlit as st
import numpy as np

class MyCylinder(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = Cylinder(fill_color=RED,radius=2, height=3)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait()
        self.add(axes, cylinder)

        # self.next_section("first section")
        

        

st.title('Bare bones')
# config.save_sections = True
# config.renderer = "opengl"
c = MyCylinder()

c.render()
st.video("media/videos/1080p60/MyCylinder.mp4")
