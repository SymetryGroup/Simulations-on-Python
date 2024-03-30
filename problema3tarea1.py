import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre, factorial

r = np.linspace(0.01,4,30)

n= 4
a = 2.5
theta = np.linspace(0,2*np.pi,30)



e = 1e-7

def deriv(n,x):
    dlegendre = (eval_legendre(n+e,x) - eval_legendre (n-e,x))/2*e

    return dlegendre



def B1(x,y):
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(y,x)
    

    Br = 0
    B_theta = 0

    for i in range(60):
        Br = Br + ((-1)**(i)*factorial(2*i)*(2*i+1)*r**(2*i)*eval_legendre(2*i+1,np.cos(theta)))/((2**i*factorial(i))**2*a**(2*i+1))
        B_theta = B_theta + ((-1)**(i+1)*factorial(2*i)*r**(2*i)*np.sin(theta)*deriv(2*i+1,np.cos(theta)))/((2**i*factorial(i))**2*a**(2*i+1))

    Bx = Br*np.cos(theta) - B_theta*np.sin(theta)
    By = Br*np.sin(theta) + B_theta*np.cos(theta)

    return Bx , By



def B2(x,y):
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(y,x)
    

    Br = 0
    B_theta = 0

    for i in range(1,60):
        Br = Br + ((-1)**(i+1)*factorial(2*i)*2*i*a**(2*i)*eval_legendre(2*i-1,np.cos(theta)))/((2**i*factorial(i))**2*r**(2*i+1))
        B_theta = B_theta + ((-1)**(i+1)*factorial(2*i)*deriv(2*i-1,np.cos(theta))*a**(2*i)*np.sin(theta))/((2**i*factorial(i))**2*r**(2*i+1))
    
    Bx = Br*np.cos(theta) - B_theta*np.sin(theta)
    By = Br*np.sin(theta) + B_theta*np.cos(theta)

    return Bx , By


x = np.linspace(-4,4,30)

y = np.linspace(-4,4,30)


(X,Y) = np.meshgrid(x,y)

condicion1 = np.sqrt(x**2+y**2) <= a

X1 = X[condicion1]
Y1 = Y[condicion1]

Bx1, By1 = B1(X1,Y1)

norma1 = np.sqrt(Bx1**2+By1**2)

condicion2 = np.sqrt(x**2+y**2) > a

X2 = X[condicion2]
Y2 = Y[condicion2]

print(X2)
print(Y2)

Bx2, By2 = B2(X2,Y2)

norma2 = np.sqrt(Bx2**2+By2**2)


plt.figure(figsize=(8, 6))
plt.quiver(Y1, X1, By1/norma1, Bx1/norma1, linewidth=1)
#plt.quiver(Y2, X2, By2/norma2, Bx2/norma2, linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()