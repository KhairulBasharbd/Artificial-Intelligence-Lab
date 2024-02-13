
import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.1)



w1,b1 = 1,10
u1 = w1*x + b1
y1 = 1 / (1 + np.exp(-u1))
w2, b2 = 5,5
u2 = w2*x + b2  
y2 = 1 / (1 + np.exp(-u2))

w3, w4, b = 10, 15,20
w = w3*y1 + w4*y2 + b   
y = 1 / (1 + np.exp(-w))

plt.title('Sigmoid of weighted sum : y = 1/(1+e^(-w)')     
plt.xlabel('x') 
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.plot(x,y)

plt.show()