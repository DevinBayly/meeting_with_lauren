from manim import *
import numpy as np 
import streamlit as st
config.max_files_cached=800
# for some reason has no effect
config.quality = 'low_quality'
# recall that we take on interation of the outer integral and do all the inner ones first
# so for this we will do all the radii rho's, then all the pi/2 to -pi/2 phi, then the full thetas,
# this amounts to being like a fan that sweeps around the axis that points up
class SphereExample(ThreeDScene):
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
        lines=[]
        angle_start = 0
        angle_range = np.pi/2
        # set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        #for i in range(0,sections+1):
        #    theta = angle_start+ angle_range/sections*i
        #    x_start=inner_radii* np.cos(theta)
        #    y_start=inner_radii* np.sin(theta)
        #    x_end=outer_radii* np.cos(theta)
        #    y_end=outer_radii* np.sin(theta)
        #    line = Line(start=(x_start,y_start,0), end=(x_end,y_end,0),color=shape_color)
        #    self.wait(.08)
        #    # self.play(Create(line))
        #    self.add(line)
        #    lines.append(line)
        # replace circles with arcs
        first_disc = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
        first_disc.set_fill(shape_color, opacity=1.0)
        first_disc.set_stroke(color=WHITE, width=1)
        self.add(first_disc)
        ## want to try to rotate the discs for sphereical
        self.wait(2)
        a = first_disc
        print(a.get_bottom())
        #first_disc.rotate(90,axis=np.array([1,0,0]))
        self.wait(2)
        self.play(Rotate(first_disc,about_point=a.get_bottom(),angle=2*PI,rate_func=linear))
        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        # self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.wait(2)
        #  for rotation without animation https://blog.furas.pl/python-manim-basic-image-animations-in-manim-gb.html



c = SphereExample()

c.render()
st.video("media/videos/480p15/SphereExample.mp4")