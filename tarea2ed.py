import numpy as np

import matplotlib.pyplot as plt 


x = np.linspace(0,7,20)
y = np.linspace(0,7,20)


(x,y) = np.meshgrid(x,y)


x1 = np.linspace(0,7,200)
y1 = np.linspace(0,7,200)


(x1,y1)=np.meshgrid(x1,y1)

a = 4
b = 2.5 

pot = 1/((x-a)**2+(y-b)**2)**0.5-1/((x-a)**2+(y+b)**2)**0.5
-1/((x+a)**2+(y-b)**2)**0.5+1/((x+a)**2+(y+b)**2)**0.5


Ex = +(x-a)/((x-a)**2+(y-b)**2)**1.5-(x-a)/((x-a)**2+(y+b)**2)**1.5
-(x+a)/((x+a)**2+(y-b)**2)**1.5+(x+a)/((x+a)**2+(y+b)**2)**1.5

Ey = +(y-b)/((x-a)**2+(y-b)**2)**1.5-(y+b)/((x-a)**2+(y+b)**2)**1.5
-(y-b)/((x+a)**2+(y-b)**2)**1.5+(y+b)/((x+a)**2+(y+b)**2)**1.5

color = np.sqrt(Ex**2+Ey**2)

Ex = Ex/color

Ey = Ey/color

plt.quiver(x,y,Ex,Ey,np.log(color),pivot = 'middle',cmap='plasma')
c = plt.contour(x1,y1,pot, levels=[0.5,1,1.5,2,2.5,3,3.5], colors='blue')
plt.clabel(c,inline=True)
plt.colorbar()

plt.show()