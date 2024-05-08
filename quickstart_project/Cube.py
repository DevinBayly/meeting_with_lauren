from manim import *
import numpy as np 
import streamlit as st

config.max_files_cached=800
config.quality = "low_quality"

class CubeExample(ThreeDScene):
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

        #INTRO FRAME
        intro_text = Text("""Lets find the volume of this cube
        using integration""")
        intro_text.to_corner(UP)
        self.add_fixed_in_frame_mobjects(intro_text)
        self.add(intro_text)
        self.wait(0.1)


        fmla_1 = Tex(r"$\int_{0}^{2}$",r"$\int_{0}^{2}$",r"$\int_{0}^{2} 1 dx$",r"$dy dz$", font_size=70)
        fmla_1.next_to(intro_text,DOWN*2)
        fmla_1.move_to(RIGHT*2)

        
        cube = Cube(side_length=2, fill_opacity=1, fill_color=BLUE, 
        stroke_width=0)
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        cube.next_to(fmla_1,LEFT*12)
        self.add(cube)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(fmla_1)
        self.wait(3)
        self.remove(cube,intro_text)
        self.wait(1)


        #FRAME TWO
        fmla_1.generate_target()
        fmla_1.target.shift(2*UP,LEFT*2)
        self.play(MoveToTarget(fmla_1))
        fmla_1[2].set_color(GREEN)
        self.wait(2)


        fmla_2 = Tex(r"$\int_{0}^{2}$",r"$\int_{0}^{2}$",r"$x\rvert_{0}^{2}$",r"$dydz$", font_size=85)
        fmla_2.next_to(fmla_1,DOWN)
        self.add_fixed_in_frame_mobjects(fmla_2)
        fmla_2[2].set_color(GREEN)
        self.wait(3)

        fmla_3 = Tex(r"$\int_{0}^{2}$",r"$\int_{0}^{2}$", r"2",r"$dy$",r"$dz$", font_size=85)
        fmla_3.next_to(fmla_2,DOWN)
        self.add_fixed_in_frame_mobjects(fmla_3)
        fmla_3[2].set_color(GREEN)
        self.wait(2)




        #FRAME THREE
        self.remove(fmla_1,fmla_2)
        fmla_3.generate_target()
        fmla_3.target.shift(UP*2,RIGHT*2).scale(.7)
        self.play(MoveToTarget(fmla_3))
        self.wait(2)

        self.axes = axes
        self.add(axes)
        axes.next_to(fmla_3,UP)
        axes.move_to(LEFT*2)
        self.add(axes)
        self.wait(2)
        shape_color = GREEN
        line = Line(start=axes.c2p(0,0,0), end=axes.c2p(2,0,0),color=shape_color)
        self.add(line)
        self.wait(2)

        
        # FRAME FOUR


        fmla_3[1:4].set_color(ORANGE)
        self.wait(2)
        slices = 20
        lines = []
        shape_color = ORANGE
        for i in range(0,slices+1):

            line = Line(start=axes.c2p(x_start,y_start+i*.1,0), end=axes.c2p(x_end,y_end+i*.1,0),color=shape_color)
            lines.append(line)
            line.set_stroke(color=ORANGE, width=2)
            self.add(line)
            # note we can't go belo .066 because our default frame rate is 1/15 because we are doing 15fps ffmpeg
            self.wait(0.2)

        # FRAME FIVE

        fmla_5 = Tex(r"$\int_{0}^{2}$",r"$2y\rvert_{0}^{2}$",r"$dz$", font_size=85)
        self.add_fixed_in_frame_mobjects(fmla_5)
        fmla_5[1].set_color(ORANGE)
        fmla_5.next_to(fmla_3,DOWN)
        self.wait(2)

        fmla_6 = Tex(r"$\int_{0}^{2}$",r"4",r"$dz$", font_size=85)
        self.add_fixed_in_frame_mobjects(fmla_6)
        fmla_6[1].set_color(ORANGE)
        fmla_6.next_to(fmla_5,DOWN)
        self.wait(2)
        self.remove(fmla_3,fmla_5)

        fmla_6.generate_target()
        fmla_6.target.shift(UP*4,RIGHT*2).scale(.7)
        self.play(MoveToTarget(fmla_6))
        self.wait(1)

        self.move_camera(phi=70 * DEGREES, theta=45 * DEGREES,frame_center=axes.c2p(-2,0,0))


        # #FRAME SIX
        sqr = Polygon(axes.c2p(0, 0, 0), axes.c2p(0, 2, 0), axes.c2p(2, 2, 0),axes.c2p(2, 0, 0), 
            fill_opacity=1, fill_color=ORANGE, stroke_width=0)
        self.add(sqr)
        self.wait(1)
        fmla_6[0:3].set_color(PINK)
        self.wait(2)


        slices = 13
        side = 2
        squares = []
        shape_color = PINK
        for i in range(0,slices+1):
            sqr = Polygon(axes.c2p(0, 0, 0), axes.c2p(0, 2, 0), axes.c2p(2, 2, 0),axes.c2p(2, 0, 0), 
            fill_opacity=1, fill_color=PINK, stroke_width=0).shift(i*0.1*OUT)
            squares.append(sqr)
            sqr.set_stroke(color=PINK, width=2)
            self.add(sqr)
            # note we can't go belo .066 because our default frame rate is 1/15 because we are doing 15fps ffmpeg
            self.wait(0.2)

        #FRAME SEVEN

        fmla_7 = Tex(r"$4\rvert_{0}^{2}$", font_size=85)
        self.add_fixed_in_frame_mobjects(fmla_7)
        fmla_7[0].set_color(PINK)
        fmla_7.next_to(fmla_6,DOWN)
        self.wait(2)

        fmla_8 = Tex(r"$(4(2)-4(0))$", font_size=85)
        self.add_fixed_in_frame_mobjects(fmla_8)
        fmla_8[0].set_color(PINK)
        fmla_8.next_to(fmla_7,DOWN)
        self.wait(2)

        fmla_9 = Tex("Volume = 8", font_size=85)
        self.add_fixed_in_frame_mobjects(fmla_9)
        fmla_9[0].set_color(BLUE)
        fmla_9.next_to(fmla_8,DOWN)
        self.wait(0.5)


        vertex_coords = [
            axes.c2p(0, 0, 0),                                                              axes.c2p(2, 0, 0),  
            axes.c2p(2, 2, 0),  
            axes.c2p(0, 2, 0),  
            axes.c2p(0, 0, 2),  
            axes.c2p(2, 0, 2),  
            axes.c2p(2, 2, 2),  
            axes.c2p(0, 2, 2),  
        ]
        faces_list = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [1, 2, 6, 5],
            [0, 3, 7, 4],
        ]
        fnl_cube = Polyhedron(vertex_coords, faces_list)
        fnl_cube.set_fill(opacity=1)
        self.add(fnl_cube)
        self.wait(3)



c = CubeExample()
c.render()
st.video("media/videos/480p15/CubeExample.mp4")

