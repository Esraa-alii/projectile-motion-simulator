import streamlit as st 
import projectile as projectile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

st.set_page_config(page_title="PROJSIM",layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.sidebar:
    st.image('logo.png')
    st.title('Parameters')
    # user inputs 
    initial_velocity = st.slider(label="initial velocity(m/s)",min_value=1, max_value=100, step=1)
    theta = st.slider(label="Theta(deg)",min_value=1, max_value=90, step=1)
    totat_distance = st.slider(label="Total distance(m)",min_value=5, max_value=100, step=1)

st.title('projectile motion simulation')
vx,vy,maxX,max_height=projectile.projectile_calculation(initial_velocity,theta,totat_distance)
xmin = vx[0]
ymin = vy[0]
xmax = max(vx)
ymax = max(vy)
xysmall = min(xmax,ymax)
maxscale = max(xmax,ymax)
fig, ax = plt.subplots()
line, = ax.plot(vx, vy, color='k')
circle = plt.Circle((xmin, ymin), radius=np.sqrt(xysmall),color='gray')
ax.add_patch(circle)
ani = animation.FuncAnimation(fig, projectile.update, len(vx), fargs=[vx, vy, line, circle],
                              interval=25, blit=True)
projectile.annot_max_height(maxX,max_height)
projectile.annot_final_height(vx,vy)
plt.xlim(left=0)
plt.ylim(bottom=0)
ani.save('output/projectile.gif')
boy_image, output = st.columns(2)
with boy_image:
    st.image("arts0653-PhotoRoom-removebg-preview.png")
with output:
    st.image("./output/projectile.gif")
