import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def trimem(x,a,b,c):
    x = range(x)
    y = np.zeros(np.size(x))
    for i in x: 
        if x[i] < a: 
            y[i] = 0 ; 
        elif (( x[i] >= a ) and ( x[i] < b )): 
            y[i] = (x[i]-a) / (b-a)
        elif (( x[i] >= b ) and ( x[i] < c )): 
            y[i] = (c-x[i]) / (c-b)
        elif x[i] >= c : 
            y[i] = 0 
    plt.plot(x, y)
    plt.show()

def trapmf(x,a,b,c,d): 
    x = range(x)
    y = np.zeros(np.size(x))
    for i in x : 
        if x[i] < a : 
            y[i] = 0 
        elif ((a <= x[i]) and (x[i] < b)): 
            y[i] = (x[i]-a)/(b-a) 
        elif ((b <= x[i]) and (x[i] < c)): 
            y[i] = 1 
        elif ((c <= x[i]) and (x[i] < d)): 
            y[i] = (d-x[i])/(d-c) 
        elif x[i] >= d :
            y[i] = 0 
    plt.plot(x, y)
    plt.show()  

def gussmf(x,m,s): 
    x = np.arange(0.0,x,0.1)
    y = np.exp( -(x-m)**2 / 2*(s)**2 )      
    plt.plot(x, y)
    plt.show() 

def bellshmf(x,a,b,c):
    x = np.arange(0.0,x,0.1)
    d = 2*b
    y = 1 / (1+ (abs((x-c)/a)**d))
    plt.plot(x, y)
    plt.show() 

def smf(x,a,b): 
    x = np.arange(0.0,x,0.1)
    y = np.zeros(np.size(x))
    for i in range(len(x)) : 
        if x[i] <=a : 
            y[i] = 0 
        elif (a <= x[i]) and (x[i] <= (a+b)/2) : 
            y[i] = 2*((x[i]-a)/(b-a))**2
        elif ((a+b)/2 <= x[i]) and (x[i] <= b) :
            y[i] = 1 - 2*((x[i]-b)/(b-a))**2
        elif x[i] >= b : 
            y[i] = 1

    plt.plot(x, y)
    plt.show() 

def zmf(x,a,b): 
    x = np.arange(0.0,x,0.1)
    y = np.zeros(np.size(x))
    for i in range(len(x)) : 
        if x[i] <=a : 
            y[i] = 1 
        elif (a <= x[i]) and (x[i] <= (a+b)/2) : 
            y[i] = 1 - 2*((x[i]-a)/(b-a))**2
        elif ((a+b)/2 <= x[i]) and (x[i] <= b) :
            y[i] = 2*((x[i]-b)/(b-a))**2
        elif x[i] >= b : 
            y[i] = 0

    plt.plot(x, y)
    plt.show() 

def main(): 
    #trimem(15,0,5,10)
    #trapmf(13,0,2,8,10)
    #gussmf(10,5,1)
    #bellshmf(12,2,4,5)
    #smf(10,2,8)
    zmf(10,2,8)
    

if __name__ == "__main__":
    main()
