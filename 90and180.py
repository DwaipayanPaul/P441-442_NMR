#IMPORTING STUFFS
import math as m
import numpy as np
from matplotlib import pyplot as plt
from scipy .integrate import odeint


#FUNCTION TO GET THE SIMULTANEOUS DIFFERENTIAL EQUATIONS
def ode(var,t,D,omega1,T1,T2,tau, w0):
    u,v,w = var
    if t<=tau:
        omega1=omega1
    else:
        omega1 = 0
    dudt = -u/T2 + D*v 
    dvdt = -D*u - v/T2 - omega1*w
    dwdt = omega1*v - w/T1 + w0/T1
    return [dudt,dvdt,dwdt]





w0=1
omega0=-1*m.pi*2
omega1=-10*m.pi*2
omega=-0.5*m.pi*2
D = omega-omega0

theta = m.pi
omegae=m.sqrt(D**2+omega1**2)
tau = theta/omegae

print(tau)

u=0
v=0
w0=1
w=1
T1 = 10
T2 = 10


D = 0#
omega1=10*m.pi*2#
tau = 0.05#




#tArr = np.arange(0,20,0.01,dtype=float)

tArr = np.arange(0,2,0.001,dtype=float)#


ini_cond = (u,v,w)
param = (D, omega1, T1, T2, tau, w0)

results = odeint(ode,ini_cond,tArr,args=param)
u = results[:,0]
v = results[:,1]
w = results[:,2]

axis = plt.axes(projection='3d')
axis.plot3D(u,v,w,'green')
axis.set_xlabel("u")
axis.set_ylabel("v")
axis.set_zlabel("w")
plt.show()

