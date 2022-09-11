from vpython import *
import numpy as np

def make_grid():
	scene.background=color.white
	thickness=0.02
	dx,dy=1,1
	xmax,ymax,zmax=10,10,10
	x=-xmax
	y=-ymax
	z=-zmax
	while x<=xmax:
		y=-ymax
		curve(vector(x,y,0),vector(x,ymax,0),color=color.white,radius=thickness)
		x+=dx
	x=-xmax
	y=-ymax
	while y<=ymax:
		x=-xmax
		curve(vector(x,y,0),vector(xmax,y,0),color=color.black,radius=thickness)
		y+=dy


def Vec2d(start=None,end=None,mag=None,deg=None,i=None,j=None,color=color.green):
	"""3 modes of input:
		1. (start=(x1,y1),end=(x2,y2)) Plots tail at start and head at end.
		2. (mag=M,deg=θ) Plots from origin with angle as θ and magnitude as M
		3. (i=x,j=y) Plots from origin to (i,j)
		
		Attributes:
		Vector.angle, Vector.rad(gives angle in radians),Vector.x(gives x component),Vector.y(gives y component), Vector.mag(gives magnitude),Vector.vec(gives vector), Vector.start,Vector.end"""
	if start!=None:
		Start=vector(*start,0)
		End=vector(*end,0)
		V=End-Start
		Mag=sqrt(V.x**2+V.y**2)
		Deg=degrees(np.arctan2(V.y,V.x))
	elif magni!=None:
		x=magni*cos(radians(deg))
		y=magni*sin(radians(deg))
		Start=vector(0,0,0)
		End=vector(x,y,0)
		Mag=magni
		V=End-Start
		Deg=deg
	elif i!=None:
		Start=vector(0,0,0)
		End=vector(i,j,0)
		V=End-Start
		Deg=degrees(np.arctan2(i,j))
		Mag=sqrt(i**2+j**2)
	Vector=arrow(pos=Start,axis=End-Start,color=color,shaftwidth=0.2)
	Vector.angle=Deg
	Vector.rad=radians(Deg)
	Vector.x=V.x
	Vector.y=V.y
	Vector.mag=Mag
	Vector.vec=V
	Vector.start=Start
	Vector.end=End
	return Vector
	
	
def Vec3d(start=None,end=None,magni=None,deg3=None,i=None,j=None,k=None,color=color.green):
	if start!=None:
		Start=vector(*start)
		End=vector(*end)
		V=End-Start
		Mag=mag(V)
		Deg3=(degrees(np.arccos(V.x/Mag)),degrees(np.arccos(V.y/Mag)),degrees(np.arccos(V.z/Mag)))
	elif magni!=None:
		x=mag*cos(radians(deg3[0]))
		y=mag*cos(radians(deg3[1]))
		z=mag*cos(radians(deg3[2]))
		Start=vector(0,0,0)
		End=vector(x,y,z)
		V=End-Start
		Mag=magni
		Deg3=deg3
	elif i!=None:
		Start=vector(0,0,0)
		End=vector(i,j,k)
		V=End-Start
		Mag=mag(V)
		Deg3=(degrees(np.arccos(V.x/Mag)),degrees(np.arccos(V.y/Mag)),degrees(np.arccos(V.z/Mag)))
	Vector=arrow(pos=Start,axis=End-Start,color=color,shaftwidth=0.2)
	Vector.x=V.x
	Vector.y=V.y
	Vector.z=V.z
	Vector.angles=Deg3
	Vector.mag=Mag
	Vector.vec=V
	Vector.start=Start
	Vector.end=End
	Vector.rad=[radians(x) for x in Deg3]
	return Vector
		
		
def vadd(Vec1,Vec2,color):
	Vector=Vec2d(start=(Vec1.start.x,Vec1.start.y),end=(Vec2.end.x,Vec2.end.y),color=color)
	return Vector
	
	
def Vcomp(V,xcolor,ycolor):
	Xcomp=Vec2d(start=(V.start.x,V.start.y),end=(V.end.x,V.start.y),color=xcolor)
	Ycomp=Vec2d(start=(V.start.x,V.start.y),end=(V.start.x,V.end.y),color=ycolor)
	return Xcomp,Ycomp
	
	
def marker(x,y,color):
	Marker=sphere(pos=vector(x,y,0),radius=0.3,color=color,make_trail=False,initial_pos=vector(x,y,0),distance=0)
	return Marker
	
	
def move(obj,dx,dy,dz=0):
	obj.pos+=vector(dx,dy,dz)
	obj.distance+=sqrt(dx**2+dy**2+dz**2)
	
	
def displacement(obj):
	return sqrt((obj.pos.x-obj.initial_pos.x)**2+(obj.pos.y-obj.initial_pos.y)**2)
def distance(obj):
	return obj.distance
	
	
def cap(Vect):
	return Vect/(sqrt(Vect.x**2+Vect.y**2+Vect.z**2))
	
	
def mag(Vect):
	return sqrt(Vect.x**2+Vect.y**2+Vect.z**2)
	
	
G=1
def Gravity(obj1,obj2):
	r=obj2.pos-obj1.pos
	force=G*obj1.mass*obj2.mass/mag(r)**2*cap(r)
	return force
	
	
K=1
def Electricity(obj1,obj2):
#	print(obj1.pos,obj2.pos)
	r=obj1.pos-obj2.pos
#	print(r)
	force=K*obj1.q*obj2.q/mag(r)**2*cap(r)
	return force
	

def FieldDraw(FieldVect,start=None,end=None,everywhere=False,color=color.yellow):
	if everywhere:
		End=cap(FieldVect)*10
		Vec3d(start=(0,0,0),end=(End.x,End.y,End.z),color=color)
	else:
		centre=(start+end)/2
		box(pos=centre, length=end.x-start.x,width=end.z-start.z,height=end.y-start.y,color=color,opacity=0.3)
		Cap=cap(FieldVect)
		V=end-centre
		Vec=vector(centre.x+Cap.x*V.x,centre.y+Cap.y*V.y,centre.z+Cap.z*V.z)
		Vec3d(start=(centre.x,centre.y,centre.z),end=(Vec.x,Vec.y,Vec.z),color=color)

		
def ElectricFieldForce(obj,FieldVect,start=None,end=None,everywhere=False):
	force=vector(0,0,0)
	if everywhere:
		force=FieldVect*obj.q
	else:
		if (start.x<obj.pos.x<end.x or start.x>obj.pos.x>end.x) and (start.y<obj.pos.y<end.y or start.y>obj.pos.y>end.y) and (start.z<obj.pos.z<end.z or start.z>obj.pos.z>end.z):
			force=FieldVect*obj.q
	return force


def MagneticFieldForce(obj,FieldVect,start=None,end=None,everywhere=False):
	force=vector(0,0,0)
	if everywhere:
		force=obj.q*cross(obj.v,FieldVect)
	else:
		if (start.x<=obj.pos.x<=end.x or start.x>=obj.pos.x>=end.x) and (start.y<=obj.pos.y<=end.y or start.y>=obj.pos.y>=end.y) and (start.z<=obj.pos.z<=end.z or start.z>=obj.pos.z>=end.z):
			force=obj.q*cross(obj.v,FieldVect)
	return force
#b=sphere(pos=vector(0,0,0))