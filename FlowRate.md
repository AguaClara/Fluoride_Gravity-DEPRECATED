Calculations for flow rates into system.
Fluroide has been running at 1.5 mm/s upflow velocity which is roughly .076 mL/s of volumetric flow. Your volumetric flow of fluoride and PACL should add together to somewhere around .076 mL/s.
```python
import math as m
import numpy as np
from aguaclara.play import*
#Input your concentrations you want your system to run at and the upflow velocity in your sed tube
Conc_PACl_exp = 40 * (u.milligram / u.liter)#PACl concentration in your experiment
upflow_velocity = 1.5 * (u.millimeter / u.second)
#Change the above parameters for what you want in your experiment
#Input your concentrations of your stock tanks
Conc_PACl_stock = 1000 * (u.milligram / u.liter)
Conc_fluoride_stock = 100 * (u.milligram / u.liter)

D_sed_tube = 1*u.inch
Area_sed_tube = np.pi*(D_sed_tube**2)/4
Q_system = Area_sed_tube * upflow_velocity
Q_system.to(u.milliliter/u.second)
Q_PACl = (Q_system * Conc_PACl_exp / Conc_PACl_stock).to(u.milliliter/u.second)
print(Q_PACl)
Q_fluoride = (Q_system-Q_PACl)
conc_fluoride_exp = Conc_fluoride_stock * Q_fluoride / Q_system
print(conc_fluoride_exp)
```

So ideally for your experimental setups with fluoride you should know the concentrations of both of your stock tanks that will flow into the system. Fluoride subteams have been using 1.5 mm/s of upflow velocity but you can change this if you would like. The above code should tell you the flowrate of PACl you want into your system, Sarah's code should then correlate that Q into a height difference between the PACl constant head tank and the drip chamber for your system. It will also tell you the fluoride concentration within the experiment that you are working with.
