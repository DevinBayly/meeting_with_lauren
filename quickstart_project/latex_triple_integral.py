from manim import *
import streamlit as st

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"$\int$",r"$\int$",r"$\int$", font_size=144)
        self.add(tex)
        labels = index_labels(tex)
        self.add(labels)
        self.wait(3)
        tex[0].set_color(RED)
        self.wait()
        tex[1].set_color(RED)
        self.wait()
        tex[2].set_color(RED)
        self.wait(3)
        self.remove(labels)
        self.remove(tex)
        self.wait()
        tex2 = Tex(r"goodbye \LaTeX ", font_size=144)
        self.add(tex2)
        self.wait(3)


h = HelloLaTeX()
h.render()
st.video("media/videos/1080p60/HelloLaTeX.mp4")

config.max_files_cached=800