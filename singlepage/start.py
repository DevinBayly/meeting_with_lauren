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

option = st.selectbox(
    'select a shape for integration',
    ('Cone','Box','Sphere',"Wedge"))

st.write('You selected:', option)
if option == "Cone":
    st.video("Cone.mp4")
elif option == "Box":
    st.video("CartesianExample.mp4")
elif option == "Sphere":
    st.video("SphereExample(1).mp4")