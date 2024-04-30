from manim import *
import numpy as np 
import streamlit as st

config.max_files_cached=800
config.quality = "low_quality"

class Cube(ThreeDScene):
    def construct(self):
        # define objects 
        axes = ThreeDAxes(x_range=(0,5,1),y_range=(0,5,1),z_range=(0,5,1))
        axes.scale(.5)
        radius = 2
        sections =10
        shape_color = GREEN
        lines=[]
        x_start = 0
        y_start = 0
        x_end = 2
        y_end = 0

        # INTRO FRAME
        # intro_text = Text("""Lets find the volume of this cube
        # using integration""")
        # intro_text.to_corner(UP)
        # self.add_fixed_in_frame_mobjects(intro_text)
        # self.add(intro_text)

        # # TODO see if we can make the bounds smaller fonts
        # fmla_1 = Tex(r"$\int_{0}^{2}$",r"$\int_{0}^{2}$",r"$\int_{0}^{2}$",r" 1  dx",r"$dy dz$", font_size=70)
        # # move to the up right corner
        # fmla_1.next_to(intro_text,DOWN)
        # fmla_1.move_to(RIGHT*4)
        # self.add_fixed_in_frame_mobjects(fmla_1)
        # self.wait(2)

        # ## side_length not recognized?
        # # cube = Cube(side_length=2, fill_opacity=0.75, fill_color=ManimColor('#58C4DD'), 
        # # stroke_width=0,direction=np.array([0,1,0]))
        # # cube.scale(.5)
        # # cube.next_to(fmla_1,LEFT)
        # # self.add(cube)
        # # self.wait(2)
        # self.remove(intro_text)
        # self.remove(fmla_1)
        # # self.remove(cube)



        # # FRAME TWO
        # self.axes = axes
        # self.add(axes)
        # self.wait(2)
        # self.add(axes)
        # shape_color = ORANGE
        # line = Line(start=(-3,-3,0), end=(0,-3,0),color=shape_color)
        # self.add(line)
        # self.wait(2)

        
        # FRAME THREE
        # Fix this mess

        # self.remove(first_disc)
        # slices = 12
        # lines = []
        # for i in range(0,slices+1):

        #     line = Line(start=(x_start,y_start+i*.1,0), end=(x_end,y_end+i*.1,0),color=shape_color)
        #     lines.append(line)
        #     line.set_fill(shape_color, opacity=1.0)
        #     line.set_stroke(color=WHITE, width=1)
        #     self.add(line)
        #     # note we can't go belo .066 because our default frame rate is 1/15 because we are doing 15fps ffmpeg
        #     self.wait(1)

        




        # self.move_camera(phi=70 * DEGREES, theta=45 * DEGREES,frame_center=axes.c2p(0,0,0))

        # LATEX PIECES
        fmla_1 = Tex(r"$\int_{0}^{2}$",r"$\int_{0}^{2}$",r"$\int_{0}^{2}$",r"$\1dxdydz$", font_size=144)
        self.add(fmla_1)
        self.wait(2)

# \[ \int_{0}^{2}\int_{0}^{2}\int_{0}^{2} 1 \,dxdydz \]
# \[ \int_{0}^{2}\int_{0}^{2}\left. x \right|_{0}^{2}\,dxdydz \]
# \[ \int_{0}^{2}\int_{0}^{2}2dydz \]
# \[ \int_{0}^{2}\left. 2y \right|_{0}^{2}\,dz \]
# \[ \int_{0}^{2}4dz \]
# \[\left. 4z \right|_{0}^{2} \]
# \[4(2) - 4(0)\]
# \[8\]



c = Cube()
c.render()
st.video("media/videos/480p15/Cube.mp4")







# #         #fmla_1[2].set_color(shape_color)
# #         #fmla_1[3].set_color(shape_color)
# #         #fmla_1.to_corner(UR)
# #         #self.add_fixed_in_frame_mobjects(fmla_1)
# #         #self.wait(2)
# #         #self.remove(fmla_1)
# #         ## second step of the formula development
# #         #fmla_2 = Tex(r"$\int_{0}^{5}$",r"$\int_{0}^{2\pi}$",r"$\frac{1}{2}r^{2}  \vert_{0}^{2}$",r" $d\theta dz$", font_size=70)
# #         #fmla_2[2].set_color(shape_color)
# #         #fmla_2.move_to(fmla_1)
# #         #self.add_fixed_in_frame_mobjects(fmla_2)
# #         #self.wait(2)
# #         #self.remove(fmla_2)
# #         ## third step of the formula dev
# #         #fmla_3 = Tex(r"$\int_{0}^{5}$",r"$\int_{0}^{2\pi}$",r"$\frac{1}{2}(2)^{2} - \frac{1}{2}(0)^{2}$",r" $d\theta dz$", font_size=50)
# #         #fmla_3[2].set_color(shape_color)
# #         #fmla_3.move_to(fmla_1)
# #         #self.add_fixed_in_frame_mobjects(fmla_3)
# #         #self.wait(2)
# #         #self.remove(fmla_3)
# #         ## last formula step for this section
# #         #fmla_4 = Tex(r"$\int_{0}^{5}$",r"$\int_{0}^{2\pi}$",r"2",r" $d\theta dz$", font_size=70)
# #         #fmla_4[2].set_color(shape_color)
# #         #fmla_4.move_to(fmla_1)
# #         #self.add_fixed_in_frame_mobjects(fmla_4)
# #         #self.wait(2)
# #         #self.remove(fmla_4)
# #         # TODO remove the single line generated before that we had with all the equations
# #         # next part of the animation
# #         shape_color = BLUE
# #         fmla_5 = Tex(r"$\int_{0}^{5}$",r"$\int_{0}^{2\pi} 2 d\theta$",r"dz", font_size=70)
# #         fmla_5[1].set_color(shape_color)
# #         # very helpful positioning option
# #         fmla_5.to_edge(UR)
# #         self.add_fixed_in_frame_mobjects(fmla_5)
# #         # self.wait(2)


