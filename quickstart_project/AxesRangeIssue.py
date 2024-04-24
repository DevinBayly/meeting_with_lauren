from manim import *
import numpy as np 
import streamlit as st
config.quality = "low_quality"
class AxesRangeIssue(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(0,5,1),y_range=(0,5,1),z_range=(0,5,1))
        axes.scale(.5)
        self.axes = axes
        self.add(axes)
        # from axes get the scene coordinate for the point 0,0,0

        self.move_camera(phi=70 * DEGREES, theta=45 * DEGREES,frame_center=axes.c2p(0,0,0))
a = AxesRangeIssue()

a.render()
st.video("media/videos/480p15/AxesRangeIssue.mp4")