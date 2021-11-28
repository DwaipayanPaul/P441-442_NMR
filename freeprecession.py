import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
'''
# function that returns dy/dt
def model(y,t):
    k = 0.3
    dydt = -k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
'''

def de(z,t):
    # variables
    w1=0
    w0=1
    om=1
    d= 2*math.pi*3
    
    t1=1
    t2=0.3
    
    
    # ode
    u=z[0]
    v=z[1]
    w=z[2]
    
    dudt= -u/t2 + d*v
    dvdt= -d*u - v/t2 - w1*w
    dwdt= w1*v - w/t1 + w0/t1
    
    return [dudt,dvdt,dwdt]

# Initial condition
z0=[1,0,0]


# T - max
t=np.arange(0,10,0.01,dtype=float )

z=odeint(de,z0,t)

u=z[:,0]
v=z[:,1]
w=z[:,2]

plt.plot(t,u,label="U Plot")
plt.plot(t,v,label="V Plot")

plt.xlabel('Time in ns')
plt.ylabel('magnetic moment')
plt.xlim([-1,4])
plt.legend()
plt.show()


axis = plt.axes(projection='3d')
axis.scatter3D(w,v,u)
axis.set_xlabel('w')
axis.set_ylabel('v')
axis.set_zlabel('u')

plt.show()

