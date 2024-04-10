from manim import *
import numpy as np 
import streamlit as st
config.quality ="low_quality"
class MyCone(ThreeDScene):
    def construct(self):
# 
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        shape_color = GREEN
        axes = ThreeDAxes()
        sections = 10
        angle_start = 0
        angle_range = np.pi/2
        # set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        lines=[]
        self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")
        # make a list of the poly points that we will use to replace the lines extending from z axis
        poly_points = []
        # we need to move up the z axis and stick lines out from it
        for i in range(sections):
            # we will use the height as the radius amount
            # do I have it right that r will be sqrt(1-z**2)
            z = i/sections
            r = z
            s =(0,0,z)
            e =(0,r,z)
            if i ==0:
                poly_points.append(s)
                poly_points.append(e)
            if i == sections-1:
                poly_points.append(e)
                poly_points.append(s)
            self.add(Line(start=s,end=e,color = shape_color))
            self.wait(.08)
        self.wait(2)
        # ensure it is a filled color
        # TODO consider using unfilled rotated shapes to avoid the overdrawing issue
        p = Polygon(*poly_points,fill_opacity = 1)
        p.set_fill(shape_color)
        self.add(p)
        self.wait(3)
        for i in range(sections):
            theta = i/sections*2*PI
            p = Polygon(*poly_points,color=shape_color)
            p.rotate(angle=theta,about_point=ORIGIN,axis=np.array([0,0,1]))
            self.add(p)
            self.wait(.8)
        self.wait(3)
        # replace with the cone now
        c = Cone(base_radius=1,height=1,direction=np.array([0,0,-1]),checkerboard_colors=[shape_color,shape_color])
        self.add(c)
        self.wait(2)



c = MyCone()
c.render()
st.video("media/videos/480p15/Cone.mp4")
config.max_files_cached=800