from manim import *
import streamlit as st
import numpy as np

class CreateCircle(Scene):
    def construct(self):
        rand_xys = np.random.random((5,2)).tolist()
        print(rand_xys)
        # range of theta is also an option
        for i in range(0,len(rand_xys)):
            rand_xy = rand_xys[i]
            line = Line(start=(0,0,0),end=(rand_xy[0],rand_xy[1],0))
            self.add(line)

        # self.next_section("first section")
        
        

# st.title('Bare bones')
# config.save_sections = True
# config.renderer = "opengl"
c = CreateCircle()
c.render()
# st.video("media/videos/1080p60/CreateCircle.mp4")
