# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:01:07 2017

@author: ealun
"""
import numpy as np
import matplotlib.pyplot as plt

#t_max = 20 #program timeout
g = -9.81 #aceleration of gravity
dt = 0.0001 #increase of time for each iteration
D = 0 #friction with air

def system(time):

    n = int(round(time/dt))
    x = np.zeros(n,float)
    v = np.zeros(n,float)
    a = np.zeros(n,float)
    t = np.zeros(n,float)
    
    x[0] = 1.0 #Meter
    v[0] = 0.0

    for i in xrange(n-1):
        
        a[i] = g - D*v[i]*abs(v[i])
        v[i+1] = v[i] +a[i]*dt
        x[i+1] = x[i] +v[i+1]*dt
        
    
        if (x[i+1] < 0.0):
            v[i+1] = -v[i+1]

        t[i+1] = t[i] +dt

    return x,v,t
    
    
def plotter(x,v,t):
     
    fase = plt.plot(x,v)
    plt.hold('on')    
    plt.xlabel("Posisjon [m]"), plt.ylabel("Hastighet $m/s$")
    plt.title("Faserommet") 
    plt.axis('equal')
    plt.legend()
    plt.show()
        
    bevegelse = plt.plot(t,x)
    plt.hold('on')
    plt.xlabel('$Tid, s$'), plt.ylabel('$Hoyde, m$')
    plt.title('Bevegelse')
    plt.axis('equal')
    plt.legend()
    plt.show()
    
    return fase,bevegelse
     
     
     

if __name__ == '__main__':
    x,v,t = system(3.5)
    fase,bevegelse = plotter(x,v,t)