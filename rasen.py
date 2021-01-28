import bion
import data
import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import csv
filename="seedcheck.csv"


#dataset
focus=40
lamda=0.365
space=lamda/2
size=0.1
x0=-30
y0=-30
z0=0
zend=50
i=0
j=0
NA=0.6
z=0
intparamater=0.002
field = 64
def phasefct(z):
    #lamda=0.365
    ph=360*z/lamda
    while ph >360:
        ph = ph -360
    return ph
def NAfct(z):
    c1 = math.sin(field/2/(z)) 
    return c1
def intfunction(z):
    c2 = 0.95 - z*intparamater
    return c2

    
Azstart=data.Azstart
Azend=data.Azend
ntfftx=data.ntfftx
ntffty=data.ntffty
mdigital=data.mdigital
mult=data.m
bion_focus=data.bion_focus
fieldx=data.fieldx
fieldy=data.fieldy
field=data.fieldx
spacedensity=data.spacedensity
duplicateparamater=data.duplicateparamater
phasereverseparamater=data.phasereverseparamater
intparamater=data.intparamater
xstart=data.xstart
ystart=data.ystart
interpolate=data.interpolatenumber
size=data.size
space=field/(ntfftx*(interpolate+1))

zlength=Azend-Azstart

mseed=bion.spacenum(0,zlength,space)+1


with open('{0}'.format(filename), 'w') as f:
    f.write("x,y,z,int,size\n")
    while z < zend:
        x = 25*math.sin(math.radians(i))
        y = 25*math.cos(math.radians(i))
        z = z0 + i*size/2
        i=i+1

        f.write("{0}, {1}, {2}, 1,1\n".format(float(x),float(y),float(z)))
# i=0
# z=0
# while z < zend:
#     x_num = 0 - i*0.1
#     y_num = 0 + i*0.1
#     z = z0 + i*lamda/3
#     i=i+1
#     trans = 0.95 - z*0.02
#     phase = phasefct(z+focus)
#     f.write("rect {0} {1} {2} {3} {4} {5} {6} {7}\n".format(x_num, y_num, size, size, trans, phase, z, NA))
# i=0
# z=0
# while z < zend:
#     x_num = 0 - i*0.1
#     y_num = 0 - i*0.1
#     z = z0 + i*lamda/3
#     i=i+1
#     trans = 0.95 - z*0.02
#     phase = phasefct(z+focus)
#     f.write("rect {0} {1} {2} {3} {4} {5} {6} {7}\n".format(x_num, y_num, size, size, trans, phase, z, NA))

f.close()


# import numpy as np
# import csv
# import pandas as pd
# import shutil
# import plotly.graph_objects as go
# import plotly.express as px
# import csv

# shutil.copy('rasen2',filename)
# mask = pd.read_table(filename,  sep=" ",header=None)

# fnum=(len(mask))
# with open('rasen2raw.csv', 'w') as f:
#     f.write("x,y,z,int,size,symbol\n")
#     for i in range(0,fnum):
#         f.write("{0}, {1}, {2}, {3}, 1,virginica\n".format(mask.iloc[i,1],mask.iloc[i,2],mask.iloc[i,7],mask.iloc[i,5]))
#     f.close()

# df_A = pd.read_csv('rasen2raw.csv')

# df = df_A



# fig = go.Figure(data=go.Scatter3d(
#     x=df['x'],
#     y=df['y'],
#     z=df['z'],
#     mode='markers',
#     marker=dict(
#         sizemode='diameter',
# 	line=dict(width=0),
#         sizeref=0.4,
#         size=df['size'],
#         color = df['int'],
#         colorscale=[[0, 'rgb(0,0,128)'], [0.5, 'yellow'], [1.0, 'red']],
#         colorbar_title = 'Light<br>Intensity',
#         opacity = 0.7,
#     )
# ))


# fig.update_layout(scene=dict(
#                   xaxis=dict(range=[-46,46], autorange=False),
#                   yaxis=dict(range=[-46,46], autorange=False),
#                   zaxis=dict(range=[60, -40], autorange=False),
#                   aspectratio=dict(x=1, y=1, z=1)
#                             )
#                  )
# fig.write_html("{0}.html".format(filename))

plot=bion.Change("seedcheck",filename)
plot.plot_csv()