from manim import *
shape_color_1 = ORANGE
shape_color_2 = BLUE
shape_color_3 = GREEN
inner_radius = 0
outer_radius = 1
sections = 10
angle_start = 0
angle_range = np.pi


        # this is here for reference, it should be the actual form of the integration
        # r"""$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{2}\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$ \\
        # $\int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{2}\, d\phi\, d\theta$ \\ 
        # $\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{2^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ 
        # $\frac{8}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\ 
        # $\frac{8}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\ 
        # $\frac{8}{3}\int_{0}^{2\pi}d\theta$ \\ 
        # $\frac{8}{3}(\theta\rvert_{0}^{2\pi})$ \\ 
        # $\frac{16\pi}{3}$ \\ 


fmla_1 = Tex(r"$\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{1}$",r"$\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$", font_size=70)
fmla_2 = Tex(r"$= \int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{1}$",r"$\rho^{2} sin(\phi)d\rho\, d\phi\, d\theta$", font_size=70)
fmla_4 =Tex( r"""$= \int_{0}^{2\pi}\int_{0}^{\pi}\frac{\rho^{3}}{3} sin(\phi)\rvert_{0}^{1}\, d\phi\, d\theta$ \\ """,font_size=70)
fmla_5 = Tex( r"""$=\int_{0}^{2\pi}\int_{0}^{\pi}(\frac{1^{3}}{3} sin(\phi)) - (\frac{0^{3}}{3} sin(\phi)) d\phi\, d\theta$ \\ """,font_size=70)
# this is the last step of the integration for the first part
fmla_6 = Tex( r"=$\int_{0}^{2\pi}$",r"$\int_{0}^{\pi}\frac{1}{3} sin(\phi)\, d\phi$",r"$\, d\theta$ \\ ",font_size=70)
# the upper right formula
fmla_ur_1 = fmla_6
fmla_7 = Tex( r"$\frac{1}{3}\int_{0}^{2\pi}-cos(\phi)\rvert_{0}^{\pi}\, d\theta$ \\" ,font_size = 70)
fmla_8 = Tex( r"$\frac{1}{3}\int_{0}^{2\pi}-(0) + (1) d\theta$ \\" ,font_size = 70)
# this is basically the last step of the integration
fmla_9 = Tex( r"$\frac{1}{3}\int_{0}^{2\pi}d\theta$ \\" ,font_size = 70)
fmla_ur_2 = fmla_9
