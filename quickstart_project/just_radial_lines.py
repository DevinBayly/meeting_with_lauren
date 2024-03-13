from manim import *
import numpy as np 

class CreateCircle1(ThreeDScene):
    def construct(self):
# 
        # note that we can create radius and re-use it with all the parts of this
        plane = NumberPlane()
        self.add(plane)
        circle = Circle(radius =2)  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        self.play(Create(circle), Create(square))  # show the shapes on screen
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        square.shift(5*RIGHT,2*UP)
        self.wait(4)
        circle.align_to(square, UP)  # set the position
        self.wait(2)
        circle.align_to(square, LEFT)  # set the position
        self.wait(2)
        # axes = ThreeDAxes()
        # self.add(axes)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        # # print("addign in lines to fill 2d circle")
        # # sections = 10
        # # for i in range(0,sections+1):
        # #     theta = np.pi*2/sections*i
        # #     x = np.cos(theta)
        # #     y=np.sin(theta)
        # #     line = Line(start=(0,0,0), end=(x,y,0),color=RED)
        # #     self.wait(.08)
        # #     # self.play(Create(line))
        # #     self.add(line)

        # slices = 12
        # discs = []
        # for i in range(0,slices+1):
        #     disc = Circle().shift(i*0.1*OUT)
        #     discs.append(disc)
        #     # disc.set_fill(GREEN, opacity=1.0)
        #     # disc.set_stroke(color=WHITE, width=1)
        #     self.add(disc)
        #     # note we can't go belo .066 because our default frame rate is 1/15 because we are doing 15fps ffmpeg
        #     self.wait(.068)

        # # attempt to make a cylinder that has it's bottom at the first circle's position, and it's top at the top of the last disc
        # for x in discs:
        #     print(x.get_start(),x.get_end(),x.get_center())
        # # create a cylinder that we are going to overlay on the shape
        # # get the last disc
        # # and get it's 3 component, the y height
        # discs_height = discs[-1].get_center()[2]
        # cyl = Cylinder(height = discs_height, checkerboard_colors=[RED,RED],fill_color=RED,resolution=(6,6))
        # cyl.align_to(discs[-1],UP)
        # self.add(cyl)
        # self.wait(1)




c = CreateCircle1()
config.max_files_cached=800