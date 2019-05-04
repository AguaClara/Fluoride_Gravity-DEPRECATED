#Effluent Flow Rate vs. Height
#Second redesign of system

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Change in height of the effluent tube from the point of zero flow
height=[10,15,20,25,30,35,40]
#System flow rate measured from effluent line
flowrate=[0.3493666354,0.5100734246,0.6434089442,0.7517197384,0.9259788526,1.069752319,1.225014697]

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




