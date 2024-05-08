from manim import *
import numpy as np 
import streamlit as st
# import particular combination of parameters as the sphere parameters
import sphere_parameters.sp1 as sp
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
        axes = ThreeDAxes()

        intro_text = Text("""Lets find the volume of this Sphere
using integration""")
        intro_text.to_corner(UP)
        self.add_fixed_in_frame_mobjects(intro_text)
        # TODO see if we can make the bounds smaller fonts
        # move to the up right corner
        sp.fmla_1.to_edge(RIGHT)
        self.add(intro_text)
        self.wait(2)
        self.add(sp.fmla_1)
        intro_sphere = Sphere()
        intro_sphere.to_edge(LEFT)
        # TODO make the shape rotate correctly
        #intro_sphere.rotate()
        self.add(intro_sphere)
        self.wait(2)


        # remove the text and shape
        self.remove(intro_sphere)
        self.remove(intro_text)
        # move the formula to the center top
        self.wait(2)
        self.remove(sp.fmla_1)
        # self.add(sp.fmla_2)
        # TODO figure out why this is suddenly back in the scene even if we wanted to remove it
        sp.fmla_2.to_edge(UP)
        self.add(sp.fmla_2)
        self.wait(2)
        # perform the on screen integration
        # TODO IMPORTANT GET THE RIGHT INTEGRATION FROM LAUREN
        # make use of the & sign to ensure that the alignment stays correct




        # TODO think about renaming the formulas by the lines that they go up to in the derivation
        # TODO shift formula names down by 1 index
        sp.fmla_4.next_to(sp.fmla_2,DOWN)
        # this is how to add it in to the scene with an animation
        self.play(Write(sp.fmla_4))

        self.wait(2)


        sp.fmla_5.next_to(sp.fmla_4,DOWN)
        self.play(Write(sp.fmla_5))
        self.wait(2)

        sp.fmla_6.next_to(sp.fmla_5,DOWN)
        self.play(Write(sp.fmla_6))
        self.wait(2)

        self.remove(sp.fmla_2)
        self.remove(sp.fmla_4)
        self.remove(sp.fmla_5)
        # self.remove(sp.fmla_6)
        sp.fmla_6.generate_target()
        sp.fmla_6.target.to_edge(UR)
        ### TODO ask lauren if this is the right time to be pausing in the animation so that we can draw the axes and stuff
        ## remove the formulas from the previous phase of multiline integration
        # TODO check whether this will be stable even if the camera 
        self.play(MoveToTarget(sp.fmla_ur_1))
        # possible work around, is do the above, then do the line underneath
        self.add_fixed_in_frame_mobjects(sp.fmla_ur_1)
        self.wait(2)
        self.add(axes)
        # add in the axes and draw a first line of the spoke that come down the rho


        ##self.begin_ambient_camera_rotation(rate=-.2)
        ophi = self.camera.get_phi()
        ogamma = self.camera.get_gamma()
        otheta = self.camera.get_theta()
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        #print("addign in lines to fill 2d circle")
        sp.fmla_ur_1[1].set_color(sp.shape_color_1)
        lines=[]
        ### set up inner and outer radii
        # TODO recall when the colors need to change to blue
        for i in range(0,sp.sections+1):
            theta = sp.angle_start+ sp.angle_range/sp.sections*i
            z_start=sp.inner_radius* np.cos(theta)
            y_start=sp.inner_radius* np.sin(theta)
            z_end=sp.outer_radius* np.cos(theta)
            y_end=sp.outer_radius* np.sin(theta)
            line = Line(start=(0,y_start,z_start), end=(0,y_end,z_end),color=sp.shape_color_1)
            self.wait(.08)
            # self.play(Create(line))
            self.add(line)
            lines.append(line)
        # replace circles with arcs

        first_disc = AnnularSector(inner_radius= sp.inner_radius,outer_radius = sp.outer_radius,start_angle = sp.angle_start,angle=sp.angle_start+sp.angle_range )
        first_disc.set_fill(sp.shape_color_1, opacity=1.0)
        first_disc.set_stroke(color=WHITE, width=1)
        first_disc.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
        self.add(first_disc)
        # want to try to rotate the discs for sphereical
        #self.wait(2)
        #print(first_disc.get_bottom())
        ## TODO think about the timing on this, is it too long?
        
        self.remove(axes)
        self.remove(first_disc)
        shape_color = BLUE
        for l in lines:
            self.remove(l)

        self.move_camera(phi=ophi,theta=otheta)
        sp.fmla_ur_1.set_color(WHITE)
        sp.fmla_ur_1.generate_target()
        sp.fmla_ur_1.target.center()
        sp.fmla_ur_1.target.to_edge(UP)
        self.play(MoveToTarget(sp.fmla_ur_1))
        ## now we need to go back into the integration to do the next couple steps of this 
        # this moves the upper right back to the center
        self.wait(2)


        # making the integrations down the page now
        # TODO remove this temporary line when connecting to the moved upper right fmla
        sp.fmla_7.center()
        sp.fmla_7.to_edge(UP)
        sp.fmla_7.next_to(sp.fmla_ur_1,DOWN)
        self.play(Write(sp.fmla_7))
        self.wait(2)

        sp.fmla_8.next_to(sp.fmla_7,DOWN)
        self.play(Write(sp.fmla_8))
        self.wait(2)



        sp.fmla_9.next_to(sp.fmla_8,DOWN)
        self.play(Write(sp.fmla_9))
        self.wait(2)



        sp.fmla_ur_2.generate_target()
        sp.fmla_ur_2.target.to_edge(UR)
        self.remove(sp.fmla_ur_1)
        self.remove(sp.fmla_7)
        self.remove(sp.fmla_8)
        self.play(MoveToTarget(sp.fmla_ur_2))
        self.add_fixed_in_frame_mobjects(sp.fmla_ur_2)
        ## add back in the axes, and update our view
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.wait(2)
        # TODO add back in the coloration
        # sp.fmla_ur_2[1].set_color(sp.shape_color_2)
        self.wait(1)
        cam_theta = self.camera.get_theta()
        cam_phi = self.camera.get_phi()
        #calculate the x,y,z position, and then figure out sector order
        cam_x = np.cos(cam_theta)
        cam_y = np.sin(cam_theta)
        cam_z = np.cos(cam_phi)
        ds =[]
        # TODO figure out how to not draw over the earlier ones with the last ones
        # TODO think about repositioning the camera to prevent the overdrawing , either through explicit coords or ambient (lauren's suggestion)
        # TODO make sure to put in the orange annulus before it tries to add in all the rotated shapes
        for i in range(0,sp.sections+1):
            phi = sp.angle_start+ sp.angle_range/sp.sections*i
            # TODO figure out why we over rotated
            # TODO see if we can get all the way over to the 
            d = AnnularSector(inner_radius= sp.inner_radius,outer_radius = sp.outer_radius,start_angle = sp.angle_start,angle=sp.angle_start+sp.angle_range )
            d.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
            # TODO decide on direction?
            d.rotate(about_point=d.get_bottom(),axis=np.array([0,0,1]),angle=-phi)
            d.set_fill(sp.shape_color_2, opacity=1.0)
            d.set_stroke(color=WHITE, width=1)
            d_center = d.get_center()
            # distance to the shape from camera
            # use this for order
            distance = np.linalg.norm(np.array([cam_x,cam_y,cam_z]) - d_center)
            d.set_z_index(-distance)
            ds.append(d)
            self.add(d)
            self.wait(.1)
        self.wait(2)
        s = Sphere(
            center=(0, 0, 0),
            radius=1,
            resolution=(20, 20),
                checkerboard_colors=[shape_color,shape_color],
                fill_color=shape_color,
        #     u_range=[0.001, PI/2],
        #     v_range=[0, PI]
        )

        # change the formula to show the final volume amount
        self.add(s)
        for d in ds:
            self.remove(d)
        self.wait(1)
        #self.remove(first_disc)
        self.wait(4)


# system, if we put all the formulas together then we can also modify this easily ahead or outside of the code

c = SphereExample()

c.render()
st.video("media/videos/480p15/SphereExample.mp4")