# #         # TODO consider how many lines we want to draw per quadrant, not sections total perhaps, with not enough sections this seems very sparse
# #         for i in range(0,sections+1):
# #             # TODO make the values use the axes c2p
# #             theta = angle_start+ angle_range/sections*i
# #             x_start=inner_radii* np.cos(theta)
# #             y_start=inner_radii* np.sin(theta)
# #             x_end=outer_radii* np.cos(theta)
# #             y_end=outer_radii* np.sin(theta)
# #             line = Line(start=(x_start,y_start,0), end=(x_end,y_end,0),color=shape_color)
# #             # TODO put this back in for aniimated spokes
# #             # self.wait(.08)
# #             # self.play(Create(line))
# #             self.add(line)
# #             lines.append(line)
# #         self.wait(2)
# #         self.remove(fmla_5)
# #         fmla_6 = Tex(r"$\int_{0}^{5}$",r"$ 2\theta \rvert_{0}^{2\pi}$",r"dz", font_size=70)
# #         fmla_6[1].set_color(shape_color)
# #         # very helpful positioning option
# #         fmla_6.to_edge(UR)
# #         self.add_fixed_in_frame_mobjects(fmla_6)
# #         self.wait(2)
# #         self.remove(fmla_6)
# #         fmla_7 = Tex(r"$\int_{0}^{5}$",r"$ 2(2\pi) - 2(0)$",r"dz", font_size=70)
# #         fmla_7[1].set_color(shape_color)
# #         # very helpful positioning option
# #         fmla_7.to_edge(UR)
# #         self.add_fixed_in_frame_mobjects(fmla_7)
# #         self.wait(2)
# #         self.remove(fmla_7)
# #         # replace circles with arcs
# #         fmla_8 = Tex(r"$\int_{0}^{5}$",r"$ 4\pi $",r"dz", font_size=70)
# #         fmla_8[1].set_color(shape_color)
# #         # very helpful positioning option
# #         fmla_8.to_edge(UR)
# #         self.add_fixed_in_frame_mobjects(fmla_8)
# #         self.wait(2)
# #         self.remove(fmla_8)
# #         first_disc = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
# #         first_disc.set_fill(shape_color, opacity=1.0)
# #         first_disc.set_stroke(color=WHITE, width=1)
# #         self.add(first_disc)
# #         self.wait(2)
# #         shape_color = PINK
# #         first_disc.set_fill(shape_color,opacity = 1.0)
# #         self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
# #         for line in lines:
# #             self.remove(line)

# #         # self.remove(first_disc)
# #         slices = 12
# #         discs = []
# #         # last set of fmlas
# #         self.remove(fmla_8)
# #         # replace circles with arcs
# #         fmla_9 = Tex(r"$\int_{0}^{5} 4\pi $",r"dz", font_size=70)
# #         fmla_9.set_color(shape_color)
# #         # very helpful positioning option
# #         fmla_9.to_edge(UR)
# #         self.add_fixed_in_frame_mobjects(fmla_9)
# #         self.wait(2)
# #         for i in range(0,slices+1):

# #             disc =  AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range ).shift(i*0.1*OUT)
# #             discs.append(disc)
# #             disc.set_fill(shape_color, opacity=1.0)
# #             disc.set_stroke(color=WHITE, width=1)
# #             self.add(disc)
# #             # note we can't go belo .066 because our default frame rate is 1/15 because we are doing 15fps ffmpeg
# #             self.wait(.068)
# # # 
# #         self.remove(fmla_9)
# #         # replace circles with arcs
# #         # TODO consider drawing all these "in back, so that the axes aren't covered?"
# #         fmla_9 = Tex(r"$ 4\pi \rvert_{0}^{5}$", font_size=70)
# #         fmla_9.set_color(shape_color)
# #         # very helpful positioning option
# #         fmla_9.to_edge(UR)
# #         self.add_fixed_in_frame_mobjects(fmla_9)
# #         self.wait(2)
# #         # attempt to make a cylinder that has it's bottom at the first circle's position, and it's top at the top of the last disc
# #         #for x in discs:
# #         #    print(x.get_start(),x.get_end(),x.get_center())
# #         ## create a cylinder that we are going to overlay on the shape
# #         ## get the last disc
# #         ## and get it's 3 component, the y height
# #         self.remove(first_disc)
# #         self.remove(fmla_9)
# #         fmla_10 = Tex("Volume  = ",r"$20\pi$",font_size = 70)
# #         fmla_10.to_edge(UR)
# #         fmla_10.set_color(shape_color)
# #         self.add_fixed_in_frame_mobjects(fmla_10)
# #         self.wait(2)
# #         discs_height = discs[-1].get_center()[2]
# #         cyl = Cylinder(height = discs_height,radius=radius,v_range=[angle_start,angle_start+angle_range], checkerboard_colors=[shape_color,shape_color],fill_color=shape_color,resolution=(6,6),show_ends=False)
# #         cyl.align_to(discs[-1],OUT)
# #         self.add(cyl)
# #         self.wait(1)
# #         # stop short of the last one so that there's a cap
# #         for disc in discs[:-1]:
# #             self.remove(disc)
# #         self.wait(1)
# #         print("finished removing")
