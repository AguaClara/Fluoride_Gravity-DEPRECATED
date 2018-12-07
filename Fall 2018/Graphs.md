# Graphs

This shows the Python code used to make graphs:

```Python

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from scipy import stats

#x coordinates are the height difference between fluoride constant head tank and PACl constant head tank
#y coordinates are the measured flow rates

data_points = np.array([[5, 0.00991333],
                       [10,0.0158],
                       [15,0.0269333],
                       [20,0.03577]])

x_points = data_points[:,0]
y_points = data_points[:,1]

linreg = stats.linregress(x_points, y_points)
slope, intercept, r_value = linreg[0:3]

start = x_points[0] # Change as desired
end = x_points[-1] # last element plus one; change as desired
plt.plot(x_points, y_points, 'o')
plt.plot(np.arange(start,end,0.1), np.arange(start, end,0.1)*slope + intercept)
plt.xlabel('Height Difference between Fluoride Constant Head Tank and PACl Constant Head Tank (cm)')
plt.ylabel('Measured Flow Rate (mL/s)')
plt.title('Measured Flow Rates at Varying Height Differences')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.savefig("flow_rate1.png",dpi=1000)
plt.show()


print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)


```
