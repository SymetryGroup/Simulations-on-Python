import numpy as np 
import matplotlib.pyplot as plt

kq = 1

x = np.linspace(-5,5,20)
y = np.linspace(-5,5,20)
a = 1.5

x1 = np.linspace(-5,5,200)
y1 = np.linspace(-5,5,200)

(x,y) = np.meshgrid(x,y)

(x1,y1)=np.meshgrid(x1,y1)

u = kq*((x-a)/((x-a)**2+y**2)-(x+a)/((x+a)**2+y**2))
v = kq*((y)/((x-a)**2+y**2)-(y)/((x+a)**2+y**2))

pot = kq*np.log(((x1+a)**2+y1**2)/((x1-a)**2+y1**2))

c=np.arange(-3,3.1,1)

r = np.sqrt(a**2+c**2)

y2 = np.linspace(r-c,r+c,100)

x21 = np.sqrt(a**2+c**2-(y2-c)**2)

x22 = -np.sqrt(a**2+c**2-(y2-c)**2)

color = np.sqrt(u**2+v**2)

u = u/color
v = v/color

plt.quiver(x,y,u,v,np.log(color),pivot = 'middle',cmap='plasma')
plt.colorbar()

c = plt.contour(x1,y1,pot, levels=[-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0.5,1,1.5,2,2.5,3,3.5], colors='blue')
plt.clabel(c,inline=True)
plt.plot(x21,y2)
plt.plot(x22,y2)
plt.title('Campo electrico 'r'$\vec{E}(x,y)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()