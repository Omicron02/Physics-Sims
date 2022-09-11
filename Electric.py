from vpython import *
from Vpython_tools import *
E1=vector(0,2,0)
E2=vector(0,-3,0)
B1=vector(0,5,0)
B2=vector(0,-5,0)
Q1=sphere(pos=vector(-10,0,0),v=vector(10,0,0),force=vector(0,0,0),radius=0.5,color=color.red,mass=1,q=5,make_trail=True,distance=0,fixed=False)
Q2=sphere(pos=vector(10,0,0),v=vector(-10,0,0),force=vector(0,0,0),radius=0.5,color=color.blue,mass=1,q=-5,make_trail=True,distance=0,fixed=False)

Ee1=vector(5,5,5)
Es1=vector(-5,-5,-5)
Ee2=vector(-10,-15,-5)
Es2=vector(10,-20,5)
Bs1=vector(-10,-15,3)
Be1=vector(10,-7,-3)
Bs2=vector(-10,15,3)
Be2=vector(10,7,-3)
# Bs1=vector(-6,-6,-6)
# Be1=vector(5,3,5)
L=[]

FieldDraw(E1,start=Es1,end=Ee1)
FieldDraw(E2,start=Es2,end=Ee2)
FieldDraw(B1,start=Bs1,end=Be1,color=color.cyan)
FieldDraw(B2,start=Bs2,end=Be2,color=color.cyan)
# FieldDraw(B2,start=Bs2,end=Be2,color=color.cyan)
L.extend([Q1,Q2])
dt=0.001
t=1
while True:
	rate(100)
	for i in range(len(L)):

		F=ElectricFieldForce(L[i],E2,start=Es2,end=Ee2)+ElectricFieldForce(L[i],E1,start=Es1,end=Ee1)+MagneticFieldForce(L[i],B1,start=Bs1,end=Be1)+MagneticFieldForce(L[i],B2,start=Bs2,end=Be2)
		for j in range(len(L)):
			if i!=j and not L[i].fixed:
				F+=Electricity(L[i],L[j])
			L[i].force=F
			L[i].v+=L[i].force*dt/L[i].mass
				#move(L[i],L[i].v.x*dt,L[i].v.y*dt)
			L[i].pos+=L[i].v*dt
#	if F!=0:
	#	t+=dt
	t+=dt