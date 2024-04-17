from manim import *
import numpy as np 
import streamlit as st
config.quality = "low_quality"
config.max_files_cached=800
class Wedge(ThreeDScene):
    def construct(self):
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        shape_color = GREEN
        axes = ThreeDAxes()
        self.add(axes)
        # TODO figure out how to move camera to the right location
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")
        # making the polygon for the formula -y+5
        # coordinates counter clockwise are xyz 0,0,5 5,0,5 5,5,0 0,5,0 this is the
        poly_points=[]
        poly_points.append((0,0,1))
        poly_points.append((1,0,1))
        poly_points.append((1,1,0))
        poly_points.append((0,1,0))
        p = Polygon(*poly_points)
        p.set_fill(opacity=1)
        self.add(p)
        self.wait(2)
        self.remove(p)
        self.wait()

        # start with drawing a vertical line, then a few polygons that extend from the z axis to the largest values of x
    def make_wedge_piece(self,pieces,top,yoffset):
        first_line = Line(start=poly_points[0],end=poly_points[1])
        self.add(first_line)
        self.wait(2)
        # pieces = 5
        for l in range(pieces):
            delta = 1/pieces
            s = (delta*l,0,1)
            s_lower = (*s[:2],0)
            e = (delta*l+delta,0,1)
            e_lower = (*e[:2],0)
            poly_points=[]
            poly_points.append(s)
            poly_points.append(s_lower)
            poly_points.append(e_lower)
            poly_points.append(e)
            p = Polygon(*poly_points,stroke_color=WHITE)
            p.set_fill(opacity=1,color=shape_color)
            self.add(p)
            self.wait()

        # then move to a new line and redo the process

        




c = Wedge()
c.render()
st.video("media/videos/480p15/Wedge.mp4")
