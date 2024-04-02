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
        radius = 1
        shape_color = GREEN
        axes = ThreeDAxes()
        self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")
        sections = 10
        lines=[]
        angle_start = 0
        angle_range = np.pi
        # set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        for i in range(0,sections+1):
            theta = angle_start+ angle_range/sections*i
            z_start=inner_radii* np.cos(theta)
            y_start=inner_radii* np.sin(theta)
            z_end=outer_radii* np.cos(theta)
            y_end=outer_radii* np.sin(theta)
            line = Line(start=(0,y_start,z_start), end=(0,y_end,z_end),color=shape_color)
            self.wait(.08)
            # self.play(Create(line))
            self.add(line)
            lines.append(line)
        # replace circles with arcs
        first_disc = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
        first_disc.set_fill(shape_color, opacity=1.0)
        first_disc.set_stroke(color=WHITE, width=1)
        first_disc.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
        self.add(first_disc)
        ## want to try to rotate the discs for sphereical
        self.wait(2)
        print(first_disc.get_bottom())
        #first_disc.rotate(90,axis=np.array([1,0,0]))
        self.wait(2)
        ds =[]
        # TODO figure out how to not draw over the earlier ones with the last ones
        for i in range(0,sections+1):
            phi = angle_start+ angle_range/sections*i
            d = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
            d.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
            # TODO decide on direction?
            d.rotate(about_point=d.get_bottom(),axis=np.array([0,0,1]),angle=-phi)
            d.set_fill(shape_color, opacity=1.0)
            d.set_stroke(color=WHITE, width=1)
            ds.append(d)
            self.add(d)
            self.wait(.1)
        for d in ds:
            self.remove(d)
        self.play(Rotate(first_disc,about_point=first_disc.get_bottom(),axis=np.array([0,0,1]),angle=-2*PI,rate_func=linear))
        #  for rotation without animation https://blog.furas.pl/python-manim-basic-image-animations-in-manim-gb.html
        # the u goes around the theta dir, v is like phi
        s = Sphere(
            center=(0, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI/2],
            v_range=[0, PI]
        )
        self.add(s)
        self.remove(first_disc)
        self.wait(4)



c = SphereExample()

c.render()
st.video("media/videos/480p15/SphereExample.mp4")