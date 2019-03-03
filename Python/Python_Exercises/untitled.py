import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2
fig = plt.figure()
axes = fig.add_axes([.1, .1, .8, .8])
axes.plot(x,y)
axes.set_xlabel("X")
axes.set_ylabel("Y")
axes.set_title("Title")
plt.show()