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
        intro_text.to_corner(UP)
        #self.add_fixed_in_frame_mobjects(intro_text)
        # TODO see if we can make the bounds smaller fonts
        fmla_1 = Tex(r"$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}$",r"$\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$", font_size=70)
        # move to the up right corner
        fmla_1.to_edge(RIGHT)
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
        #fmla_2 = Tex(r"$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}$",r"$\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$", font_size=70)
        ## self.add(fmla_2)
        #self.play(Transform(fmla_1,fmla_2))
        ## TODO figure out why this is suddenly back in the scene even if we wanted to remove it
        #self.remove(fmla_1)
        #fmla_2.generate_target()
        #fmla_2.target.to_edge(UP)
        #self.play(MoveToTarget(fmla_2))
        #self.wait(2)
        ## perform the on screen integration
        ## TODO IMPORTANT GET THE RIGHT INTEGRATION FROM LAUREN
        ## make use of the & sign to ensure that the alignment stays correct
        #self.remove(fmla_2)
#         fmla_3 = Tex(
# r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$ \\
# $\int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ 
# $\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{2^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ 
# $\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\ 
# $\frac{8}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\ 
# $\frac{8}{3}\int_{0}^{2\pi}d\theta$ \\ 
# $\frac{8}{3}(\theta\rvert_{0}^{2\pi})$ \\ 
# $\frac{16\pi}{3}$ \\ 
# """
# , font_size=70)
#        fmla_3 = Tex(
#r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$ \\""",font_size=70)
#        fmla_3.to_edge(UP)
#        self.add(fmla_3)
#        # TODO think about renaming the formulas by the lines that they go up to in the derivation
#        fmla_4 =Tex( 
#r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$  \\
#$\int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ """,font_size=70)
#        # TODO this seems too fancy for its own good, how can we fix?
#        fmla_4.to_edge(UP)
#        self.play(Transform(fmla_3,fmla_4))
#        self.add(fmla_4)
#        self.remove(fmla_3)
#
#        self.wait(2)
#        fmla_5 = Tex(
#r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$ \\
#$\int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ 
#$\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{2^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ """,font_size=70)
#        fmla_5.to_edge(UP)
#        self.play(Transform(fmla_4,fmla_5))
#        self.add(fmla_5)
#        self.remove(fmla_4)
#        self.wait(2)
#        fmla_6 = Tex(
#r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$ \\
#$\int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ 
#$\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{2^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ 
#$\int_{0}^{2\pi}\int_{0}^{\pi}\frac{8}{3} sin(\phi)\, d\phi\, d\theta$ \\ 
#""",font_size=70)
#        fmla_6.to_edge(UP)
#        self.play(Transform(fmla_5,fmla_6))
#        self.add(fmla_6)
#        self.remove(fmla_5)
#        self.wait(2)
        # TODO ask lauren if this is the right time to be pausing in the animation so that we can draw the axes and stuff
        upper_right_fmla = Tex(
r"$\int_{0}^{2\pi}$",r"$\int_{0}^{\pi}\frac{8}{3}sin(\phi)\, d\phi\,$",r"$ d\theta$ \\ "
            ,font_size = 70)
        upper_right_fmla.to_edge(UR)
        # self.remove(fmla_6)
        self.add_fixed_in_frame_mobjects(upper_right_fmla)
        self.wait(2)
        self.add(axes)
        ## add in the axes and draw a first line of the spoke that come down the rho


        ##self.begin_ambient_camera_rotation(rate=-.2)

        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        ##print("addign in lines to fill 2d circle")
        #shape_color=ORANGE
        #upper_right_fmla[1].set_color(shape_color)
        #sections = 10
        #lines=[]
        angle_start = 0
        angle_range = np.pi
        ## set up inner and outer radii
        inner_radii =0
        outer_radii = radius
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
        first_disc = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
        first_disc.set_fill(shape_color, opacity=1.0)
        first_disc.set_stroke(color=WHITE, width=1)
        first_disc.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
        self.add(first_disc)
        ## want to try to rotate the discs for sphereical
        self.wait(2)
        print(first_disc.get_bottom())
        #first_disc.rotate(90,axis=np.array([1,0,0]))
        # TODO think about the timing on this, is it too long?
        self.wait(2)#
        self.remove(axes)
        self.remove(first_disc)



        # now we need to go back into the integration to do the next couple steps of this 
        fmla_6 = Tex(
r"$\int_{0}^{2\pi}$",r"$\int_{0}^{\pi}\frac{8}{3}sin(\phi)\, d\phi\,$",r"$ d\theta$ \\ "
            ,font_size = 70)
        fmla_6.to_edge(UP)
        self.play(Transform(upper_right_fmla,fmla_6))
        self.add_fixed_in_frame_mobjects(fmla_6)
        self.remove(upper_right_fmla)
        self.wait(2)

        self.move_camera(theta = None,phi=None)
        # making the integrations down the page now
        fmla_7 = Tex(
r"$\int_{0}^{2\pi}$",r"$\int_{0}^{\pi}\frac{8}{3}sin(\phi)\, d\phi\,$",r"$ d\theta$ \\ ",
r"$\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\"
            ,font_size = 70)
        fmla_7.to_edge(UP)
        self.play(Transform(fmla_7,fmla_6))
        self.add_fixed_in_frame_mobjects(fmla_7)
        self.remove(fmla_6)
        self.wait(2)

        fmla_8 = Tex(
r"$\int_{0}^{2\pi}$",r"$\int_{0}^{\pi}\frac{8}{3}sin(\phi)\, d\phi\,$",r"$ d\theta$ \\ ",
r"$\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\",
r"$\frac{8}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\"
            ,font_size = 70)
        fmla_8.to_edge(UP)
        self.play(Transform(fmla_7,fmla_8))
        self.add_fixed_in_frame_mobjects(fmla_8)
        self.remove(fmla_7)
        self.wait(2)



        fmla_9 = Tex(
r"$\int_{0}^{2\pi}$",r"$\int_{0}^{\pi}\frac{8}{3}sin(\phi)\, d\phi\,$",r"$ d\theta$ \\ ",
r"$\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\",
r"$\frac{8}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\"
            ,font_size = 70)
        fmla_9.to_edge(UP)
        self.play(Transform(fmla_9,fmla_8))
        self.add_fixed_in_frame_mobjects(fmla_9)
        self.remove(fmla_8)
        self.wait(2)
