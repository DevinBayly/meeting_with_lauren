from manim import *
import numpy as np 

class Cone(ThreeDScene):
    def construct(self):
# 
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        shape_color = GREEN
        axes = ThreeDAxes()
        sections = 10
        angle_start = 0
        angle_range = np.pi/2
        # set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        lines=[]
        self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")




c = Cone()
config.max_files_cached=800