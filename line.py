import bion
import data
import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import csv
filename="seedcheck.csv"


#size=0.1
lamda=0.365

x0=-30;y0=-30;z0=10
seedzend=45
NA=0.6
x=0;y=0;z=0
arg=10

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

# arrseed=np.zeros((ntfftx*2+1,ntffty*2+1,mseed))    
# arrT=np.zeros((data.ntfftx+1,data.ntffty+1,mseed))
zee=30
with open('{0}'.format(filename), 'w') as f:
    f.write("x,y,z,int,size\n")
    for j in range(0,1,1):
        loop1=bion.spacenum(-25,-10,space)
        loops=int(spacedensity)
        for i in range(0,loop1,loops):
            x = -25 + i*space
            y = j/50
            z = z0
            f.write("{0}, {1}, {2}, 1,1\n".format(float(x),float(y),float(z)))

        loop1=bion.spacenum(-10,10,space)
        loops=int(spacedensity)
        while z < zee:
            x = x+space
            #for j in range(bion.spacenum(-0.5,0.5,thresh)):
            y = j/50
            z = z+space
            f.write("{0}, {1}, {2}, 1,1\n".format(float(x),float(y),float(z)))

        zee=30
        x=0;y=0;i=0;z=0
        loop1=bion.spacenum(10,25,space)
        loops=int(spacedensity)
        for i in range(0,loop1,loops):
            x = 10 + i*space
            #for j in range(bion.spacenum(-0.5,0.5,thresh)):
            y = j/50
            z = zee
            f.write("{0}, {1}, {2}, 1,1\n".format(float(x),float(y),float(z)))
f.close()

plot=bion.Change("seedcheck",filename)
plot.plot_csv()