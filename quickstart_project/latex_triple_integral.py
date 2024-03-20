from manim import *
import streamlit as st

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"Hello \LaTeX ", font_size=144)
        self.add(tex)
        self.wait(3)
        self.remove(tex)
        tex2 = Tex(r"goodbye \LaTeX ", font_size=144)
        self.add(tex2)
        self.wait(3)


h = HelloLaTeX()
h.render()
st.video("media/videos/1080p60/HelloLaTeX.mp4")