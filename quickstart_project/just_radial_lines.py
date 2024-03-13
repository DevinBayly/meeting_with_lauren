from manim import *
import numpy as np 

class CreateCircle1(ThreeDScene):
    def construct(self):
# 
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        shape_color = GREEN
        axes = ThreeDAxes()
        self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")
        sections = 10
        lines=[]
        angle_start = 0
        angle_range = np.pi/2
        # set up inner and outer radii
        inner_radii =0
        outer_radii = radius
        for i in range(0,sections+1):
            theta = angle_start+ angle_range/sections*i
            x_start=inner_radii* np.cos(theta)
            y_start=inner_radii* np.sin(theta)
            x_end=outer_radii* np.cos(theta)
            y_end=outer_radii* np.sin(theta)
            line = Line(start=(x_start,y_start,0), end=(x_end,y_end,0),color=shape_color)
            self.wait(.08)
            # self.play(Create(line))
            self.add(line)
            lines.append(line)
        # replace circles with arcs
        first_disc = AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range )
        first_disc.set_fill(shape_color, opacity=1.0)
        first_disc.set_stroke(color=WHITE, width=1)
        self.add(first_disc)
        self.wait(3)
        for line in lines:
            self.remove(line)

# 
        self.remove(first_disc)
        slices = 12
        discs = []
        for i in range(0,slices+1):

            disc =  AnnularSector(inner_radius= inner_radii,outer_radius = outer_radii,start_angle = angle_start,angle=angle_start+angle_range ).shift(i*0.1*OUT)
            discs.append(disc)
            disc.set_fill(shape_color, opacity=1.0)
            disc.set_stroke(color=WHITE, width=1)
            self.add(disc)
            # note we can't go belo .066 because our default frame rate is 1/15 because we are doing 15fps ffmpeg
            self.wait(.068)
# 
        # attempt to make a cylinder that has it's bottom at the first circle's position, and it's top at the top of the last disc
        for x in discs:
            print(x.get_start(),x.get_end(),x.get_center())
        # create a cylinder that we are going to overlay on the shape
        # get the last disc
        # and get it's 3 component, the y height
        discs_height = discs[-1].get_center()[2]
        cyl = Cylinder(height = discs_height,radius=radius,v_range=[angle_start,angle_start+angle_range], checkerboard_colors=[shape_color,shape_color],fill_color=shape_color,resolution=(6,6),show_ends=False)
        cyl.align_to(discs[-1],OUT)
        self.add(cyl)
        self.wait(1)
        # stop short of the last one so that there's a cap
        for disc in discs[:-1]:
            self.remove(disc)
        self.wait(1)
        print("finished removing")




c = CreateCircle1()
config.max_files_cached=800