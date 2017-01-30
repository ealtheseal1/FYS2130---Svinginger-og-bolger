# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:58:29 2017

@author: ealun
"""
import numpy as np
import matplotlib.pyplot as plt
#Constants
m = 2.0
k = 1.5 #N/m
v0 = 1.0 #m/s
g = 9.81 #G
dt = 0.00001

def system(time):
    time = time #free variable
    n = int(round(time/dt)) #arrays
    t = np.zeros(n,float)
    y = np.zeros(n,float)
    v = np.zeros(n,float)
    
    y[0] = 0.0 #initial position
    v[0] = v0 #initial velocity

    for i in xrange(n-1): #Euler-cromer integration method

        F = -k*y[i] - m*g #N2L and Hookes law
        a = F/m # N2l

        v[i+1] = v[i] + a*dt #Euler-cromer
        y[i+1] = y[i] + v[i+1]*dt
        t[i+1] = t[i] + dt
    
    return y,v,t
    
def plotter(y,v,t):
    
    fase = plt.plot(y,v)
    plt.xlabel("Vinkel ,$radianer$"), plt.ylabel("$Vinkelhastighet$ rad/s")
    plt.title("Faserommet") 
    plt.axis('equal')
    plt.legend()
    plt.show()
    
    bevegelse = plt.plot(t,y)
    plt.hold('on')
    plt.xlabel('$Tid, s$'), plt.ylabel('$Lengde, m$')
    plt.title('Bevegelse')
    plt.axis('equal')
    plt.legend()
    plt.show()
    
    return fase,bevegelse
       
if __name__ == '__main__':
    y,v,t = system(60)
    fase,bevegelse = plotter(y,v,t)    

        
    


