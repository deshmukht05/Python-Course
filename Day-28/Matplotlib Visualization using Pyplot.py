# Matplotlib Visualization using Pyplot
# We know that graphical or pictorial or visual representation of data is easy for understanding the data statistics like trend, correlation, pattern, etc. 
# The pyplot() is the most important function in matplotlib library and is used to plot 2 dimensional data. 
# The Numpy is another library avaiiled in python that offers various useful function and routines to create array. 

import numpy as np
import matplotlib.pyplot as plt
l = [2, 4, 8, 1, 9]
ar1 = np.array(l)
plt.plot(ar1)
plt.show()