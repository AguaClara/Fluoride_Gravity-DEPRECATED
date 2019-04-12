# Fluoride Gravity, Spring 2019
#### Sarah Huang, Cindy Jin, Simar Kohli
#### April 12, 2019
This publication Fluoride, Spring 2019 was developed under Assistance Agreement No. SU-83695001 awarded by the U.S. Environmental Protection Agency to Cornell University. It has not been formally reviewed by EPA. The views expressed in this document are solely those of Sarah Huang, Cindy Jin, and Simar Kohli and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication.

**[Sidney: Hey team! I will be using bolded square brackets to comment on your manual.]**

**[Overall: Very minor grammar issues and some improvements to be made with your code but you're doing good!]**

## Abstract
Fluoride contamination of water is a significant issue faced by nations and people across the globe, and can, lead to adverse consequences on health (e.g. muscle weakness and atrophy, weakness, fatigue). The Fluoride Gravity team’s objective is to develop a cost-effective, self-sufficient mechanism for extracting excess fluoride from drinking water. The Spring 2019 team hopes to further the gravity-powered system’s efficacy and potentially begin to run field-tests with the device. The application of such a device in real-world scenarios will be predicated upon success seen with the aforementioned field tests.


## Introduction
The majority of AguaClara plants are located in Central America, where the sources of surface water originate from rivers and mountain streams. AguaClara's mission of providing access to safe drinking water for all has motivated the AguaClara team to expand and develop new goals. By considering and analyzing the differences in drinking water collected from groundwater sources in other regions around the world, AguaClara can serve communities outside of Central America who are deprived of access to safe drinking water.

At some locations where there is little to no fluoride in drinking water, fluoride is added in for the purpose of strengthening teeth and deteriorating natural deposits [(NYC DEP, 2016)](http://www.nyc.gov/html/dep/pdf/wsstate16.pdf). However, there are detrimental consequences when there is an excess concentration of fluoride in the water being consumed by inhabitants in the area. For example, there has been moderate to high fluoride pollution in regions such as Algeria, Thailand, Ghana, India, and Iran, whose major source of drinking water comes from groundwater sources. The pollution of groundwater in these regions is due to the mobile dissolution of fluorite, apatite, and topaz from weathered rocks, increasing the levels of fluoride in the groundwater [(Bhattacharya and Samal, 2018)](http://www.isca.in/rjrs/archive/v7/i4/6.ISCA-RJRS-2018-028.pdf). The effects of consuming excess fluoride include dental, skeletal, developmental, neurological, endocrine, reproductive, and carcinogenic issues that affect the health of the communities in areas of high fluoride concentrations [(Bhattacharya and Samal, 2018)](http://www.isca.in/rjrs/archive/v7/i4/6.ISCA-RJRS-2018-028.pdf). Therefore, the World Health Organization (WHO) regulated the concentration limit for fluoride in drinking water to be 1.5 mg/L [(Water-related diseases, 2016)](https://www.who.int/water_sanitation_health/diseases-risks/diseases/fluorosis/en/).

In India, the Bureau of India Standards set an upper limit of fluoride concentrations in drinking water to be 1 mg/L [(Bureau of India Standards, 2012)](https://archive.org/details/gov.in.is.10500.2012). However, more than 65 million Indians consume drinking water above the recommended limit of 1.5 mg/L and some locations in India contain up to 20 mg/L, which risks the health of many communities [(LeChevallier and Au, 2004)](https://www.who.int/water_sanitation_health/publications/9241562552/en/).

AguaClara aspires to achieve the recommended limit of 1 mg/L or lower by the Bureau of India Standards and to implement the gravity-powered system of fluoride removal into the communities with excess concentrations of fluoride. The Fluoride Gravity team will be testing the gravity-powered apparatus with PACl and red dye substituted as fluoride to optimize fluoride removal to achieve residual concentration of less than 1 mg/L. If the gravity-powered fluoride removal apparatus operates in the optimal conditions of removing fluoride to a concentration of 1 mg/L, feasibility analysis on site will be performed to test whether the system can be used in the communities in India, which will allow AguaClara to provide access to safe drinking water in India and other locations that obtain water from groundwater sources.


## Literature Review
### Interaction between Polymeric Aluminum Hydroxide with Fluoride
When hydrolyzed, polyaluminum based coagulants, one of which is polyaluminum chloride, formed mono- and polymeric species [(Gebbie, 2001)](http://wioa.org.au/conference_papers/2001/pdf/paper6.pdf). The interaction between aluminum hydroxide polymer and fluoride led to the formation of several insoluble and soluble products depending on the ratio of total fluoride ion and aluminum ion concentrations, pH, and the total applied fluoride and aluminum concentrations [(Parthasarathy et al., 1986)](http://www.nrcresearchpress.com/doi/abs/10.1139/v94-310). When pH was less than 4, the predominant fluorocomplex was AlF due to the complete dissociation of polymeric aluminum. When the ratio of total fluoride ion and aluminum ion concentrations was between 0.5 and 1, fluoride was observed to precipitate, replacing some of the hydroxide ions ions in the aluminum hydroxide polymer. When the ratio of total fluoride ion and aluminum ion concentration was greater than 3, there is both precipitate and dissolved complexed fluoride present. It was observed that the optimal conditions for precipitating fluoride was a hydroxide to aluminum ratio of 2.5, a fluoride to aluminum ratio of 0,7, and a pH between 4 and 7.


### Mechanisms Governing Removal of Fluoride
Of the potential mechanisms that may play a role in the removal of fluoride with polyaluminum chloride, including surface adsorption, coprecipitation, and precipitation, it appeared that coprecipitation is the main mechanism [(Kowalchuk, 2011)](https://digitalrepository.unm.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1059&context=ce_etds). Coprecipitation is the contamination of a precipitate by an impurity that is otherwise soluble under the conditions of precipitation [(Randtke in Kowalchuk, 2011)](https://digitalrepository.unm.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1059&context=ce_etds). Occlusion and surface adsorption played major roles in this process.

### Interactions Among Fluoride, NOM, and Alum During Coagulation Process
Experimental results from jar tests illuminated mechanisms of behind fluoroaluminum complexation [(Herrboldt, 2016)](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1). When fluoride was present in the system with alum, the residual aluminum increased significantly, indicating that fluoride is likely forming a soluble fluoroaluminum complex. In the removal of fluoride, the presence of natural organic matter (NOM) caused a small decrease in fluoride removal from 50.1% to 45.8%, whereas NOM removal was greatly inhibited by the presence of fluoride [(Herrboldt, 2016)](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1). This indicates that in the removal of fluoride, fluoride was likely outcompeting NOM for complexation with aluminum or adsorption to aluminum solids.

In the precipitation of aluminum with fluoride, fluoride was predicted to act in the following manner: since fluoride is a negatively charged species, fluoride must overcome the negative charge repulsion between particles in order to allow for aggregation. In the precipitation of fluoride with aluminum, the disruption of charges due to the negative repulsion stops collisions and ultimately causes particles to be concentrated at smaller particle diameters [(Herrboldt, 2016)](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1). In this manner, fluoride may inhibit the aggregation of flocs by acting as a stabilizing agent or by inhibiting precipitation. It was hypothesized that fluoride prevents the growth of precipitates by inhibiting interactions between hydroxide and nearby particles. It was also hypothesized that, due to the way that fluoride can replace hydroxide in solids , the formation of aluminum hydroxide complexes is disrupted.

### pH Dependence of Fluoride Removal
In a study by Gong et al. (2012), fluoroaluminum complexation was found to exhibit pH dependence. At pH values less than 5.0, almost all fluoride existed as fluoro-aluminum complexes, inhibiting its removal by coagulation. At pH levels greater than 8.0, fluoride almost exclusively as free fluoride, indicating that hydroxide has a greater affinity for aluminum at a higher pH [(Herrboldt, 2016)](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1).

### Collection and Analysis of Fluoride samples
An Ion-Selective Electrode (ISE) fluoride probe is used to measure the fluoride concentration of a sample. The following quality-control procedures should be followed.

ISE fluoride probes can only detect solubilized fluoride, and would give inaccurate readings in the presence of Fe3+ and Al3+, such as in cases where polyaluminum chloride is added to the system. Total Ionic Strength Adjusting Buffer (TISAB) solution is added to samples to solubilize the fluoride in the sample and keep the sample at a constant pH of 5-5.5. Temperature should be kept constant with less than a 1 degree Celsius deviation [(EPA Method 9214)](https://www.epa.gov/sites/production/files/2015-12/documents/9214.pdf).

Polyethylene containers, instead of glassware, should be used, since fluoride can adsorb to glass. An Initial Calibration Verification standard and a Continuing Calibration Verification standard should also be used, consisting of solutions of known fluoride concentration within the mean expected fluoride concentration that should be tested. The ICV should be used to test the accuracy of the calibration curve and the CCV should be sued after every 10 samples to ensure that the fluoride probe has not drifted from the calibration curve. These controls should be within 10% of their known values. A control blank containing one part water and one part TISAB should also be used to enhance the accuracy of data in future experiments.

## Previous Work
A coagulant-sedimentation system was developed to extract fluoride from contaminated water. Multiple tests have been run by past teams to analyze the efficacy of the designed filtration system using polyaluminum chloride (PACl) as a coagulant.

The Spring 2016 team continued to develop a more efficient filtration system by testing PACl with clay [(Longo, 2016)](https://drive.google.com/file/d/0B9yahrdDmfVpQ0t0M2NUUkRRNHM/view). While the team was successfully able to create a floc blanket, the Summer 2017 deemed clay to be not as necessary as it increased the effluent turbidity of the system, [(Akpan et al., 2017)](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md), and therefore ran tests with just fluoride and PACl. However, it was soon realized that the system would begin to fail after just 10 hours. In conjunction with the Summer 2017 High Rate Sedimentation Team, a new reactor was able to boost the time to failure and allow for increased upflow velocities. It was determined that the most efficient upflow velocity was 1.5 mm/s [(Pang et al., 2018)](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md#previous-work). The same team continued to conduct experiments with varying concentrations of PACl in order to develop an absorbance spectrum and determine the most effective concentration of PACl to be delivered to the system.


<img src="Fit with Langmuir Isotherm.PNG">

**Figure 1:** A Langmuir Adsorption Model fitting data from trials conducted by Fall 2017 team.

The 2018 cycle of teams managed to focus on developing a robust, gravity-powered filtration system [(Akpan et al., 2017)](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md).

<img src="Schematic.PNG">

**Figure 2:** A schematic for the gravity-powered system with differences in height generated power.

Some of the major designs of the model were created by the Spring 2018 team, and focused on deploying float valves to maintain a constant amount of water flowing through the system. Since the concentration of the PACl solution remained constant in the stock tank, a calculation of flow rate provided insight into the concentration of PACl actually entering in the system [(Pang et al., 2018)](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md#previous-work).

The Summer 2018 team furthered the flexibility of the filtration system by including sliders for controlling height differences between different tanks and pipes. This provided the ability for teams to adjust the flow rate within the system.

<img src="Diagram.PNG">

**Figure 3:** Adjustments made by the Summer 2018 team to the set-up to allow for height variations.


The Summer 2018 team continued to conduct tests on varying PACl concentrations and fitted new data to the Langmuir adsorption spectrum created by the Fall 2017 team. Concentrations of fluoride (range: 3 to 20 mg/L) and PACl (range: 10 to 50 mg/L) were tested. A Langmuir isotherm was applied to the data to obtain a new uptake vs effluent model [(Pang et al., 2018)](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md#previous-work).

The following equation was used: $$ \frac{C_e}{q_e} = \frac{1}{q_e}C_e+\frac{1}{K_L\cdot q_m} $$

where $C_e$ is the equilibrium concentration of the adsorbant, $q_e$ is the amount adsorbed at equilibrium, and $K_L$ and $q_m$ are Langmuir constants which are related to adsorption capacity and energy of adsorption.

<img src="Fit with Langmuir Isotherm 2018.PNG">

**Figure 4:** A Langmuir isotherm fitted with data from the Summer 2018 team.

In Fall of 2018, two teams were made from the original Fluoride team: [Fluoride Gravity](https://github.com/AguaClara/Fluoride_Gravity) worked to make the gravity-powered apparatus more efficient, and [Fluoride Auto](https://github.com/AguaClara/Fluoride-Auto) spearheaded the development of an adsorption model by running more bench experiments [(Pang et al., 2018)](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md#previous-work).

Finally, the Fall 2018 team prioritized developing a mechanism or process for measuring coagulant flow rate within the system. An IV drip was installed within the filtration system along with microtubing. While headloss still occurred, the team adjusted the height of the coagulant constant head tank to modify flow rate. The drip chamber was noted to substantially streamline the process of measuring flow rate [(Pang et al., 2018)](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md#previous-work).

The goal of the Spring 2019 Fluoride team was to modify any necessary parts to the filtration system developed over the past few years by previous Fluoride teams, begin to run comprehensive tests on red-dye within the system, and finally proceed to testing fluoride solutions within the filtration system itself. **[Remember to use past tense when talking about any work you are doing this semester.]**

## Methods
### Experimental Apparatus
The gravity-powered apparatus was constructed as according to the fabrication manual in the [Fluoride Gravity Fall 2018 report](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md).

### Redesigning of Filtration System
Despite the foundational work of the apparatus laid by the Fall 2018 team, it was determined the filtration system needed to focus on having modifications in three major areas:

* Development of new method of introduction of polyaluminum chloride (PACl)
*	Size reduction of fluoride constant head tank
*	Increasing length of flocculator

However, most of the other aspects of the filtration system were kept the same (e.g. sliders for moving tanks up and down, the presence of stock and constant head tanks, and the sedimentation tube).

The overall set up of the current system is shown in Figure 5.

<img src="current diagram.png">

**Figure 5:** An overview of the newly modified filtration system.

#### Coagulant Introduction and Fluoride Constant Head Tank Size Reduction
The principal reason for modifying the method by which coagulant (PACl) was introduced into the system was the inefficiency of the IV drip chamber system set up by the Fall 2018 team (Figure 6).

<img src="IV drip.png">

**Figure 6:** The IV drip system that was implemented by Fall 2018 team. IV drip chamber was connected to coagulant constant head tank and flowed into flocculator.

When the system would be run under the previous set-up, hydrostatic pressure from the flocculator could drive water into the drip chamber, filling it completely by the time the system was restarted. This resulted in the team having to consistently flush out the chamber, however, this led to air being introduced into the tubing and stopping flow within the system, entirely [(Pang et al., 2018)](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md).

As a result, the team focused on creating a more effective drip system for introducing PACl while also being able to monitor flow rate/the rate of introduction of PACl into the system.

#### First Redesign

Several changes were made to optimize the ease of use of the apparatus. The IV drip chamber was removed due to previous difficulties in starting the system, The T-joint was removed, allowing the fluoride constant head tank to be directly connected to the flocculator (Figure 7).

<img src="IMG_20190209_092106.png">

**Figure 7:** New connection linking the fluoride constant head tank with the flocculator.

The team decided to directly drip the coagulant into the fluoride constant head tank by taping the end of the microtubing to the side of the tank (Figure 7). However, given that the size of the actual constant head tank was too large for proper mixing of the coagulant to occur, the constant head tank was reduced to a smaller size to allow for better mixing of the coagulant in the actual fluoride solution.

<img src="IMG_20190209_092113.png">

**Figure 8:** Microbore tubing connected to the PACl system allows PACl to drip directly into the fluoride constant head tank.

However, two major problems were noted with this procedure. The first was coagulation began in the tank as a result of dripping PACl directly into the tank. This could risk failure of the system if the coagulation blocked the outflow from the fluoride constant head tank. The second problem was a non-homogenous mixture was formed within the constant head tank, resulting in lower flocculation.

#### Second Redesign
The team determined that a new mechanism was necessary for effectively introducing the PACl into the system, one that would allow for easy calculation of flow rate, prevent re-introduction of air within the system, and create essentially a homogenous solution flowing into the flocculator.

As a result, the team decided that a T-junction could be used in between the outflow of the fluoride constant head tank and the flocculator. The third hole on the T-junction would be connected to a translucent pipe in which the PACl microtubing would drip the coagulant into (Figure 9).

<img src="new drip.jpg">

**Figure 9:** The system works by dropping PACl in to the solution flowing out of the system (towards the flocculator). Flow rate can be calculated by counting the volume of PACl dispensed in a certain period of time, producing a flow rate. Alternatively, the number of drops dispensed can be tracked by shining a light through the translucent tubing. The volume of one drop can be calculated, multiplied by the number of drops introduced in a time frame, and divided by the total time taken.

#### Increasing Flocculator Length
The length of the flocculator was increased to provide greater amount of time for flocculation. Specifically, the newly constructed coils around the main cardboard cylinder approximately 40 times, and was constructed from 46 ft of tubing (Figure 10).

<img src="flocculator.jpg">

**Figure 10:** The flocculator (lengthened) in the filtration system.

The reasoning behind increasing the flocculator’s length was that the PACl may need more time mixing effectively with the solution to produce the flocs necessary for filtration. Furthermore, providing more room and opportunity for collision between PACl molecules and the fluoride/red-dye within the system creates a more effective flocculation system and overall filtration system.  

### Addition of Bottom Geometry in Sedimentation Tube
The red dye flocs were observed to be clumping together at the bottom of the sedimentation tube, which resulted in the formation of a gel rather than a fluidized bed (Figure 11).

<img src = "before botgeo.gif" height = "350" width = "300">

**Figure 11:** The formation of a gel is seen on the bottom of the sedimentation tube, which prevents the flow of clean water to exit the sedimentation tube and prevents the removal of the red dye particles from the PACl solution.

In order to prevent the formation of a gel at the bottom of the sedimentation tube and to effectively remove flocs, a [bottom geometry](
https://github.com/AguaClara/Fluoride_Gravity/blob/master/Spring%202019/BotGeo.stl) was added to the bottom of the sedimentation tube to increase recirculation and collisions of the flocs to promote the formation of a fluidized bed (Figure 12).

<img src = "after botgeo.gif" height = "350" width = "300">

**Figure 12:** The formation of a fluidized bed is seen after the addition of the bottom geometry.

The bottom geometry helped with the removal of flocs in the system because the slanted angle in the bottom geometry allowed for flocs to resuspend and change in flow direction rather than fall to the bottom of the sedimentation tube. The fluidized bed allowed for the flocs to move along the sedimentation tube and down the waste line as the PACl and water solution past the waste line and exit the effluent line. Thus, the flocs were able to form a fluidized bed and increase the removal of red dye flocs from the PACl solution.


### Jar Testing: Methods
In previous runs of the second redesign of the gravity powered system, it was observed that red dye particles continued to float through the sedimentation tube regardless of its upflow velocity. That is, even when the system was stopped, all of the red dye flocs floated to the top of the sedimentation tube.

To test whether this result was specific to mechanics of flocculation that could perhaps change the properties of red dye flocs, a jar test was conducted, using a magnetic stirrer to rapidly mix the solution to increase collision rates.

Plastic beakers with 420 $\mu$L of PACl was mixed with 400 $\mu$L of red dye in 400 mL of water. The solution was using a stir bar for 15 minutes before leaving the solution to settle.

This was compared to a solution of red dye-PACl flocs collected directly from the experimental apparatus after flocculation. The flocculator was run at a system concentration of 40 mg/L of PACl, which was mixed with red dye. The solution after flocculation was added to a beaker initially containing 200 mL of water to simulate conditions in the sedimentation tank. The flocculation solution was added to the beaker it was roughly the same color as the first independently created solution. The solution was not stirred and was allowed to settle directly after the addition of flocs.

## Results and Analysis
### Determining the Effectiveness of New System
#### Determining Coagulant Flow Rate
The flow rate of PACl was determined to have a linear relationship with the height differential between the fluoride constant head tank and the PACl constant head tank by the [Fluoride Gravity Fall 2018 team](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md#measuring-coagulant-flow-rate). It was hypothesized that the decoupled PACl system would exhibit the same linear relationship with the change in height. The flow rate of the PACl entering the decoupled fluoride system was determined in two different methods: gravimetrically and volumetrically.

#### Gravimetric Method: First Redesign of System
The flow rate of the coagulant was determined by measuring the change in mass of the PACl stock tank over a period of time. This was then converted to volumetric flow rate. This was mode of measurement was conducted only with the first redesign of the system. The balance was connected to ProCoDA to measure the change in mass. The volumetric flow rate of the PACl coagulant entering the fluoride system was measured at several height differences (Figure 13).

<img src="PACl vs height gravity.PNG">

**Figure 13:** The flow rate of the PACl system was plotted against the change in height between the fluoride constant head tank and the PACl constant head tank. The data exhibits a strong positive correlation, indicating a direct relationship between flow rate and change in height.



The slope of the best fit line of the flow rate of the PACl system versus the difference in height between the fluoride constant head tank and the PACl constant head tank graph was calculated to be $7.9*10^{-4} mL*s^{-1}*cm^{-1}$, demonstrating the flow rate of PACl flowing into the fluoride system increases by $7.9*10^{-4}$ mL/s per cm of height difference raised.

#### Volumetric Method: Second Redesign of System
Using a 10 mL graduated cylinder, the flow rate of the PACl entering the fluoride system was also determined by measuring the time the PACl coagulant took to drip into the fluoride system to a volume of 2 mL. This was only conducted with the second redesign of the system. The flow rate of the PACl entering the fluoride system was measured while varying the height difference between the fluoride constant head tank and the PACl constant head tank and doing three trials for each height difference. The data also exhibits a strong positive correlation indicating a direct relationship between flow rate and the difference in height between the coagulant constant head tank and the fluoride constant head tank (Figure 14).

<img src="PACl vs height volume.PNG">

**Figure 14:** The flow rate of the PACl system versus the difference in height between the fluoride constant head tank and the PACl constant head tank graph displaying a strong correlation between flow rate and change in height.

The slope of the best fit line of the flow rate of the PACl system versus the difference in height between the fluoride constant head tank and the PACl constant head tank graph was calculated to be $1.28*10^{-3} mL*s^{-1}*cm^{-1}$, which demonstrates the flow rate of PACl flowing into the fluoride system increases by $7.9*10^{-4}$ mL/s per cm of height difference raised.

The strong correlation implies that the relationship in the decoupled system operates in the same manner as the previously linked system with the IV drip chamber.

#### Comparison Between Gravimetric Method and Volumetric Method
The value of the coefficient of determination, $R^2$, was higher in the volumetric analysis graph (Figure 14) than the $R^2$ value of the gravimetric analysis graph of the PACl flow rate versus height (Figure 13). Therefore, the data collected from volumetric method is more accurate because **[Check grammar here]RESOLVED** the mass balance's readings was rounded to the hundredths place. This decreased the accuracy of the data measurement, as miniscule droplets of PACl are released per minute compared to the large volume of PACl stock solution resting on the mass balance. Also, the mass balance scale only measured the change in mass when the float valve in the constant PACl head tank opens, which gives inaccurate results as the float valve opens only when the water level drops. The mass does not change when the water level is level with the valve. Therefore, the change in mass is not constant which provides inaccuracy in the measurements.  However, the gravimetric method used ProCoDA and a mass balance with automated time and mass readings while the volumetric analysis was estimated with the human eye and timed manually, which accounted for human error. As a result, several trials were done to increase the accuracy and precision of the measurement of the volumetric flow rate of PACl entering the fluoride system.

The determination of the coagulant flow rate was used to control and optimize the concentration of PACl entering the fluoride system.


#### Determining Binding of PACl: First Redesign of System
The system was run in reverse, with red dye run through the PACl system to determine the extent of mixing. PACl solution was added to the fluoride system to determine the extent of coagulation and whether the solution would successfully flocculate. The system was run with a upflow velocity of 0.76 mL/s.

The red dye appeared to coagulate at the surface of the constant head tank. The water entering the flocculator was less red than the water in the constant head tank, implying that precipitation occurred in the constant head tank, disallowing flocculation to occur.

#### Determining Binding of PACl: Second Redesign of System
The system was run in the correct orientation, with the red dye run through the fluoride tanks and PACl run through the PACl stock tanks. The PACl stock concentration was 1000 mg/L. The system was run at an upflow velocity of 0.48 mL/s.

The red dye was able to bind with PACl in the flocculator, allowing for successful flocculation.

### Conditions for Flocculation
In the first redesign of the system in which the microbore tubing dripped directly into the fluoride constant head tank, it was observed that no flocs or precipitates were observed when the system was run at the previously successful effluent flow rate of 0.76 mL/s. It was observed that the water exiting the effluent line had a large red dye concentration, suggesting an inability of PACl to bind with red dye at this high velocity.

When the system was run at 0.10 mL/s, a significantly lower velocity, small precipitates were observed. However, when the system was run at 0.13 mL/s, very large precipitates were observed in the flocculator (Figure 15).

<img src="floc 224.gif">

**Figure 15:** At an effluent flow rate of 0.13 mL/s, flocculation was able to occur in the first redesign of the gravity powered system.

The implications of this result are the following:
The system must be run at a sufficiently low velocity that binding is able to occur but at a sufficiently high velocity that the number of collisions are maximized.
The system was sensitive to minute changes in the effluent velocity, indicating that there was a narrow optimal range with which the system was able to properly function.

The ideal concentrations of PACl was thought to be modelled by the following Python program:
```python
import math as m
import numpy as np
from aguaclara.play import*

#Input the desired concentration of PACl through the system
Conc_PACl_exp = 40 * (u.milligram / u.liter)
#Input the desired upflow velocity in the sedimentation tube
upflow_velocity = 1.5 * (u.millimeter / u.second)

#Input your concentrations of your stock tanks
Conc_PACl_stock = 1000 * (u.milligram / u.liter)
Conc_fluoride_stock = 100 * (u.milligram / u.liter)

#Diameter of sedimentation tube
D_sed_tube = 1*u.inch
#Cross sectional area of sedimentation tube
Area_sed_tube = np.pi*(D_sed_tube**2)/4

#Calculate flow rate of system and input units of mL/s
Q_system = Area_sed_tube * upflow_velocity
Q_system.to(u.milliliter/u.second)
#Calculate the flow rate of PACl through the relation Q(PACl)*C(PACl)=Q(system)*C(system), where Conc_PACl_exp is the concentration of PACl in the system
Q_PACl = (Q_system * Conc_PACl_exp / Conc_PACl_stock).to(u.milliliter/u.second)
print(Q_PACl)

#Calculate the flow rate of fluoride through the relation Q(system)=Q(fluoride)+Q(PACl)
Q_fluoride = (Q_system-Q_PACl)
#Calculate the concentration of fluoride through the relation Q(system)*C(system)=Q(fluoride)*C(fluoride), where conc_fluoride_exp is concentration of fluoride in the system
conc_fluoride_exp = Conc_fluoride_stock * Q_fluoride / Q_system
print(conc_fluoride_exp)
```
**[Make better use of comments to walk reader through each of your lines of code.]**

In the second redesign of the experiment, this Python program was used to determine the ideal flow rate of PACl using an ideal concentration of PACl through the system, which was then mapped to the correct height using Figure 7. It was previously found that the ideal PACl concentration ranged from 10 mg/L to 50 mg/L; thus, the experiment was selected to run at a system concentration of 40 mg/L of PACl. The calculated flow rate of PACl that yielded this concentration was 0.34 mL/s, which corresponded to a height of 10cm (Figure 12). Under these conditions, it was found that a effluent flow rate of 0.48 mL/s yielded the largest flocs (Figure 16).

<img src="floc 310.gif">

**Figure 16:** At an effluent flow rate of 0.48 mL/s and PACl flow rate of 0.34 mL/s, large flocs were observed in the flocculator of the second redesign of the system.

However, more tests must be done to conclude whether the ideal experimental concentrations of PACl correspond with the determined concentrations of PACl modelled by the Python program, and how the concentration of PACl through the system and the effluent velocity work together to cause flocculation.

### Jar Testing: Results and Analysis
With the independently mixed solution, it was observed that the solution was first homogenous, but after some time, small particles similar to flocs were observed to form. When these flocs were allowed to settle, the majority of these flocs settled to the bottom, with only a small amount of flocs remaining on the surface of the water.

On the other hand, with the solution collected from the flocculator, it was observed that the majority of the flocs rose to the top of the solution rather than sinking (Figure 17).

<img src="jar 310.gif">

**Figure 17:** The mechanics of the red dye are shown. The beaker on the left contains the solution acquired after flocculation and the beaker on the right contains the solution created through rapid stirring.

When both solutions were stirred once more with a magnetic stir bar, both solutions behaved in the same way. The majority of particles then settled, with a few floating to the top.

This seems to suggest that the flocculation process causes the water to act in a different manner than in normal mixing. It was hypothesized that a difference in pH may prevent mixing and the proper settling of flocs. However, when using pH strips that range between 1 and 14, the pH of both solutions were found to be approximately 8 (Figure 18 and 19).

<img src = "pH Flocculator.jpg" height = "350" width = "300">

**Figure 18:** The pH of the solution collected from the flocculator sample was estimated to be 8 using a pH strip.

<img src = "pH Independent.jpg" height = "350" width = "300">

**Figure 19:** The pH of the independently mixed solution was also estimated to be 8 using a pH strip.

Both the independently mixed solution and solution collected from the flocculator had the same pH value, which rules out the difference in pH potentially altering the mechanics of red dye, but the Fluoride Gravity team will verify this result using more sensitive pH strips or a pH meter.

When the apparatus was tested again with newly created red dye solution, the problem of small red dye flocs floating to the surface of the water in the sedimentation tube did not reoccur. However, more investigations should be done on this phenomenon to fully understand the mechanisms of binding and to prevent future problems from occurring.


### Determination of Effluent Flow Rate
In all prior experiments, the effluent flow rate was manually measured each time with a graduated cylinder. A curve based on the change in height of the effluent tube and the flow rate was established in order determine the flow rate of the system more easily.

To establish this curve, the effluent flow rate of the entire system was determined volumetrically. The team changed the height of the effluent pipe leaving the sedimentation height from 5 cm to 40 cm, with intervals of 5 cm. At each particular height, a 10 ml graduated cylinder was used to measure the volume of effluent water leaving the system in a particular period of time. Three trials were conducted and an average effluent flow rate was calculated, per height. At the end, the data was input into excel where a line of best-fit was determined to measure the effluent flow rate at varying heights (Figure 20).

<img src="Effluent Flow Rate.png">

**Figure 20:** The effluent flow rate graph determined volumetrically from a height difference of 0 to 40 cm from the point of zero flow.

When running the system at approximately 0.48 mL/s (with the effluent pipe located at the 10 cm mark), the system was noted to generate large flocs within the flocculator, indicating that the particular speed of the system seemed to be working appropriately. Even when the system’s velocity was decreased to 0.34 mL/s, large flocs were still forming.

In light of this, the team decided to increase the effluent velocity of the system to analyze the impact of making the system faster. As a result, smaller flocs were noted to form, even to the point that the flow rate became too fast for significant flocs to form (flow rate > 30 cm).

However, from previous research, it was noted that a flow rate of 0.76 mL/s has been the most effective at floc formation as well as speed/efficiency of the system.

Yet, upon re-testing the system after determining the optimal effluent flow rate, as well as with other flow rates that previously worked (e.g. 0.48 mL/s, 0.38 mL/s, etc.), the system failed to flocculate. It was noted that the dye seemed to be lighter than usual, as well as the dye continued to clump within the sedimentation tank. As a result, the team will be re-running the system after replacing the PACl and red-dye solutions and re-record results.

## Future Work

The overarching goal of the Fluoride Gravity team is to determine the optimal method of removing fluoride from the water and creating the most compact system possible to be used for field testing. Future goals involve determining a mechanism to remove flocs from water, since it was observed that they do not fall into the floc weir. To do this, the jar experiments should be replicated and the pH should be tested to better understand the mechanisms of binding to determine the next steps.  

Since red dye was able to successfully bind to PACl in flocculation, indicating that the apparatus provides the correct mechanics for flocculation, tests should move onto using fluoride to determine whether fluoride will also bind to PACl.

If fluoride tests are proven successful, efforts should move to creating an Onshape model for future deployment of the system in field testing.

## Conclusion

At too low of a flow rate of PACl entering the system, it was observed the precipitate formed was too small and the system velocity was too slow to have sufficient collisions for effective flocculation.

At too high of a flow rate of PACl entering the fluoride system, there were no precipitates formed and the effluent leaving the system contained both the PACl and red dye in solution.

The optimal flow rate of PACl entering the fluoride system was found in between the two extremes where the fluid is flowing at a high velocity to maximize collisions but not too high of a velocity such that the flocs break up. This velocity ranged from 0.45 mL/s to 0.76 mL/s.

The successful flocculation of red dye experiments imply that fluoride can be separated from tap water using the reported experimental system and optimized so that the concentration of PACl entering the fluoride system is minimized. Once the experimental design is tested several times and able to be modeled optimally at all times, the design can be sent to communities with high concentrations of fluoride in their tap water for field testing and ultimately for water treatment to remove fluoride from drinking water systems.

## Bibliography
Akpan, P., Mehrabyan, T,. Sausele, D., & Zhang, V. (2018). Fluoride, Spring 2018. Retrieved from https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md.

Bhattacharya, P., & Samal, A. (2018, April). Fluoride contamination in groundwater, soil and cultivated foodstuffs of
India and its associated health risks: A Review. Research Journal of Recent Sciences, 7(4),36-47. Retrieved from http://www.isca.in/rjrs/archive/v7/i4/6.ISCA-RJRS-2018-028.pdf.
Bureau of Indian Standards. (2012). IS 10500: Drinking water. Retrieved from https://archive.org/details/gov.in.is.10500.2012/page/n3.

EPA Method 9214. (1996, December). Retrieved from https://www.epa.gov/sites/production/files/2015-12/documents/9214.pdf.

Gebbie, P. (2001). Using Polyaluminium Coagulants in Water Treatment. Retrieved from http://wioa.org.au/conference_papers/2001/pdf/paper6.pdf.

Herrboldt, J. P. (2016). Fluoride, Natural Organic Matter, and Particles: The Effect of Ligand Competition on the Size Distribution of Aluminum Precipitates in Flocculation. Retrieved from https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1.

Kowalchuk, E. E. (2011). Selective Fluoride Removal by Aluminum Precipitation and Membrane Filtration. Retrieved from https://digitalrepository.unm.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1059&context=ce_etds.

LeChevallier, M. W., & Au, K. (2014, December 10). Water treatment and pathogen control: Process efficiency in achieving safe drinking water. Retrieved from https://www.who.int/water_sanitation_health/publications/9241562552/en/.

Longo, A., Desai, D., & Dao, K. (2016). Fluoride Floc Blanket, Spring 2016. Retrieved from https://drive.google.com/file/d/0B9yahrdDmfVpQ0t0M2NUUkRRNHM/view.

Pang, C., Sarmiento, K., & Tsang, C. (2018). Fluoride Gravity, Fall 2018. Retrieved from https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Fluoride_Grav_Fall2018_Report.md.

Parthasarathy, N., Buffle, J., & Haerdi, W. (1986). Study of interaction of polymeric aluminium hydroxide with fluoride. Canadian Journal of Chemistry, 64(1), 24-29. doi:10.1139/v86-006.

United States, NYC Environmental Protection. (2016). New York City 2016 Drinking Water Supply and Quality Report. New York. Retrieved from http://www.nyc.gov/html/dep/pdf/wsstate16.pdf.

World Health Organization. (2016, August 29). Water-related diseases. Retrieved from http://www.who.int/water_sanitation_health/diseases-risks/diseases/fluorosis/en/.

#Manual

##Experimental Setup
### Set-up
Step 1. Preparing stock solutions
* PACL: dilute PACl stock to yield 2 L of 1000 mg/mL PACl solution
* Red dye: use the dilution factor 100 $\mu$L of Red Dye 40 in 400 mL of water.

Step 2. Filling stock tanks and constant head tanks
* PACl: fill constant head tank with the prepared PACl stock solution until the volume is a small distance below the bottom of the float valve. Use the remainder of the solution to fill the PACl stock tank
* Red dye: fill the fluoride stock tank with red dye. Open the valve and let the constant head tank fill.

Step 3: Filling the flocculator
* Connect a tube from the sink faucet to the flocculator.
* Ensure that the valve to the right of the T junction is closed to prevent backflowing.
* Turn on the sink faucet and let the system fill with water until bubbles do not run through the sedimentation tube.
* Quickly connect the flocculator back to the T-junction, making sure as little air as possible enters the system.

Step 4. Starting the system
* Open the valve to the right of the T junction. Water should be able to flow through the effluent line. If water is unable to flow, connect the flocculator to a tube connected to the sink faucet, and run water through the system until bubbles do not persist.
* After system begins to flow, open the valve below the PACl constant head tank. Shine a flashlight through the tube connected to the T-junction to ensure that PACl is dripping. If the PACl solution does not flow, flick the tube until the flow starts.
* Open the waste line until the flow is slightly slower than the flow out of the effluent line.

###Stopping the System
Step 1. Closing valves
* Ensure that all valves are closed.

Step 2. Adjusting effluent line
* Move effluent line up until it is above the volume level of the fluoride constant head tank.

###Cleaning the System
Step 1. Disconnecting system
* Disconnect the tube below the valve of the PACl constant head tank. Plug the flocculator with a stopper. Open the valve and allow the PACl solution to drain.
* Disconnect the tube connecting the fluoride constant head tank to the fluoride stock tank. Empty the fluoride constant head tank and fluoride stock tank.

Step 2. Cleaning flocculator
* Open the waste line.
* Run water through the system until all flocs have been removed.


##Python Code
###Code for Figure 11: Gravimetric Determination of Flow Rate
Below is the code used to describe the relationship between the change in height of the PACl constant head tank and the effluent flow rate, determined gravimetrically using a mass balance.
```Python
#Gravimetrically Determined Average Flow Rate of PACl vs. Height
#First redesign of system (microbore tubing dripping PACl directly into fluoride constant head tank)

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Change in height of PACl system
height=[5,10,15,20]
#System flow rate measured from effluent
flowrate=[0.00344,0.00894,0.0125,0.01542]

#Plot data points from experiment
plt.plot(height,flowrate,'o')

#Formatting plot
plt.xlabel('Height (cm)')
plt.ylabel('Flow Rate (mL/s)')
plt.title('Gravimetrically Determined Average Flow Rate of PACl')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')

#Calculate linear regression and store stats in variables
linreg=stats.linregress(height,flowrate)
slope,intercept,r_value=linreg[0:3]

#Plot linear regression and legend
xvals=np.arange(0,25,0.01)
yvals=slope*xvals+intercept
plt.plot(xvals,yvals,color='blue',label='y={:.6f}x+{:.6f}\nR\N{SUPERSCRIPT TWO}={:.4f}'.format(slope,intercept,r_value**2))
plt.legend()

plt.show()
```
###Code for Figure 14: Volumetric Determination of Flow Rate
Below is the code used to describe the relationship between the change in height of the PACl constant head tank and the effluent flow rate, determined volumetrically by measuring the time to fill a graduated cylinder to 10 mL.
```Python
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
```

##Code for Figure (): Determination of Effluent Flow Rate
Below is the code used to describe the relationship between the change in height of the effluent tube from the point of zero flow and the effluent flow rate. The effluent flow rate was determined volumetrically by measuring the time to fill a graduated cylinder to 10 mL.
```python
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
```

##Determination of Height Needed for Desired System Concentration of PACl
Below is the code used to determine the flow rate of PACl needed for a desired system concentration of PACl and upflow velocity through the sedimentation tube.
```python
import math as m
import numpy as np
from aguaclara.play import*

#Input the desired concentration of PACl through the system
Conc_PACl_exp = 40 * (u.milligram / u.liter)
#Input the desired upflow velocity in the sedimentation tube
upflow_velocity = 1.5 * (u.millimeter / u.second)

#Input your concentrations of your stock tanks
Conc_PACl_stock = 1000 * (u.milligram / u.liter)
Conc_fluoride_stock = 100 * (u.milligram / u.liter)

#Diameter of sedimentation tube
D_sed_tube = 1*u.inch
#Cross sectional area of sedimentation tube
Area_sed_tube = np.pi*(D_sed_tube**2)/4

#Calculate flow rate of system and input units of mL/s
Q_system = Area_sed_tube * upflow_velocity
Q_system.to(u.milliliter/u.second)
#Calculate the flow rate of PACl through the relation Q(PACl)*C(PACl)=Q(system)*C(system), where Conc_PACl_exp is the concentration of PACl in the system
Q_PACl = (Q_system * Conc_PACl_exp / Conc_PACl_stock).to(u.milliliter/u.second)
print(Q_PACl)

#Calculate the flow rate of fluoride through the relation Q(system)=Q(fluoride)+Q(PACl)
Q_fluoride = (Q_system-Q_PACl)
#Calculate the concentration of fluoride through the relation Q(system)*C(system)=Q(fluoride)*C(fluoride), where conc_fluoride_exp is concentration of fluoride in the system
conc_fluoride_exp = Conc_fluoride_stock * Q_fluoride / Q_system
print(conc_fluoride_exp)
```
Output: Flow rate of PACl is 0.0304 mL/s for a PACL system concentration of 40 mg/L and an upflow velocity of 1.5 mm/s. By using the regression in Figure 14, it was determined that the height of PACl should be 11 cm.
