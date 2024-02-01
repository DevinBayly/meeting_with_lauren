from manim import *
import streamlit as st

class CreateCircle(Scene):
    def construct(self):
        circle = Square()  # create a circle
        circle.set_fill(RED, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

st.title('Bare bones')

c = CreateCircle()
c.render()
st.video("media/videos/1080p60/CreateCircle.mp4")
