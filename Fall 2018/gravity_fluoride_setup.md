```python
"""Contains functions pertaining to the design of the gravity-powered fluoride removal experimentation apparatus.
"""

import math as m
import numpy as np
from aide_design.play import*

G = 9.80665 * u.m/u.s**2
"""Define the gravitational constant, in m/s²."""

def required_height(T=298*u.K, q_sys, d_sys, d_micro, l_micro, q_PACl):

  """Returns height difference (delta_h) between the water level in the fluoride constant head tank and the water level in the PACl constant head tank.

  Parameters
  ----------
  T:  scalar (float) (optional argument)
      Temperature of water

  q_sys:  scalar (float)
      Flow rate through system

  d_system: scalar (float)
      Diameter of system tubing i.e. tubing from fluoride constant head tank to flocculator

  d_micro:  scalar (float)
      Diameter of microbore tubing from PACl constant head tank to T-joint where PACl mixes with fluoride

  l_micro:  scalar (float)
      Length of microbore tubing

  q_PACl: scalar (float)
      Desired flow rate of PACl

  """
  #calculate dynamic viscosity and water density
  mu = pc.viscosity_dynamic(T)
  rho = pc.density_water(T)

  #calculate cross-sectional area of microbore tubing
  a_micro = pc.area_circle(d_micro)

  #calculate cross-sectional area of system tubing
  a_sys = pc.area_circle(d_sys)

  #calculate required height difference
  #This equation was derived from the modified Bernoulli equation, accounting for head loss due to friction through the microbore tubing.

  delta_h = -1/(2*G)*((q_sys-q_PACl)/a_sys)**2 + ((q_PACl/a_micro)**2)/(2*G) + (32*mu*L*q_PACl/a_micro)/(rho*G*d_micro)

  return delta_h

q_PACl_array = [1,2,3,4,5]
delta_h_array = []

for k in q_PACl:
  i=required_height(q_sys=2, d_sys=3, d_micro=4, l_micro=5, q_PACl=k)
  delta_h_array.append(i)


```
