#Effluent Flow Rate vs. Height
#Second redesign of system

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Change in height of the effluent tube from the point of zero flow
height=[5,10,15,20,25,30,35,40]
#System flow rate measured from effluent line
flowrate=[0.303921123,0.4525731793,0.6403088421,0.7827710055,0.8833781973,1.043483972,1.186551281,1.336794586]

#Plot data points from experiment
plt.plot(height,flowrate,'o')

#Formatting plot
plt.xlabel('Change in Height (cm)')
plt.ylabel('Flow Rate (mL/s)')
plt.title('Effluent Flow Rate of System')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')

#Calculate linear regression and store stats in variables
linreg=stats.linregress(height,flowrate)
slope,intercept,r_value=linreg[0:3]

#Plot linear regression and legend
xvals=np.arange(0,45,0.01)
yvals=slope*xvals+intercept
plt.plot(xvals,yvals,color='blue',label='y={:.6f}x+{:.6f}\nR\N{SUPERSCRIPT TWO}={:.4f}'.format(slope,intercept,r_value**2))
plt.legend()

plt.show()




