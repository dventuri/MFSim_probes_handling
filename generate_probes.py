import numpy as np

center = 0.5
pipe_radius = 0.3207
start = center - pipe_radius
stop = center + pipe_radius

n = 101
points = np.linspace(start, stop, n)

lines = ["line_0deg_WE",
         "line_15deg",
         "line_30deg",
         "line_45deg",
         "line_60deg",
         "line_75deg",
         "line_90deg_SN",
         "line_105deg",
         "line_120deg",
         "line_135deg",
         "line_150deg",
         "line_165deg"]

dx = 0.00078125
xs = [0.1+dx, 0.2, 0.3, 0.4, 0.5-dx]

angle = 0
for line in lines:
    line_array = np.zeros((n,4))
    line_array[:,0] = np.arange(1,n+1)

    for i in range(n):
        line_array[i,2] = (points[i]-center)*np.sin(np.deg2rad(angle))+center
        line_array[i,3] = (points[i]-center)*np.cos(np.deg2rad(angle))+center

    for x in xs:
        line_array[:,1] = x
        np.savetxt(line+'_'+str(round(x,1))+'.dat', line_array,
                   fmt=['%i', '%9.7e', '%20.18e', '%20.18e'],
                   header=str(n),
                   comments='')

    angle += 15
