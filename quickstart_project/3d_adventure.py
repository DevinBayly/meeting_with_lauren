from manim import *
import numpy as np 

class CreateCircle1(ThreeDScene):
    def construct(self):
# 
        # self.next_section("first section")
        axes = ThreeDAxes()
        # circle = Circle()
        # slide =2
        # circle.set_fill(PINK, opacity=0.5)
        # line = Line()
# 
        # self.add(line)
        # self.wait(1)
        # self.play(Rotate(Line(), angle=2*PI, about_point= LEFT, rate_func=linear))
        # self.add(circle)
        # self.wait(1)
        # this section seems slow for some reason
        # print("adding cylinder")
        # self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        # cylinder = Cylinder()
        # self.play(Transform(circle,cylinder))
        # self.wait(1)

        # cylinder.generate_target()
        # cylinder.target.shift(slide*UP)
        # self.add(cylinder)
        # self.play(MoveToTarget(cylinder))
        # at this point we have generated a cylinder from the circle

        print("addign in lines to fill 2d circle")
        sections = 101
        for i in range(0,sections+1):
            theta = np.pi*2/sections*i
            x = np.cos(theta)
            y=np.sin(theta)
            line = Line(start=(0,0,0), end=(x,y,0))
            self.wait(.01)
            self.add(line)

        circle = Circle()
        circle.set_fill(WHITE, opacity = 1.0)
        circle.set_stroke(color=WHITE, width=1)
        self.add(circle)
        self.wait(1)


        slices = 12
        for i in range(0,slices+1):
         disc = Circle().shift(i*0.1*OUT)
         disc.set_fill(GREEN, opacity=1.0)
         disc.set_stroke(color=WHITE, width=1)
         self.add(disc)
         self.wait(.01)



c = CreateCircle1()
config.max_files_cached=800
c.render()