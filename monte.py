# Estimating pi using the monte carlo method
import numpy as np

limit = 5000000

darts = 0
insideCircle = 0

while darts < limit:
    darts +=1
    x = np.random.uniform(-1.0,1.0)
    y = np.random.uniform(-1.0,1.0)
    if x*x + y*y <= 1:
        insideCircle += 1
    
    #print(x,y,inside)


print(darts)
print(insideCircle)
pi = 4 * (insideCircle / darts)
print(pi)
