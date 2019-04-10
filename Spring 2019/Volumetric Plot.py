#Volumetric Determined Average Flow Rate of PACl vs. Height
#Second redesign of system (microbore tubing dripping into T system)

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Change in height of PACl system
height=[5,10,15,20,25,30]
#System flow rate measured from effluent
flowrate=[0.02583472335,0.03367053161,0.03962373578,0.04338574177,0.05256246053,0.05848966854]

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
