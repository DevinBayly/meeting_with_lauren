import streamlit as st

# the layout makes sure that things don't get squished
# TODO update the project title
st.set_page_config(
    layout="wide",
    page_title="Project Title",
    page_icon="👋",
)
# make two collumns to start with, and then ignore the first one to get your buttons off to the right
top1,top2 = st.columns(2)
# TODO update the project title
top1.write("# Your Title of the project")
c1, c2, c3,c4 = top2.columns(4)

c1.markdown('<a href="/basic_shapes" target="_self"><button>Basic Shapes</button></a>', unsafe_allow_html=True)
c2.markdown('<a href="/advanced_shapes" target="_self"><button>Advanced Shapes</button></a>', unsafe_allow_html=True)
c3.markdown('<a href="/custom_shapes" target="_self"><button>Custom Shapes</button></a>', unsafe_allow_html=True)
c4.markdown('<a href="/additional_resources" target="_self"><button>Additional Resources</button></a>', unsafe_allow_html=True)
# TODO consider adding in a About Me page





# using the """ allows you to make multiple line strings in python
st.write("""
## Introduction Welcome Statement
[title] is an interactive tool designed for students to build intuition with multi-dimensional integration. Our videos utilize Manim Animation to help users make connections between integrals on paper and integrals in 3D space. 
""")
st.markdown("---")
c1,c2 = st.columns(2)


c1.video("HelloLaTeX.mp4")
c2.markdown("""
### Iterated integral overview
""")
