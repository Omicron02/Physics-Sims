from vpython import *
from Vpython_tools import *
A1=sphere(pos=vector(0,0,0),v=vector(0,0,0),force=vector(0,0,0),radius=1.5,color=color.yellow,mass=200,make_trail=True,distance=0,fixed=True)
A2=sphere(pos=vector(-10,0,0),v=vector(3,-3,4),force=vector(0,0,0),radius=0.5,color=color.cyan,mass=4,make_trail=True,distance=0,fixed=False)
A3=sphere(pos=vector(3,0,-10),v=vector(0,-5,0),force=vector(0,0,0),radius=0.6,color=color.red,mass=4,make_trail=True,distance=0,fixed=False)

L=[]
#attach_arrow(A1,"force",scale=5e-1,color=color.green)
attach_arrow(A2,"force",scale=5e-1,color=color.green)
attach_arrow(A3,"force",scale=5e-1,color=color.green)
L.extend([A1,A2,A3])
dt=0.001
while True:
	rate(2000)
	for i in range(len(L)):
		F=vector(0,0,0)
		for j in range(len(L)):
			if i!=j and not L[i].fixed:
				F+=Gravity(L[i],L[j])
				L[i].force=F
				L[i].v+=L[i].force*dt/L[i].mass
				#move(L[i],L[i].v.x*dt,L[i].v.y*dt)
				L[i].pos+=L[i].v*dt
	