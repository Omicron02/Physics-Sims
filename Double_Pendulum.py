import vpython as vp
import numpy as np
from win32api import GetSystemMetrics
scene=vp.canvas(width=GetSystemMetrics(0)//2,height=GetSystemMetrics(1)//2,autoscale=True,align="left")
# scene.camera.pos=vp.vector(0,0,30)
# scene.center=vp.vector(0,0,0)
# scene.range=21
#help(vp.graph)
θ_t=vp.graph(xtitle="Time",ytitle="Angle",width=300,height=300,align="left")
θ_θ=vp.graph(xtitle="Angle 1",ytitle="Angle 2",width=300,height=300,align="left")
θ1=vp.gcurve(label="Theta 1",color=vp.color.blue,graph=θ_t)
θ2=vp.gcurve(label="Theta 2",color=vp.color.red,graph=θ_t)
θθ1=vp.gcurve(color=vp.color.black,graph=θ_θ)
def v(x,y):
	return vp.vector(x,y,0)
	
g=1
m1=1
m2=1
r1=10
r2=10
t1=0
t2=0
w1=0
w2=0
a1=0
a2=0

x1 = r1*np.sin(t1)
y1 = - r1*np.cos(t1)
x2 = x1 + r2*np.sin(t2)
y2 = y1 - r2*np.cos(t2)

p1=vp.sphere(pos=v(x1,y1),color=vp.color.blue,radius=m1**0.5,make_trail=False,retain=10,trail_type="points",interval=100)
p2=vp.sphere(pos=v(x2,y2),color=vp.color.red,radius=m2**0.5,make_trail=False,retain=10,trail_type="points",interval=100)
l1=vp.cylinder(pos=v(0,0),radius=0.2,axis=v(x1,y1),color=vp.color.orange,texture=vp.textures.metal,make_trail=False)
l2=vp.cylinder(pos=v(x1,y1),radius=0.2,axis=v(x2-x1,y2-y1),color=vp.color.orange,texture=vp.textures.metal,make_trail=False)

def m1change():
	global w1
	w1=0
	m1=M1.value
	p1.radius=m1**0.5

scene.append_to_caption("\nMass of upper bob")
M1=vp.slider(bind=m1change,min=0.1,max=15,step=0.1,value=m1)

def m2change():
	global w2
	w2=0
	m2=M2.value
	p2.radius=m2**0.5
scene.append_to_caption("\nMass of lower bob")
M2=vp.slider(bind=m2change,min=0.1,max=15,step=0.1,value=m2)

def t1change():
	global t1,w1
	w1=0
	t1=T1.value
scene.append_to_caption("\nAngle of upper bob")
T1=vp.slider(bind=t1change,min=0,max=2*np.pi,step=0.1,value=t1)

def t2change():
	global t2,w2
	w2=0
	t2=T2.value

scene.append_to_caption("\nAngle of lower bob")
T2=vp.slider(bind=t2change,min=0,max=2*np.pi,step=0.1,value=t2)


def r1change():
	global r1,w1
	w1=0
	r1=R1.value
	print(R1.value)

scene.append_to_caption("\nLength of upper wire")
R1=vp.slider(bind=r1change,min=1,max=45,step=1,value=r1)

def r2change():
	global r2,w2
	w2=0
	r2=R2.value
	print(R2.value)
scene.append_to_caption("\nLength of lower wire")
R2=vp.slider(bind=r2change,min=1,max=45,step=1,value=r2)

t=0
dt=0.03
while True:
	vp.rate(300)
	if t>1:

		a1=(-g*(2*m1+m2)*np.sin(t1)-m2*g*np.sin(t1-2*t2)-2*np.sin(t1-t2)*m2*(w2**2*r2+w1**2*r1*np.cos(t1-t2)))/(r1*(2*m1+m2-m2*np.cos(2*t1-2*t2)))
		a2=(2*np.sin(t1-t2)*(w1**2*r1*(m1+m2)+g*(m1+m2)*np.cos(t1)+w2**2*r2*m2*np.cos(t1-t2)))/(r2*(2*m1+m2-m2*np.cos(2*t1-2*t2)))
		
		a1=1*a1
		a2=1*a2
		
		w1+=a1*dt
		w2+=a2*dt
		
		w1=1*w1
		w2=1*w2
		t1+=w1*dt
		t2+=w2*dt
		
		x1 = r1*np.sin(t1)
		y1 = - r1*np.cos(t1)
		x2 = x1 + r2*np.sin(t2)
		y2 = y1 - r2*np.cos(t2)
		
		l1.axis=v(x1,y1)
		l2.pos=v(x1,y1)
		l2.axis=v(x2-x1,y2-y1)
		p1.pos=v(x1,y1)
		p2.pos=v(x2,y2)
		
		θ1.plot(t,t1)
		θ2.plot(t,t2)
		θθ1.plot(t1,t2)
	t+=dt
		
		