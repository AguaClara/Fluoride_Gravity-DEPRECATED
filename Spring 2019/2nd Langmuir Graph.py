import pandas as pd
import matplotlib.pyplot as plt

#import experimental data as a CSV file
df = pd.read_csv ('https://raw.githubusercontent.com/AguaClara/Fluoride_Gravity/master/Spring%202019/Langmuir%20Isotherm%202.csv')
#import Langmuir best fit line as a CSV file
df1 = pd.read_csv ('https://raw.githubusercontent.com/AguaClara/Fluoride_Gravity/master/Spring%202019/Langmuir%20Best%20Fit.csv')

#save each column of data
effluent=pd.to_numeric(df["Effluent Concentration (mmol/g)"])
uptake=pd.to_numeric(df["Uptake (mmol/g)"])
Lx=pd.to_numeric(df1["Lx"])
Ly=pd.to_numeric(df1["Ly"])

#plot the experimental data and the Langmuir isotherm
plt.plot(effluent,uptake,'o', label='Experimental Data')
plt.plot(Lx,Ly, label='Langmuir Best Fit')

#formatting
plt.xlabel('Effluent Concentration (mmol/g)')
plt.ylabel('Uptake (mmol/g)')
plt.title('Experimental Data Fit with Langmuir Adsorption Model')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')


plt.legend()


plt.show()

                





