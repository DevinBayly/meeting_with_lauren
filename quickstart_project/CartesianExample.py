from manim import *
import numpy as np 
import streamlit as st
config.quality = "low_quality"
class CartesianExample(ThreeDScene):
    def construct(self):
# 
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        shape_color = GREEN
        axes = ThreeDAxes()
        self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")
        sections = 10
        self.begin_ambient_camera_rotation(rate=-.2)

        # # lines=[]
        poly_points=[]
        angle_start = 0
        angle_range = np.pi/2
        # set up inner and outer radii
        for i in range(sections):

            partial = i/sections
            s = (0,partial,0)
            e = (1,partial,0)
            if i ==0:
                poly_points.append(s)
                poly_points.append(e)
            if i == sections-1:
                poly_points.append(e)
                poly_points.append(s)
            l = Line(start=s,end=e)
        #     self.add(l)
        #     self.wait(.08)
        # self.wait(3)
        p = Polygon(*poly_points,color=shape_color)
        p.set_fill(opacity=1)
        # self.add(p)
        # self.wait(3)
        # for i in range(sections):

        #     partial = i/sections
        #     p = Polygon(*poly_points,color=shape_color)
        #     p.shift((0,0,partial))
        #     # p.set_fill(opacity=1)
        #     self.add(p)
        #     self.wait(.08)
        # self.wait(3)
        box = Cube(side_length=1, fill_opacity=0.7, fill_color=shape_color)
        # TODO get the box to the right location
        box.move_to((.5,.5,.5))
        self.add(box)
        self.wait(4)
 

        




c = CartesianExample()
st.video("media/videos/480p15/CartesianExample.mp4")
config.max_files_cached=800
c.render()
