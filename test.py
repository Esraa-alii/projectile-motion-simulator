import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

initial_velocity=20
totat_distance=15
theta = 22
g=9.81

def projectile_calculation(initial_velocity,totat_distance,theta):
    vx=[]
    vy=[]
    theta = np.deg2rad(theta)
    # d  = np.linspace(0, totat_distance, 100)
    # t  = d/initial_velocity*np.cos(theta)
    rising_time = (initial_velocity*np.sin(theta))/g
    max_height = (initial_velocity*np.sin(theta)*rising_time) - (0.5*g*rising_time*rising_time)
    distance_to_maxh = initial_velocity*np.cos(theta)*rising_time
    falling_distace = totat_distance - distance_to_maxh
    falling_time = falling_distace / (initial_velocity*np.cos(theta))
    final_h = max_height - (0.5*g*falling_time*falling_time)


    up_distance= np.linspace(0, distance_to_maxh, 50)
    down_distance = np.linspace(distance_to_maxh+1, totat_distance, 50)

    # down_time = np.linspace(rising_time)
    print(rising_time)
    print(max_height)
    print(distance_to_maxh)
    print(falling_distace)
    print(final_h)



    for d in up_distance:
        t = d/(initial_velocity*np.cos(theta))
        x = initial_velocity*np.cos(theta)*t
        y = (initial_velocity*np.sin(theta)*t) - (0.5*g*t*t)
        vx.append(x)
        vy.append(y)

    maxX=initial_velocity*np.cos(theta)*rising_time
    vx.append(maxX)
    vy.append(max_height)

    for d in down_distance:
        t = d/(initial_velocity*np.cos(theta))
        x = initial_velocity*np.cos(theta)*t
        y = (initial_velocity*np.sin(theta)*t) - (0.5*g*t*t)
        vx.append(x)
        vy.append(y)

    return vx,vy,maxX,max_height
# final_x=initial_velocity*np.cos(theta)*falling_time
# vx.append(final_x)
# vy.append(final_h)


# print(vx)
# print(vy)

# plt.plot(vx, vy, label='first plot')
# plt.xlim(left=0)
# plt.ylim(bottom=0)


def annot_max_height(maxX,max_height, ax=None):
# xmax = maxX
    # ymax = y.max()
    text= "Maximum height={:.3f}".format(max_height)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.2", fc="w", ec="k", lw=0.02)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90")
    kw = dict(xycoords='data',textcoords="axes fraction",
                arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(maxX, max_height), xytext=(0.42,0.32), **kw)

def annot_final_height(x,y, ax=None):
    lastx = x[-1]
    lasty = y[-1]
    if(lasty < 0):
        lasty = 0
    text= "Final height={:.3f}".format(y[-1])
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.5", fc="gray", ec="white", lw=0.70)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90")
    kw = dict(xycoords='data',textcoords="axes fraction",
            arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(lastx, lasty), xytext=(0.42,0.42), **kw)

def update(num, x, y, line, circle):
    line.set_data(x[:num], y[:num])
    circle.center = x[num],y[num]
    line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])
    return line,circle

vx,vy,maxX,max_height=projectile_calculation(initial_velocity,totat_distance,theta)
 
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
ani = animation.FuncAnimation(fig, update, len(vx), fargs=[vx, vy, line, circle],
                              interval=25, blit=True)
annot_max_height(maxX,max_height)
annot_final_height(vx,vy)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()