#Volumetric Determined Average Flow Rate of PACl vs. Height
#Vertical T-junction redesign of system (microbore tubing dripping into T system)

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Change in height of PACl system
height=[10,15,20,25]
#System flow rate measured from effluent
flowrate=[0.01559184396,0.0188905051,0.02100172006,0.02395553165]

#Plot data points from experiment
plt.plot(height,flowrate,'o')

#Formatting plot
plt.xlabel('Height (cm)')
plt.ylabel('Flow Rate (mL/s)')
plt.title('Volumetrically Determined Average Flow Rate of PACl')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')

#Calculate linear regression and store stats in variables
linreg=stats.linregress(height,flowrate)
slope,intercept,r_value=linreg[0:3]

#Plot linear regression and legend
xvals=np.arange(0,35,0.01)
yvals=slope*xvals+intercept
plt.plot(xvals,yvals,color='blue',label='y={:.6f}x+{:.6f}\nR\N{SUPERSCRIPT TWO}={:.4f}'.format(slope,intercept,r_value**2))
plt.legend()

plt.show()
