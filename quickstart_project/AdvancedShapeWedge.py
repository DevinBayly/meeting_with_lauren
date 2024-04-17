from manim import *
import numpy as np 
# import streamlit as st
config.quality = "low_quality"
class Wedge(ThreeDScene):
    def construct(self):
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        shape_color = GREEN
        axes = ThreeDAxes(x_range=(-10,10,1),y_range=(-10,10,1),z_range=(-10,10,1))
        # axes = ThreeDAxes()
        self.add(axes)
        # TODO figure out how to move camera to the right location
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")
        # making the polygon for the formula -y+5
        # coordinates counter clockwise are xyz 0,0,5 5,0,5 5,5,0 0,5,0 this is the
        poly_points=[]
        poly_points.append((0,0,5))
        poly_points.append((5,0,5))
        poly_points.append((5,5,0))
        poly_points.append((0,5,0))
        p = Polygon(*poly_points)
        #p.set_fill(opacity=1)
        self.add(p)
        self.wait(2)

        




c = Wedge()
c.render()
# st.video("media/videos/480p15/Wedge.mp4")
config.max_files_cached=800