#  
#  
# $\frac{8}{3}\int_{0}^{2\pi}d\theta$ \\ 




        #ds =[]
        ## TODO figure out how to not draw over the earlier ones with the last ones
        ## TODO think about repositioning the camera to prevent the overdrawing , either through explicit coords or ambient (lauren's suggestion)
        #for i in range(0,sections+1):
        #    phi = angle_start+ angle_range/sections*i
        #    # TODO figure out why we over rotated
        #    # TODO see if we can get all the way over to the 
        #    d = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
        #    d.rotate(PI/2,about_point=ORIGIN,axis=np.array([0,1,0]))
        #    # TODO decide on direction?
        #    d.rotate(about_point=d.get_bottom(),axis=np.array([0,0,1]),angle=-phi)
        #    d.set_fill(shape_color, opacity=1.0)
        #    d.set_stroke(color=WHITE, width=1)
        #    ds.append(d)
        #    self.add(d)
        #    self.wait(.1)
        #for d in ds:
        #    self.remove(d)
        #self.play(Rotate(first_disc,about_point=first_disc.get_bottom(),axis=np.array([0,0,1]),angle=-2*PI,rate_func=linear))
        ##  for rotation without animation https://blog.furas.pl/python-manim-basic-image-animations-in-manim-gb.html
        ## the u goes around the theta dir, v is like phi
        ## 
        #s = Sphere(
        #    center=(0, 0, 0),
        #    radius=1,
        #    resolution=(20, 20),
        #    u_range=[0.001, PI/2],
        #    v_range=[0, PI]
        #)
        #self.add(s)
        #self.remove(first_disc)
        #self.wait(4)



c = SphereExample()

c.render()
st.video("media/videos/480p15/SphereExample.mp4")