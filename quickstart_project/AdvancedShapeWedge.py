from manim import *
import numpy as np 
import streamlit as st
config.quality = "low_quality"
config.max_files_cached=800
class Wedge(ThreeDScene):
    def construct(self):
        # note that we can create radius and re-use it with all the parts of this
        # TODO set this up so that a range of the 0-2pi space can be represented at each step
        radius = 2
        self.shape_color = GREEN
        # TODO figure out how to not show the negative side, but have camera look at the right place
        #axes = ThreeDAxes(x_range=(0,5,1),y_range=(0,5,1),z_range=(0,5,1))
        axes = ThreeDAxes()
        self.axes = axes
        self.add(axes)


        # TODO figure out how to move camera to the right location

        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        print("addign in lines to fill 2d circle")

        # make some test text and see if we can position it to the right of the screen
        tex = Tex(r"$\int$",r"$\int$","-y + 5", font_size=100)
        tex.to_corner(UR)


        # keeps it from rotating when the camera moves
        self.add_fixed_in_frame_mobjects(tex)
        # add in the ability to turn the poly slices and lines off or modify, these are lists that we will update later
        self.slice_polys = []
        self.lines = []
        poly_points=[]
        # making the polygon for the formula -y+5
        # coordinates counter clockwise are xyz 0,0,5 5,0,5 5,5,0 0,5,0 this is the
        poly_points.append(self.axes.c2p(0,0,1))
        poly_points.append(self.axes.c2p(1,0,1))
        poly_points.append(self.axes.c2p(1,1,0))
        poly_points.append(self.axes.c2p(0,1,0))
        p = Polygon(*poly_points)
        p.set_fill(opacity=1)
        self.add_foreground_mobjects(p)
        self.wait(2)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES,zoom=2)
        ## self.remove(p)
        ## TODO make the fill gradual and animated
        p.set_fill(opacity=0)
        top_z = 1
        # TODO change back
        number_of_planes =1
        z_delta = top_z/number_of_planes
        sections = 5
        animate_drawing = True
        # TODO make the color of the segments only for the first pass through the plane
        # then for the other ones leave it alone
        for np in range(number_of_planes):
            z = top_z - z_delta*np
            y= -z + 1
            self.wait(.08)
            self.make_wedge_piece(sections,z,y,animate=animate_drawing)
            if np ==0:
                # do additional refine step
                sections=15
                animate_drawing = False
                self.make_wedge_piece(sections,z,y,animate=animate_drawing)
                self.wait(1)

        # make some test text and see if we can position it to the right of the screen
        self.remove(tex)
        tex = Tex(r"$\int$","-2y + 10", font_size=100)
        self.add_fixed_in_frame_mobjects(tex)
        ## TODO make the stroke color go away for all the drawn polygons
        #self.make_solid()
        #self.wait()
        #number_of_planes=20
        #z_delta = top_z/number_of_planes
        #for np in range(number_of_planes):
        #    z = top_z - z_delta*np
        #    y= -z + 1
        #    # self.wait(.08)
        #    self.make_wedge_piece(sections,z,y,animate=animate_drawing,plane_wait=.08,stroke_color=self.shape_color)
        #    # self.wait(1)
        #self.wait(2)


        ## start with drawing a vertical line, then a few polygons that extend from the z axis to the largest values of x
    def make_wedge_piece(self,pieces,top,yoffset,animate=True,plane_wait = .8,stroke_color=WHITE):
        first_line = Line(start=self.axes.c2p(0,yoffset,top),end=self.axes.c2p(1,yoffset,top))
        self.add(first_line)
        self.wait(plane_wait)
        self.lines.append(first_line)
        # pieces = 5
        # TODO make it so that it's optional to see the rectangles animate out
        for l in range(pieces):
            delta = 1/pieces
            # the rectangles that are drawn descendin from the line and iterating out from the x axis
            s = (delta*l,yoffset,top)
            # 
            s_lower = (*s[:2],0)
            e = (delta*l+delta,yoffset,top)
            e_lower = (*e[:2],0)
            poly_points=[]
            poly_points.append(self.axes.c2p(*s))
            poly_points.append(self.axes.c2p(*s_lower))
            poly_points.append(self.axes.c2p(*e_lower))
            poly_points.append(self.axes.c2p(*e))
            p = Polygon(*poly_points,stroke_color=stroke_color)
            p.set_fill(opacity=1,color=self.shape_color)
            self.add(p)
            self.slice_polys.append(p)
            if animate:
                self.wait(.08)

        # then move to a new line and redo the process
    def make_solid(self):
        # take the polygons that have a certain stroke color and turn that off
        for p in self.slice_polys:
            p.set_stroke(self.shape_color)
        




c = Wedge()
c.render()
st.video("media/videos/480p15/Wedge.mp4")
