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

        intro_text = Text("""Lets find the volume of this Sphere
using integration""")
        #intro_text.to_corner(UP)
        #self.add_fixed_in_frame_mobjects(intro_text)
        ## TODO see if we can make the bounds smaller fonts
        #fmla_1 = Tex(r"$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}$",r"$\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$", font_size=70)
        ## move to the up right corner
        #fmla_1.to_edge(RIGHT)
        #self.add(intro_text)
        #self.wait(2)
        #self.add(fmla_1)
        #intro_sphere = Sphere()
        #intro_sphere.to_edge(LEFT)
        ## TODO make the shape rotate correctly
        ##intro_sphere.rotate()
        #self.add(intro_sphere)
        #self.wait(2)


        ## remove the text and shape
        #self.remove(intro_sphere)
        #self.remove(intro_text)
        ## move the formula to the center top
        #self.wait(2)
        #self.remove(fmla_1)
        #fmla_2 = Tex(r"$= \int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}$",r"$\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$", font_size=70)
        ## self.add(fmla_2)
        ## TODO figure out why this is suddenly back in the scene even if we wanted to remove it
        #fmla_2.to_edge(UP)
        #self.add(fmla_2)
        #self.wait(2)
        # perform the on screen integration
        # TODO IMPORTANT GET THE RIGHT INTEGRATION FROM LAUREN
        # make use of the & sign to ensure that the alignment stays correct

        ## this is here for reference, it should be the actual form of the integration
        ## r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$ \\
        ## $\int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ 
        ## $\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{2^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ 
        ## $\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\ 
        ## $\frac{8}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\ 
        ## $\frac{8}{3}\int_{0}^{2\pi}d\theta$ \\ 
        ## $\frac{8}{3}(\theta\rvert_{0}^{2\pi})$ \\ 
        ## $\frac{16\pi}{3}$ \\ 



        # TODO think about renaming the formulas by the lines that they go up to in the derivation
        # ampersand!
        #fmla_4 =Tex( 
        #r"""$= \int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ """,font_size=70)
        ## TODO shift formula names down by 1 index
        #fmla_4.next_to(fmla_2,DOWN)
        ## this is how to add it in to the scene with an animation
        #self.play(Write(fmla_4))

        #self.wait(2)


        #fmla_5 = Tex(
        #r"""$=\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{2^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ """,font_size=70)
        #fmla_5.next_to(fmla_4,DOWN)
        #self.play(Write(fmla_5))
        #self.wait(2)

        #fmla_6 = Tex(
        #r"""=$\int_{0}^{2\pi}\int_{0}^{\pi}\frac{8}{3} sin(\phi)\, d\phi\, d\theta$ \\ 
        #""",font_size=70)
        #fmla_6.next_to(fmla_5,DOWN)
        #self.play(Write(fmla_6))
        #self.wait(2)

        #self.remove(fmla_2)
        #self.remove(fmla_4)
        #self.remove(fmla_5)
        ## self.remove(fmla_6)
        #fmla_6.generate_target()
        #fmla_6.target.to_edge(UR)
        #### TODO ask lauren if this is the right time to be pausing in the animation so that we can draw the axes and stuff
        #upper_right_fmla = fmla_6
        ### remove the formulas from the previous phase of multiline integration
        ## TODO check whether this will be stable even if the camera 
        #self.play(MoveToTarget(upper_right_fmla))
        ## possible work around, is do the above, then do the line underneath
        #self.add_fixed_in_frame_mobjects(upper_right_fmla)
        #self.wait(2)
        #self.add(axes)
        ## add in the axes and draw a first line of the spoke that come down the rho


        ###self.begin_ambient_camera_rotation(rate=-.2)
        #ophi = self.camera.get_phi()
        #ogamma = self.camera.get_gamma()
        #otheta = self.camera.get_theta()
        #self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        ##print("addign in lines to fill 2d circle")
        #shape_color=ORANGE
        ## upper_right_fmla[1].set_color(shape_color)
        sections = 10
        #lines=[]
        angle_start = 0
        angle_range = np.pi
        ### set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        ## TODO recall when the colors need to change to blue
        #for i in range(0,sections+1):
        #    theta = angle_start+ angle_range/sections*i
        #    z_start=inner_radii* np.cos(theta)
        #    y_start=inner_radii* np.sin(theta)
        #    z_end=outer_radii* np.cos(theta)
        #    y_end=outer_radii* np.sin(theta)
        #    line = Line(start=(0,y_start,z_start), end=(0,y_end,z_end),color=shape_color)
        #    self.wait(.08)
        #    # self.play(Create(line))
        #    self.add(line)
        #    lines.append(line)
        ## replace circles with arcs

        #first_disc = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
        #first_disc.set_fill(shape_color, opacity=1.0)
        #first_disc.set_stroke(color=WHITE, width=1)
        #first_disc.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
        #self.add(first_disc)
        ## want to try to rotate the discs for sphereical
        ##self.wait(2)
        ##print(first_disc.get_bottom())
        ### TODO think about the timing on this, is it too long?
        
        #self.remove(axes)
        #self.remove(first_disc)
        #shape_color = BLUE
        #for l in lines:
        #    self.remove(l)

        #self.move_camera(phi=ophi,theta=otheta)
        #upper_right_fmla[1].set_color(WHITE)
        #upper_right_fmla.generate_target()
        #upper_right_fmla.target.center()
        #upper_right_fmla.target.to_edge(UP)
        #self.play(MoveToTarget(upper_right_fmla))
        ### now we need to go back into the integration to do the next couple steps of this 
        ## this moves the upper right back to the center
        #self.wait(2)


        ## making the integrations down the page now
        fmla_7 = Tex(
        r"$\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\"
            ,font_size = 70)
        # TODO remove this temporary line when connecting to the moved upper right fmla
        fmla_7.center()
        fmla_7.to_edge(UP)
        # fmla_7.next_to(upper_right_fmla,DOWN)
        self.play(Write(fmla_7))
        self.wait(2)

        fmla_8 = Tex(
        r"$\frac{8}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\"
            ,font_size = 70)
        fmla_8.next_to(fmla_7,DOWN)
        self.play(Write(fmla_8))
        self.wait(2)



        fmla_9 = Tex(
        r"$\frac{8}{3}\int_{0}^{2\pi}d\theta$ \\"
            ,font_size = 70)
        fmla_9.next_to(fmla_8,DOWN)
        self.play(Write(fmla_9))
        self.wait(2)



        upper_right_fmla = fmla_9
        upper_right_fmla.generate_target()
        upper_right_fmla.target.to_edge(UR)
        self.remove(fmla_7)
        self.remove(fmla_8)
        self.play(MoveToTarget(upper_right_fmla))
        self.add_fixed_in_frame_mobjects(upper_right_fmla)
        ## add back in the axes, and update our view
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.wait(2)
        shape_color=GREEN
        # TODO add back in the coloration
        # upper_right_fmla[1].set_color(shape_color)
        self.wait(1)
        ds =[]
        # TODO figure out how to not draw over the earlier ones with the last ones
        # TODO think about repositioning the camera to prevent the overdrawing , either through explicit coords or ambient (lauren's suggestion)
        # TODO make sure to put in the orange annulus before it tries to add in all the rotated shapes
        for i in range(0,sections+1):
            phi = angle_start+ angle_range/sections*i
            # TODO figure out why we over rotated
            # TODO see if we can get all the way over to the 
            d = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
            d.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
            # TODO decide on direction?
            d.rotate(about_point=d.get_bottom(),axis=np.array([0,0,1]),angle=-phi)
            d.set_fill(shape_color, opacity=1.0)
            d.set_stroke(color=WHITE, width=1)
            ds.append(d)
            self.add(d)
            self.wait(.1)
        self.wait(2)
        ## self.play(Rotate(first_disc,about_point=first_disc.get_bottom(),axis=np.array([0,0,1]),angle=-2*PI,rate_func=linear))
        ##  for rotation without animation https://blog.furas.pl/python-manim-basic-image-animations-in-manim-gb.html
        ## the u goes around the theta dir, v is like phi
        ## 
        #s = Sphere(
        #    center=(0, 0, 0),
        #    radius=1,
        #    resolution=(20, 20),
        #        checkerboard_colors=[shape_color,shape_color],
        #        fill_color=shape_color,
        ##     u_range=[0.001, PI/2],
        ##     v_range=[0, PI]
        #)

        #self.add(s)
        #for d in ds:
        #    self.remove(d)
        #self.wait(1)
        #self.remove(first_disc)
        #self.wait(4)



c = SphereExample()

c.render()
st.video("media/videos/480p15/SphereExample.mp4")