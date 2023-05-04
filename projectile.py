import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81 

def projectile_calculation(initial_velocity,theta,totat_distance):
    vx=[]
    vy=[]
    # convert theta to radian
    theta = np.deg2rad(theta)
    # time during rising 
    rising_time = (initial_velocity*np.sin(theta))/g
    # max height of the ball 
    max_height = (initial_velocity*np.sin(theta)*rising_time) - (0.5*g*rising_time*rising_time)
    # distance from the origin to max height
    distance_to_maxh = initial_velocity*np.cos(theta)*rising_time
    # distance from the max height to goal
    falling_distace = totat_distance - distance_to_maxh
    # time during rising 
    falling_time = falling_distace / (initial_velocity*np.cos(theta))
    # final height of the ball at goal
    final_h = max_height - (0.5*g*falling_time*falling_time)
    # array of distances to reach the max height ( 50 point )
    up_distance= np.linspace(0, distance_to_maxh, 50)
    # array of distances to reach the goal ( 50 point )
    down_distance = np.linspace(distance_to_maxh+1, totat_distance, 50)
    print(rising_time)
    print(max_height)
    print(distance_to_maxh)
    print(falling_distace)
    print(final_h)
    # calculate velocity in x direction and y direction during rising time
    for d in up_distance:
        t = d/(initial_velocity*np.cos(theta))
        x = initial_velocity*np.cos(theta)*t
        y = (initial_velocity*np.sin(theta)*t) - (0.5*g*t*t)
        vx.append(x)
        vy.append(y)

    # append the max heitgh axes
    maxX=initial_velocity*np.cos(theta)*rising_time
    vx.append(maxX)
    vy.append(max_height)

    # calculate velocity in x direction and y direction during falling time 
    for d in down_distance:
        t = d/(initial_velocity*np.cos(theta))
        x = initial_velocity*np.cos(theta)*t
        y = (initial_velocity*np.sin(theta)*t) - (0.5*g*t*t)
        vx.append(x)
        vy.append(y)

    return vx,vy,maxX,max_height

# to animate the plot
def update(num, x, y, line, circle):
    line.set_data(x[:num], y[:num])
    circle.center = x[num],y[num]
    line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])
    return line,circle

# annotate the max height
def annot_max_height(maxX,max_height, ax=None):
    text= "Maximum height={:.3f}".format(max_height)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.2", fc="w", ec="k", lw=0.02)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90")
    kw = dict(xycoords='data',textcoords="axes fraction",
                arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(maxX, max_height), xytext=(0.42,0.32), **kw)

# annotate the final height
def annot_final_height(x,y, ax=None):
    lastx = x[-1]
    lasty = y[-1]
    text= "Final height={:.3f}".format(y[-1])
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.4", fc="w", ec="k", lw=0.7)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(lastx, lasty), xytext=(0.42,0.42), **kw)
