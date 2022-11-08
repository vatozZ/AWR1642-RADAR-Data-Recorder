import matplotlib.pyplot as plt
import scipy.io
import os
import subprocess
import time as tm
awr_data = scipy.io.loadmat('awr_data.mat')['awr_cell']

awr_data = awr_data[1:][:]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

fig_counter = 0

for zk in awr_data:

    zk_x, zk_y, zk_z = zk[0][0][0][0],  zk[1][0][0][0],  zk[2][0][0][0]

    ax.scatter(zk_x, zk_y, zk_z)
    max_range = 5
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    """plt.pause()
    plt.clf()"""
    plt.title("AWR1642 Radar Detections")
    plt.pause(0.1)

    #plt.savefig(os.getcwd() + "/file%02d.png" % fig_counter)
    plt.cla()
    fig_counter += 1
