from manim import *
import numpy as np 
import streamlit as st
config.max_files_cached=800
# for some reason has no effect
config.quality = 'low_quality'
class Order(ThreeDScene):
    def construct(self):
        radius =1
        axes = ThreeDAxes()
        sections = 10
        #lines=[]
        angle_start = 0
        angle_range = np.pi
        ### set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.wait(2)
        shape_color=GREEN
        self.wait(1)
        # so we need to use theta and phi to calculate the position in 3d
        cam_theta = self.camera.get_theta()
        cam_phi = self.camera.get_phi()
        #calculate the x,y,z position, and then figure out sector order
        cam_x = np.cos(cam_theta)
        cam_y = np.sin(cam_theta)
        cam_z = np.cos(cam_phi)


        for i in range(0,sections+1):
            phi = angle_start+ angle_range/sections*i
            d = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
            d.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
            # TODO decide on direction?
            d.rotate(about_point=d.get_bottom(),axis=np.array([0,0,1]),angle=-phi)
            d.set_fill(shape_color, opacity=1.0)
            d.set_stroke(color=WHITE, width=1)
            d_center = d.get_center()
            # distance to the shape from camera
            # use this for order
            distance = np.linalg.norm(np.array([cam_x,cam_y,cam_z]) - d_center)
            d.set_z_index(-distance)
            self.add(d)
            self.wait(.1)
        self.wait(2)
        print(type(self.camera))

c = Order()
c.render()
st.video("media/videos/480p15/Order.mp4")