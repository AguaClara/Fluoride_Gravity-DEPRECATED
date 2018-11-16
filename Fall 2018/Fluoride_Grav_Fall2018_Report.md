# Fluoride Gravity, Fall 2018
#### Cheer Tsang, Kevin Sarmiento, Ching Pang

[EM: Hi team! I will be putting my comments in brackets under the paragragh in which I am referring to. Thanks!]

#### October 24, 2018
This publication Fluoride, Fall 2018 was developed under Assistance Agreement No. SU-83695001 awarded by the U.S. Environmental Protection Agency to Cornell University. It has not been formally reviewed by EPA. The views expressed in this document are solely those of Ching Pang, Kevin Sarmiento, and Cheer Tsang and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication.
 ## Index
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*
 - [Abstract](#abstract)
- [Introduction](#introduction)
- [Literature Review](#literature-review)
- [Previous Work](#previous-work)
- [Methods](#methods)
  - [Experimental Apparatus](#experimental-apparatus)
  - [Head Loss Calculations](#head-loss-calculations)
  - [Measuring Coagulant Flow Rate](#measuring-coagulant-flow-rate)
- [Future Work](#future-work)
- [Bibliography](#bibliography)
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Abstract

Fluoride contamination of drinking water is a common public health issue in some regions of the world such as India. The fluoride teams' overarching goal is to create low cost, compact, and sustainable solutions to fluoride contamination in drinking water. The Fall 2018 Fluoride Gravity team aims to simplify the design of a gravity powered fluoride removal research apparatus that would allow current and future research teams to easily conduct fluoride removal experiments in the field. Experiments conducted with this research apparatus will be used to determine the on-site feasibility of the proposed fluoride removal method.  

[EM: Is your goal to create a research apparatus or go create an apparatus that will successfully remove fluoride in the field?]

[CT: The goal is to create a apparatus that will be used for research purposes only. Then, researchers in the field can use this apparatus to conduct feasibility tests to determine if using our system of coagulation/flocculation/sedimentation to remove fluoride in drinking water is a viable solution in the intended setting. If these tests are successful, then we can start thinking about designing a real fluoride removal system to be used by communities in India. I added a sentence to the abstract and will explain this in more detail in the introduction.]

## Introduction

The expansion of AguaClara Cornell technology to new places around the world, like India, has uncovered new challenges and prompted new goals. The bulk of the AguaClara plants that have been constructed to date are located in Central America where surface waters, such as rivers and lakes, are a major source of water for AguaClara purification plants. These waters have high turbidities due to sediments, Natural Organic Matter (NOM), and other particulate matter. In addition, these waters also carry biological contaminants that can pose serious health threat without proper treatment of water.

In contrast to Central America, 85% of the Indian population obtains their drinking water from groundwater sources such a wells and aquifers ([World Bank, 2017](http://www.worldbank.org/en/news/feature/2012/03/06/india-groundwater-critical-diminishing)). Compared to surface water, groundwater has a much lower turbidity due to natural filtration processes which use the soil and underlying rock material to filter particulate matter from water. While this natural filtration process is capable of removing undissolved particulate matter and pathogenic microorganisms, it also allows minerals and metals to leach from the surrounding geological landscape into the groundwater. The types of contaminants seen in the water of one region depend heavily on the types of parent rock material and soils found in that region. Therefore, there is a lot of variability between regions when it comes to contamination of groundwater with agents such as fluoride.

India is geographically located on one of a number of Fluoride Belts that exists around the world. These are expanses of land that are geologically rich in fluoride and therefore have a much greater capacity to leach fluoride into groundwater [(Water-related diseases, 2016)](http://www.who.int/water_sanitation_health/diseases-risks/diseases/fluorosis/en/). India alone contains about 14% of the total fluoride deposited on the earth's crust  [(Mondal, Dutta, & Gupta, 2016)](https://doi.org/10.1007/s10653-015-9743-7). The coupling of high groundwater fluoride concentrations with a high population dependency on groundwater for consumptions has produced a serious public health problem that needs to be addressed.

There are a number of public health implications associated with both underconsumption and overconsumption of fluoride. One of the risks associated with low exposure to fluoride is an increased development of dental cavities. The American Dental Association has set the recommended concentration of fluoride in drinking water to 0.7 $\mathrm{\frac{mg}{L}}$ in order to prevent the onset of dental cavities [(ADA, 2017)](https://www.ada.org/en/member-center/oral-health-topics/fluoride-topical-and-systemic-supplements). As a result, fluoride has become a common additive to municipal water systems in places such as the United States, where there is little to no fluoride naturally present in the water. New York City, for example, adds fluoride to its water in order to achieve a concentration of 0.7 $\mathrm{\frac{mg}{L}}$ in its effluent water supply [(NYC DEP, 2016)](http://www.nyc.gov/html/dep/pdf/wsstate16.pdf). There are, however, a number of health risks associated with the consumption of fluoride at higher concentrations.

The World Health Organization has set an absolute limit on the concentration of fluoride in drinking water to 1.5 $\mathrm{\frac{mg}{L}}$ in order to minimize the negative impacts of elevated fluoride on human health. Dental fluorosis, the mildest condition caused by the over consumption of fluoride, can begin with water concentrations above 0.9 $\mathrm{\frac{mg}{L}}$. Skeletal fluorosis, a much more serious condition, can begin to develop at fluoride concentrations above 3 $\mathrm{\frac{mg}{L}}$. Lastly, at concentrations above 10 $\mathrm{\frac{mg}{L}}$, crippling skeletal fluorosis will begins to occur  [(WHO, 2004)](http://www.who.int/water_sanitation_health/dwq/chemicals/fluoride.pdf). The number of cases of dental fluorosis, the mildest indicator of excessive fluoride, varies across India, but has been shown to range from 13-91 percent of the total population of some regions [(Arlappa et al., 2013)](http://www.ijrdh.com/files/11.Fluorosis.pdf). In total, it is estimated that 66 million people in India are consuming fluoride contaminated water [(Arlappa et al., 2013)](http://www.ijrdh.com/files/11.Fluorosis.pdf). While there is no established mean fluoride concentration in Indian groundwater, concentrations in some extreme cases have been measured as high as 20 $\mathrm{\frac{mg}{L}}$ in some regions, but most frequently are below 5 $\mathrm{\frac{mg}{L}}$ [(LeChevallier and Au, 2004)](http://www.who.int/water_sanitation_health/publications/9241562552/en/). In order to provide safe drinking water to the people living in these regions of the world effective and feasible fluoride removal technologies need to be developed, which is the overarching goal of the fluoride team.

The Bureau of Indian Standards has created water quality standards designed to protect the public from the adverse effects of fluoride. They have set the upper limit for fluoride at 1 $\mathrm{\frac{mg}{L}}$, and the permissible limit in the absence of an alternate source at 1.5 $\mathrm{\frac{mg}{L}}$ [(Bureau of Indian Standards, 2012)](http://archive.org/details/gov.in.is.10500.2012). AguaClara has set its fluoride standards to match the standards set by the Bureau of Indian Standards and therefore will be striving to achieve an effluent fluoride concentration of 1 $\mathrm{\frac{mg}{L}}$ or lower. The team will be experimenting with stock fluoride concentrations up to 20 $\mathrm{\frac{mg}{L}}$ in order to simulate the highest concentrations these filtration systems may encounter out in the field.

[EM: Although the effects of overconsumption of fluoride is important, it was a bit too detailed for this report. It takes many, many paragraphs to get to the point of this report. It started out as though the purpose was about fluoride effects, not fluoride removal.]

[CT: We condensed the introduction a little, but we believe that providing the background of the issue as well as presenting the consequences of elevated fluoride levels is important in understanding why we are removing fluoride. Please let us know what else we can do to make out point more clear!]

The Fluoride Gravity team's objective this semester was to modify and test the gravity-powered fluoride removal apparatus. The goal was to make it easy to adjust and control key variables such as flow rate, PACl concentration, and fluoride concentration. The gravity-powered apparatus will then be used to conduct feasibility analyses on site, which will determine if the proposed system of fluoride removal is a viable solution in the intended setting. If these tests are successful, AguaClara can begin designing a marketable product that can used by communities in India.

The 2018 Fall Fluoride Gravity team optimized the gravity-powered system by making it compact and easy to operate for field testing and laboratory work. Fluoride removal efficiency of the gravity powered system was compared to that of the automated system. The team also created a fabrication and operation manual of the gravity apparatus for easy operation and future reference. Furthermore, the team strived to gain a general understanding of the mechanisms involved in fluoride removal through literature review and experimentation.

## Literature Review

### Interactions Between Fluoride, Natural Organic Matter (NOM), and Polyaluminum Chloride (PACl)

The dynamic interactions between fluoride, Natural Organic Matter (NOM), and the aluminum based coagulants used in traditional drinking water treatment processes are important to consider when treating water sources containing significant amounts of NOM and fluoride. While many of the sources of water in India come from wells, and therefore the NOM content is generally low, interactions between these three types particles have not been vastly studied. The presence of fluoride reduced the capacity of water treatment systems to remove other contaminants such as turbidity and NOM due to fluoride's capacity to inhibit aluminum hydroxide precipitation [(Herrboldt, 2016)]((https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1)). In the presence of fluoride, aluminum precipitates become smaller in size compared to precipitates created in fluoride-free solutions. Water with fluoride produced more particles with diameters smaller than 10&mu;m. Smaller particles are more difficult to remove during the sedimentation process. These results suggest that removal of fluoride is more than just particulate matter due to the difficulty of settling and filtering of smaller particles in the sedimentation and filtration of water treatment. Tests with both NOM and fluoride also showed similar effects with smaller floc sizes, adding to the difficulty of treatment.

### Effect of pH on Fluoride removal

The difficulty of fluoride removal is also affected by environmental factors. At a pH value below 5, nearly all the fluoride present in fluoride and aluminum based coagulant solution are in the form of a fluoro-aluminum complexation (Gong et al. 2012 in [Herrboldt, 2016](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1)). Such complexation is soluble in water and cannot be removed by coagulation which therefore makes fluoride removal by traditional methods at pH values below 5 unlikely. However, at pH values greater than 8 nearly all fluoride exists freely as fluoride ion, allowing the formation of flocs to occur. While parameters, such as pH can be carefully controlled in the lab, it varies can vary depending on local geology and other chemical factors out in the field. Further research about the expected chemistry of groundwater in regions like India would help the team's overall understanding. For example, if pH is rarely observed to be 5 in groundwater then the effect of pH would also be minimal. However, not enough research have been done to make such assumptions, and the critical pH transition points are also not fully understood yet. Fluoride removal was observed to occur best in a coagulation treatment process when the molar ratio between hydroxide and fluoride was greater than 2.4 [OH<sup>-</sup>]:[F<sup>-</sup>] (Hu et al., 2005). More research should be done to find other critical pH values for effective fluoride removal with aluminum based coagulants.

### Fluoro-aluminium Complexation

The formation of a fluoro-aluminum complex is also responsible for an observed increase in residual aluminum concentration [(Herrboldt, 2016)]((https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1)). Formation of aluminum hydroxide is negatively affected by the presence of fluoro-aluminum, which prevents the formation of larger diameter particles. This reduces the system's capacity to remove both fluoride and residual aluminum. When comparing experiments that contained aluminum coagulant and NOM mixtures with aluminum coagulant and fluoride mixtures, both of which contained aluminum concentration of 8.0 $\mathrm{\frac{mg}{L}}$, the amount of residual aluminum was found to be 0.058$\mathrm{\frac{mg}{L}}$ and 0.244$\mathrm{\frac{mg}{L}}$ respectively. Thus, residual aluminum concentration increased by nearly an order of magnitude when fluoride was present. Unintended residual aluminum release in the effluent water supply from systems can be a concern if fluoride is present in the water.

### Effect of pH on Fluoride Removal

Environmental conditions also increase the difficulty in fluoride removal. At a pH value below 5, nearly all the fluoride present in fluoride and aluminum based coagulant solution are in the form of a fluoro-aluminum complexation (Gong et al. 2012 in [(Herrboldt, 2016)]((https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1))). Such complexation is soluble in water and cannot be removed by coagulation which therefore makes fluoride removal by traditional methods at pH values below 5 unlikely. However, at pH values greater than 8 nearly all fluoride exists freely as fluoride ion, allowing the formation of flocs to occur. While parameters, such as pH can be carefully controlled in the lab, it varies can vary depending on local geology and other chemical factors out in the field. Further research about the expected chemistry of groundwater in regions like India would help the team's overall understanding. For example, if pH is rarely observed to be 5 in groundwater then the effect of pH would also be minimal. However, not enough research have been done to make such assumptions, and the critical pH transition points are also not fully understood yet. Fluoride removal was observed to occur best in a coagulation treatment process when the molar ratio between hydroxide and fluoride was greater than 2.4 [OH<sup>-</sup>]:[F<sup>-</sup>] (Hu et al., 2005). More research should be done to find other critical pH values for effective fluoride removal with aluminum based coagulants.

### Formation of Fluoro-aluminium Complexation

The formation of fluoro-aluminum complexation is also responsible for an observed increase in residual aluminum concentration [(Herrboldt, 2016)]((https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1)). Formation of aluminum hydroxide is negatively affected by the presence of fluoro-aluminum which disallows the formation of larger diameter particles which in return reduces a system's capacity to remove both fluoride and residual aluminum. When comparing experiments that contained aluminum coagulant and NOM mixtures with aluminum coagulant and fluoride mixtures, both of which contained aluminum concentration of 8.0 $\mathrm{\frac{mg}{L}}$, the amount of residual aluminum was found to be 0.058$\mathrm{\frac{mg}{L}}$ and 0.244$\mathrm{\frac{mg}{L}}$ respectively. Thus, residual aluminum concentration increased by nearly an order of magnitude when fluoride was present. This shows that unintended residual aluminum release in the effluent water supply from systems can be a concern.


### Collection and Analysis of Fluoride Samples
In order to measure the fluoride concentration, an Ion-Selective Electrode (ISE) fluoride probe is often used. One of the biggest issues in previous semesters was the inaccuracy of measurements taken by the fluoride probe. In order to mitigate these errors, the following quality-control procedures should be followed.

There are three main critical interferences that can impact the accuracy of the fluoride probe. The first is the presence of polyvalent cations such as Fe<sup>+3</sup> and Al<sup>+3</sup> which form complexes with F<sup>-</sup>. ISE fluoride probes can only detect solubilized fluoride and therefor would give inaccurate fluoride readings when in the presence of Fe<sup>+3</sup> and Al<sup>+3</sup> as is the case when Polyaluminum Chloride (PACl) coagulant is added to our experiments. As a remedy for this interference, Total Ionic Strength Adjuster Buffer (TISAB) solution is added to samples to solubilize the fluoride in the sample. The use of TISAB is also critical in remedying a second source of interference which is pH. TISAB solution is a buffer that keeps the sample at a constant pH of about 5-5.5 to avoid ISE probe interference from hydroxide at high pH and bifluoride formation, undetectable to ISE probe, at lower pH. Lastly, the temperature of the samples can also be a significant source of error in fluoride measurements. In order to collect accurate data, samples should not deviate more than $\pm 1^\circ$C from those used to create the standard curve or from each other ([EPA Method 9214](https://www.epa.gov/sites/production/files/2015-12/documents/9214.pdf)).

Several quality control measures should be taken into consideration, such as the use of containers. The first is the highly recommended use of polyethylene plastic over glassware as fluoride can adsorb to glass, which may result in inaccurate readings. Another quality control measure is the use of an Initial Calibration Verification (ICV) standard and a Continuing Calibration Verification (CCV) standard. These would consist of a solution of known fluoride concentration within the mean expected fluoride concentration that is being tested. The ICV would be utilized as a way to test the accuracy of the calibration curve prior to the analysis of unknown samples. Similarly, The CCV would be use after every 10 samples as a way to check that the fluoride probe has not drifted significantly from the standard curve. Both ICV and CCV controls should be within 10% of their known values. A final quality control measure that is suggested is the use of a blank after each ICV and CCV. The control blank would contain 1 part water and 1 part TISAB to ensure that the fluoride probe was not contaminated in some way with residual fluoride. Implementing these methods can possibly enhance the accuracy of data in future experiments.

## Previous Work

A coagulant-sedimentation process was used to remove fluoride. A series of bench experiments were conducted using polyaluminum chloride (PACl) as the coagulant and varying concentrations of fluoride.

The Spring 2016 team conducted bench tests using clay and PACl, and were able to successfully create a floc blanket. After adding in fluoride, their system was able to remove 85% of the initial fluoride ([Longo, 2016](https://drive.google.com/file/d/0B9yahrdDmfVpQ0t0M2NUUkRRNHM/view)). The Summer 2017 team determined that the addition of clay was unnecessary, since it caused an increase in effluent turbidity ([Akpan et al., 2017](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md)). Thus, the Fall 2017 team ran experiments with only fluoride and PACl, without the addition of clay. They determined that their reactors would fail after 10 hours due to sludge buildup in the reactor. After switching to a new reactor geometry designed by the High Rate Sedimentation 2017 Summer Team (see ["Fabrication Details > Sedimentation Tube"](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md) for fabrication details), the time to failure increased, allowing for higher upflow velocities. Thus, the Fall 2017 team determined that a upflow velocity of 1.5 mm/s was optimal for preventing sludge buildup in the reactor. The team then ran experiments with various PACl concentrations to create an adsorption model, which would allow users to determine an optimal PACl dosage for the influent fluoride concentration.

The Spring 2018 team began constructing a gravity-powered apparatus for fluoride removal ([Akpan et. al, 2018](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md)).

![gravity_schematic](https://github.com/AguaClara/Fluoride-Auto/blob/master/fluoride%20report/Gravity%20Powered%20Reactor%20(2).jpg?raw=true)

**Figure 1:** Schematic for gravity-powered apparatus. The height difference between the effluent of the sedimentation tank and the fluoride constant head tank (h2) determined the flow rate through the system.

The principle behind the design is that the difference in head between the surface of the constant head tank of the influent and the effluent supplies enough potential energy to cause flow through the system. Float valves in the constant head tanks for fluoride and PACl were utilized to keep the water level and thus, the flow, constant throughout the system. The PACl concentration in the coagulant stock tank is fixed. Therefore, the concentration of coagulant into the system is determined by its flow rate. In order to change the PACl concentration throughout the system to accommodate for varying system flow rates, the PACl flow rate is adjusted accordingly.

The Summer 2018 team modified the gravity-powered apparatus fabricated by the Spring 2018 team. Adjustable sliders were added to allow for easy height adjustments of the sedimentation tube, coagulant stock tank, and coagulant constant head tank, and thus adjusting the flow rate of the system (Figure 1) Fabrication details can be found in the [Summer 2018 Final Report](https://github.com/AguaClara/Fluoride-Auto/blob/master/Fluoride_Summer2018.md#sedimentation-tube).

[EM: I still don't see the connection between flow rate and fluoride removal. Is there an optimal flow rate at which removal occurs? Is it to fix the concentration of coagulant? I'm having difficulty understanding why it is necessary to build an apparatus with an adjustable flow rate. Please clarify how this apparatus will be implemented in a plant (or is it independent of a plant? Or is it in tandem with the EStaRS filters in India?)]

[CT: I believe this apparatus will be implemented independent of a plant, since the groundwater being used for drinking water in India is relatively turbidity-free (will double-check this). Since it's gravity powered, the idea is that the concentration of coagulant is fixed; thus, the concentration of coagulant into the system is determined by its flow rate (similar to the way the chemical dose controller works to regulate chlorine dose). The purpose of making it easy to adjust the overall flow rate of the system is that this system will be used for research in the field. When this system is used by researchers on site with real groundwater in India, they can experiment with different flow rates through the system to determine the optimum flow rate for fluoride removal.]

![Gravity powered reactor](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Gravity_system_schematic.png?raw=true)

**Figure 2:** Modified gravity powered reactor shown with 3 adjustable sliders.

The Summer 2018 team also ran a series of bench experiments with varying concentrations of fluoride and PACl to create an adsorption model. Fluoride concentrations ranging from 3 to 20 mg/L and PACl concentrations of 10 to 50 mg/L were tested. Experiments were run on the bench setup utilized by previous semesters (Figure 2).

![Bench_setup](https://github.com/AguaClara/Fluoride-Auto/blob/master/Summer%202018%20fluoride%20report/Bench_setup_new.png?raw=true)

**Figure 3:** Schematic for bench system.

An adsorption model was created using the data from Summer 2018 by the [Fall 2018 Fluoride Auto team](https://github.com/AguaClara/Fluoride-Auto). The effluent concentration of fluoride in mmol/L was plotted against the fluoride uptake (amount adsorbed) in mmol/g. Data points at 1.5 hr were selected from each experiment, at each fluoride and PACl concentration tested.

A Langmuir Isotherm was then fitted to the data, using the following equation:

$$ \frac{C_e}{q_e} = \frac{1}{q_e}C_e+\frac{1}{K_L\cdot q_m} $$

where $C_e$ is the equilibrium concentration of the adsorbant, $q_e$ is the amount adsorbed at equilibrium, and $K_L$ and $q_m$ are Langmuir constants which are related to adsorption capacity and energy of adsorption.

An R-squared value of 0.7611 was observed, indicating a relatively accurate fit of the Langmuir adsorption model and the experimental data. For more information on the adsorption model, see the [2018 Fluoride Auto Final Report](https://github.com/AguaClara/Fluoride-Auto/blob/master/Fall%202018/Automated%20System/Fall_2018_Report.md).

![langmuir](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/langmuir_isotherm.png?raw=true)

**Figure 4:** Langmuir isotherm fitted to experimental data from Summer 2018. Model created by [Spring 2018 Fluoride Auto team](https://github.com/AguaClara/Fluoride-Auto/blob/master/Fall%202018/Automated%20System/Fall_2018_Report.md).

In Fall 2018, two fluoride teams were created: [Fluoride Auto](https://github.com/AguaClara/Fluoride-Auto) focused on creating an adsorption model by running bench experiments, and [Fluoride Gravity](https://github.com/AguaClara/Fluoride_Gravity) focused on optimizing the gravity-powered apparatus.

## Methods

### Experimental Apparatus

The gravity-powered apparatus was constructed using 80/20 T-slotted aluminum bars (Figure 2). (We will put the final setup here, once we have finished the calculations as detailed below)

### Head Loss Calculations

The flow rate through the gravity-powered apparatus depends on piezometric head. Thus, by altering the height differences in the system, flow rate can be manually adjusted (Figure 4, Figure 5).  

#### System Flow Rate

Water in the gravity-powered system flows from the fluoride stock tank, to the fluoride constant head tank, to the flocculator, up the sedimentation tube, and out the effluent line.

![Systemflowrate](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/system_flow_2.png?raw=true)

**Figure 5:** The system flow rate is determined by the height difference between the water level of the fluoride constant head tank and the effluent line. The height difference, and thus the flow rate, can be controlled by the adjustable slider on effluent line.

There are multiple sources of head loss in this system: major head loss in the tubing and minor head loss in the flocculator.

To find major head loss in the straight sections of tubing we will be utilizing the Hagen–Poiseuille equation:

$\Delta H_1 =\frac{32\mu LV}{\rho gd^2}$

Where $L$ is the length of the tube, $V$ is the bulk velocity of the system, and $d$ is the diameter of the tubing.

To find the head loss in the coiled flocculator we will utilize the following equation:

$\Delta H_2 = \frac{32\mu VL}{\rho gd^2} 0.37 De^{0.36}$

**citation**

Where $De$ is the Dean Number, found experimentally by C.M White. It is a dimensionless quantity that establishes a relationship between the inertial, centripetal, and viscous forces in a fluid, and is used to find the pressure drop in a coiled tube. It represented by the following expression:

$De=Re\sqrt\frac{D}{d}$

Where $Re$ is the Reynolds Number:

$Re=\frac{\rho VL}{\mu }$

Therefore,

$\Delta H_2 = \frac{32\mu VL}{\rho gd^2} 0.37 (\frac{\rho VL}{\mu }\sqrt\frac{D}{d})^{0.36}$

The total head loss for the system flow rate will be:

$\Delta H_{tot}=\Delta H_1 + \Delta H_2$

#### Coagulant Flow Rate

![PAClflowrate](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/headloss_diagram2.png?raw=true)
**Figure 6:** The flow rate of PACl is determined by the height difference between the water level of the fluoride constant head tank and the water level of the coagulant constant head tank. The height of the PACl constant head tank can be adjusted, which allows for user control of the PACl flow rate.

To calculate the required height difference between the water level of the fluoride constant head tank and the water level of the coagulant constant head tank, the following equations were used:

First, the energy equation was applied from the PACl constant head tank to the connection junction point at $H_3$. Note that the tubing used to connect to the PACl tank is microbore tubing.

$\frac{P_C}{\gamma} + \frac{V_C^2}{2g} + H_1 = \frac{P_D}{\gamma} + \frac{V_D^2}{2g} + H_3 + H_f$

* The $\frac{P_C}{\gamma}$ term can be ignored since the container is open to the atmosphere so gauge pressure at C is zero.

* $\frac{V_C^2}{2g}$ also drops out because the velocity at point C is zero due to a float valve that keeps the water level constant.

Applying these assumptions, the following expression was obtained:

 1) $H_1 - H_3 = \frac{P_D}{\gamma } + \frac{V_D^2}{2g} +H_f$

Then, the Bernoulli Equation was applied from the fluoride constant head tank to the connection junction. This was done assuming that the head loss from the tubing was negligible since it has a diameter of $\frac{1}{4}$ inches and its length is very small.

$\frac{P_A}{\gamma}+ \frac{V_A^2}{2g} + H_2 = \frac{P_B}{\gamma} + \frac{V_B^2}{2g} + H_3$

* Similarly, the $\frac{P_A}{\gamma}$ term can be ignored since the container is open to the atmosphere so gauge pressure at A is zero.

* $\frac{V_A^2}{2g}$ also drops out because the velocity at point A is zero due to a float valve that keeps the water level constant.

Applying these assumptions, the following is obtained:

2) $P_B= \gamma(H_2-H_3 -\frac{V_B^2}{2g})$

The pressures going into the junction were assumed to be equal:

3) $P_B =P_D$

Combining equations 1, 2 and 3, the following expression is obtained:

$H_1 - H_3 = \frac{\gamma(H_2-H_3 -\frac{V_B^2}{2g})}{\gamma } + \frac{V_D^2}{2g} +H_f$

Which can be simplified to:

$H_1 - H_2 = -\frac{V_B^2}{2g} + \frac{V_D^2}{2g} + H_f$

Where $H_f$ is described by the Hagen–Poiseuille equation, since the microbore tubing consists of a length that is much greater than its diameter:

$\frac{32\mu LV_D}{\rho gd^2}$

Thus, the desired head for the PACl tank is:

$\Delta h = -\frac{V_B^2}{2g} + \frac{V_D^2}{2g} + \frac{32\mu LV_D}{\rho gd^2}$

Additionally, using the desired fluoride flow rate through the system of 0.76 mL/s, and desired maximum PACl flow rates (which was estimated to be 1% of the system flow rate), it was determined that both $\frac{V_B^2}{2g}$ and $\frac{V_D^2}{2g}$ are less than 1% of total head loss and therefore can be ignored.

 Finally, the height difference between the coagulant constant head tank and the fluoride constant head tank is given by:

 $\Delta h = \frac{32\mu LV_D}{\rho gd^2}$

#### Python Code

A [Python function](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/gravity_fluoride_setup.md) was created with the headloss equation derived above. The user can input the flow rate of the system and the desired flow rate of coagulant, and the function will output the required height difference between the fluoride constant head tank and the coagulant constant head tank.

```python
import math as m
import numpy as np
from aide_design.play import*
G = 9.80665 * u.m/u.s**2
"""Define the gravitational constant, in m/s²."""
  #@u.wraps(u.m**2, u.m, False)

def required_height(q_sys, d_sys, d_micro, l_micro, q_PACl):
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
  T=298*u.K
  mu = pc.viscosity_dynamic(T)
  rho = pc.density_water(T)
  print(mu)
  print(rho)

  #calculate cross-sectional area of microbore tubing
  a_micro = pc.area_circle(d_micro)
  #calculate cross-sectional area of system tubing
  a_sys = pc.area_circle(d_sys)
  #calculate required height difference
  #This equation was derived from the modified Bernoulli equation, accounting for head loss due to friction through the microbore tubing.
  delta_h = -1/(2*G)*((q_sys-q_PACl)/a_sys)**2 + ((q_PACl/a_micro)**2)/(2*G) + (32*mu*l_micro*(q_PACl/a_micro))/(rho*G*d_micro**2)

  return(delta_h)

q_sys = (0.76*u.mL/u.s).to(u.m**3/u.s)
d_sys = (3/16*u.inch).to(u.m)
d_micro = (0.022*u.inch).to(u.m)
l_micro = (78*u.cm).to(u.m)
q_PACl = (0.0076*u.mL/u.s).to(u.m**3/u.s)

required_height(q_sys, d_sys, d_micro, l_micro, q_PACl)

```

### Measuring Coagulant Flow Rate
Since the flow rate of coagulant is very small, it is difficult to measure and verify that the experimental flow rates are within range of the mathematically derived flow rates. The team came up with several solutions to easily measure the flow rate of coagulant.

#### Balance

A balance was added to the bottom of the coagulant stock tank to verify coagulant flow rate (Figure 7). The balance measures the mass flow rate out of the coagulant stock tank. As coagulant flows out of the coagulant stock tank into the coagulant constant head tank, the balance measures the rate of mass decrease over time. The mass flow rate can then be converted to volumetric flow rate to obtain the flow rate of coagulant through the system.


![balance_system](https://github.com/AguaClara/Fluoride-Auto/blob/master/Summer%202018%20fluoride%20report/Gravity_reactor_PACl_adjustable_edit.jpg?raw=true)

**Figure 7:** The balance was placed under the coagulant stock tank and was used to measure the change in mass over time as the coagulant flows from the stock tank to the constant head tank.

The balance was connected to ProCoDA, and the mass over time was recorded (Figure 8).

![mass_flow](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Mass_Coagulantflow.png?raw=true)

**Figure 8:** The mass flow of coagulant from the coagulant stock tank over time. The slope of the graph was -0.0019, which indicates that the mass flow rate was 1.9 mg/s. The graph appears stepwise because the balance only has a precision of 0.1 g.

The recorded mass flow rate of coagulant can then be converted to volumetric flow rate using a density relationship. However, accuracy with this flow rate measuring technique was suspected to be low. The reason for this was the uncertainty in the ability of the float valve to respond to the low flow rates that we were working with. This uncertainty prompted the introduction of second method for measuring flow rate out of the PACl constant head tank, the IV drip chamber.

#### IV Drip System

Another proposed method to measure and regulate coagulant flow rate was to use an intravenous (IV) system (Figure 11). The idea is that the user would be able to easily measure the flow rate by counting the amount of drops that fall within a given time period. Most IV drip chambers specify the number of drops that equal a milliliter of water; the current setup uses a drip chamber with 20 drops per milliliter. This would allow the user to convert drops per unit time to mL per unit time to get a flow rate and it also serves to check the results of the scale.

Flow measurements were taken to verify the method of counting drops to determine flow rate. In order to do this, the team timed the amount of time it took for 20 drops to fall in the drip chamber. Since the IV drip chamber specified 20 drops per milliliter, the flow rate was calculated by dividing 1 mL by the recorded time. The calculated flow rates can be found
[here](https://docs.google.com/spreadsheets/d/1IfbS2UFp3Ce4mH5M0O0il0AwW0HiAQ8-2CF-pYxHCLg/edit?usp=sharing).

The first iteration of this system consisted of the drip chamber connected to a 90$\degree$ elbow that was attached to the constant head tank. While running experiments with this setup, it was observed that air bubbles became trapped in the elbow. This caused the flow rates to vary drastically between tests. This prompted the team to alter the drip chamber design to improve reproducibility.  

<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/iv_system.jpg?raw=True" height=500>

**Figure 11:** The IV drip chamber was added after the PACl constant head tank.

## Results and Analysis

blah

## Future Work

After the implementation of the new PACl constant head tank experiments will be rerun to determine the flow rates at different platform heights. Further microbore tubing lengthening or shortening can then be done in order to optimize the system as a whole.

[EM: Both paragraphs are too informal.]

## Conclusions
Explain what you have learned and how that influences your next steps. Why does what you discovered matter to AguaClara?

Make sure that you defend your conclusions with facts and results.

## Bibliography

EPA (2018) [EPA Method 9214](https://www.epa.gov/sites/production/files/2015-12/documents/9214.pdf)

Herrboldt, J. P. (2016)["Fluoride, Natural Organic Matter, and Particles: The Effect of Ligand Competition on the Size Distribution of Aluminum Precipitates in Flocculation."](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1)



###add previous fluoride report as citation, add all other citations



# Manual
The manual provides details on how to construct and operate the gravity-powered fluoride removal apparatus.

## Fabrication Details
The frame of the apparatus was built using metal 80/20 bars.

### Frame

### Stock Tanks
something about tanks for fluoride and PACL

### Tubing
something about tubing

### Flocculator
something about flocculator

### Reactor
something about reactor


add pictures and measurements (maybe make a schematic idk)

## Special Components
If your subteam uses a particular part that is unique and you could foresee a future subteam needing to order it or learn more about it, please include basic information like the vendor where it was purchased, catalog/item number, and a link to any documentation.

### Sliding Tracks

something about sliders

### IV Drip Chamber
maybe add links for sliders/IV chamber

## Experimental Methods
### Set-up
Step 1.
* Put tasks in a sequential order.
* It is okay to have sub-lists.
  - Like this.

### Experiment
Step 1.

### Cleaning Procedure
Step 1.

## Experimental Checklist
Another potential section could include a list of things that you need to check before running an experiment.

**END OF DRAFT 2**



***

### Procedure
Discuss your experimental procedure. How did you run your experiment? What were you testing? What were the values of relevant parameters?

## Results and Analysis
Present an observation (results), then explain what happened (analysis).  Each paragraph should focus on one aspect of your results. In that same paragraph, you should interpret that result.  
In other words, there should not be two distinct paragraphs, but instead one paragraph containing one result and the interpretation and analysis of this result. Here are some guiding questions for results and analysis:

When describing your results, present your data, using the guidelines below:
* What happened? What did you find?
* Show your experimental data in a professional way.
```python
from aide_design.play import*
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
plt.figure('ax',(10,8))
plt.plot(x,y,'*')
plt.savefig('/Users/jillianwhiting/github/Jillian-Whiting/Images/linear')
plt.show()
```
![linear](https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/linear.png?raw=true)
Figure 1: Captions are very important for figures. Captions go below figures.

### Figure requirements
 - Create the graph using python (not Excel)
 - If the x axis is time then make zero time reflect the beginning of the test.
 - Use a white background for all graphs.
 - Most data will have both x and y values and thus should be presented using an xy scatter plot.
 - Label all axes and include units where appropriate.
 - Axis scale labels should be in the margin of the graph and not inside the graph border.
 - Eliminate parts of the range in both x and y axis that aren't used or that aren't meaningful.
 - Place a caption with a brief description below the graph. Add this caption using the wiki formatting, not in your graphing software.
 - Use data symbols to show data points unless there is so much data that the symbols overlap. If the data symbols overlap it is better to connect the data points with a line and not show the data symbols.
 - When presenting multiple plots on a single graph make sure that it is easy to distinguish the plots using the legend.
 - If curve fitting is used explain why and include the equation (elsewhere in the report).
 - If a model or theoretical curve is presented it should be a smooth curve without data points.
 - Use the same font in the graphs as you use in the text of the report.
 - Insert the graph in your report after the first reference to it in the text. Inserted the graph after the next paragraph break
 - Scale the size of the graph so it is large enough to see the data and read the text without having to follow a link to see a larger image. Avoid using hyperlinks on images because that causes the export to Microsoft Word option to not include the image.

After describing a particular result, within a paragraph, go on to connect your work to fundamental physics/chemistry/statics/fluid mechanics, or whatever field is appropriate. Analyze your results and compare with theoretical expectations; or, if you have not yet done the experiments, describe your expectations based on established knowledge. Include implications of your results. How will your results influence the design of AguaClara plants? If possible provide clear recommendations for design changes that should be adopted. Show your experimental data in a professional way using the following guidelines:
* Why did you get those results/data?
* Did these results line up with expectations?
* What went wrong?
* If the data do not support your hypothesis, is there another hypothesis that describes your new data?



## ProCoDA Method File
Use this section to explain your method file. This could be broken up into several components as shown below:

### States
Here, you should describe the function of each state in your method file, both in terms of its overall purpose and also in terms of the details that make it distinct from other states. For example:
\begin{itemize}
\item \underline{OFF} - Resting state of ProCoDA. All sensors, relays, and pumps are turned off.
\end{itemize}

### Set Points
Here, you should list the set points used in your method file and explain their use as well as how each was calculated.



```python
# To convert the document from markdown to pdf
pandoc Fluoride_Grav_Fall2018_Report.md -o Fluoride_Gravity_Research_Report.pdf
```
