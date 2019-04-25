import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv ('https://raw.githubusercontent.com/AguaClara/Fluoride_Gravity/master/Spring%202019/Langmuir%20Isotherm%202.csv')
df1 = pd.read_csv ('https://raw.githubusercontent.com/AguaClara/Fluoride_Gravity/master/Spring%202019/Langmuir%20Best%20Fit.csv')

effluent=pd.to_numeric(df["Effluent Concentration (mmol/g)"])
uptake=pd.to_numeric(df["Uptake (mmol/g)"])
Lx=pd.to_numeric(df1["Lx"])
Ly=pd.to_numeric(df1["Ly"])

plt.plot(effluent,uptake,'o')
plt.plot(Lx,Ly)

plt.xlabel('Effluent Concentration (mmol/g)')
plt.ylabel('Uptake (mmol/g)')
plt.title('Effluent Concentration of Fluoride vs. Uptake')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')

plt.show()

                





