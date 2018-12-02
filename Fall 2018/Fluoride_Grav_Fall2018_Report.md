# Fluoride Gravity, Fall 2018
#### Cheer Tsang, Kevin Sarmiento, Ching Pang

[EM: Hi team! I will be putting my comments in brackets under the paragragh in which I am referring to. Thanks!]

#### November 16, 2018
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
    - [System Flow Rate](#system-flow-rate)
    - [Coagulant Flow Rate](#coagulant-flow-rate)
    - [Python Code](#python-code)
  - [Measuring Coagulant Flow Rate](#measuring-coagulant-flow-rate)
    - [Balance](#balance)
    - [IV Drip System](#iv-drip-system)
- [Future Work](#future-work)
- [Conclusion](#conclusion)
- [Bibliography](#bibliography)
- [Manual](#manual)
  - [Fabrication Details](#fabrication-details)
    - [Frame](#frame)
    - [Stock Tanks](#stock-tanks)
      - [PACl Tank Platforms](#pacl-tank-platforms)
      - [Fluoride Tank Platforms](#fluoride-tank-platforms)
    - [Tubing](#tubing)
    - [Flocculator](#flocculator)
    - [Reactor](#reactor)
  - [Special Components](#special-components)
    - [Adjustable Sliders](#adjustable-sliders)
    - [IV Drip Chamber](#iv-drip-chamber)
  -[Operation Manual](#operation-manual)
    - [Set-up](#set-up)
    - [Cleaning Procedure](#cleaning-procedure)
  - [Experimental Checklist](#experimental-checklist)
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

The Spring 2016 team conducted bench tests using clay and PACl, and were able to successfully create a floc blanket. After adding in fluoride, their system was able to remove 85% of the initial fluoride ([Longo, 2016](https://drive.google.com/file/d/0B9yahrdDmfVpQ0t0M2NUUkRRNHM/view)). The Summer 2017 team determined that the addition of clay was unnecessary, since it caused an increase in effluent turbidity ([Akpan et al., 2017](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md)). Thus, the Fall 2017 team ran experiments with only fluoride and PACl, without the addition of clay. They determined that their reactors would fail after 10 hours due to sludge buildup in the reactor. After switching to a new reactor geometry designed by the High Rate Sedimentation 2017 Summer Team, the time to failure increased, allowing for higher upflow velocities. Thus, the Fall 2017 team determined that a upflow velocity of 1.5 mm/s was optimal for preventing sludge buildup in the reactor. The team then ran experiments with various PACl concentrations to create an adsorption model, which would allow users to determine an optimal PACl dosage for the influent fluoride concentration.

The Spring 2018 team began constructing a gravity-powered apparatus for fluoride removal ([Akpan et. al, 2018](https://github.com/AguaClara/Fluoride-Auto/blob/master/FluorideReportSp18.md)).

![gravity_schematic](https://github.com/AguaClara/Fluoride-Auto/blob/master/fluoride%20report/Gravity%20Powered%20Reactor%20(2).jpg?raw=true)

**Figure 1:** Schematic for gravity-powered apparatus. The height difference between the effluent of the sedimentation tank and the fluoride constant head tank (h2) determined the flow rate through the system.

The principle behind the design is that the difference in head between the surface of the constant head tank of the influent and the effluent supplies enough potential energy to cause flow through the system. Float valves in the constant head tanks for fluoride and PACl were utilized to keep the water level and thus, the flow, constant throughout the system. The PACl concentration in the coagulant stock tank is fixed. Therefore, the concentration of coagulant into the system is determined by its flow rate. In order to change the PACl concentration throughout the system to accommodate for varying system flow rates, the PACl flow rate is adjusted accordingly.

The Summer 2018 team modified the gravity-powered apparatus fabricated by the Spring 2018 team. Adjustable sliders were added to allow for easy height adjustments of the sedimentation tube, coagulant stock tank, and coagulant constant head tank, and thus adjusting the flow rate of the system (Figure 1).

[EM: I still don't see the connection between flow rate and fluoride removal. Is there an optimal flow rate at which removal occurs? Is it to fix the concentration of coagulant? I'm having difficulty understanding why it is necessary to build an apparatus with an adjustable flow rate. Please clarify how this apparatus will be implemented in a plant (or is it independent of a plant? Or is it in tandem with the EStaRS filters in India?)]

[CT: I believe this apparatus will be implemented independent of a plant, since the groundwater being used for drinking water in India is relatively turbidity-free (will double-check this). Since it's gravity powered, the idea is that the concentration of coagulant is fixed; thus, the concentration of coagulant into the system is determined by its flow rate (similar to the way the chemical dose controller works to regulate chlorine dose). The purpose of making it easy to adjust the overall flow rate of the system is that this system will be used for research in the field. When this system is used by researchers on site with real groundwater in India, they can experiment with different flow rates through the system to determine the optimum flow rate for fluoride removal.]

<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Gravity_system_schematic.png?raw=true" height=500>

**Figure 2:** Modified gravity powered reactor shown with 3 adjustable sliders.

The Summer 2018 team also ran a series of bench experiments with varying concentrations of fluoride and PACl to create an adsorption model. Fluoride concentrations ranging from 3 to 20 mg/L and PACl concentrations of 10 to 50 mg/L were tested. Experiments were run on the bench setup utilized by previous semesters (Figure 2).

<img src="https://github.com/AguaClara/Fluoride-Auto/blob/master/Summer%202018%20fluoride%20report/Bench_setup_new.png?raw=true" height=400>

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
$Q_{PACl} C_{PACl} = Q_{system} C_{system}$

Water in the gravity-powered system flows from the fluoride stock tank, to the fluoride constant head tank, to the flocculator, up the sedimentation tube, and out the effluent line.

<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/system_flow_2.png?raw=true" height=500>

**Figure 5:** The system flow rate is determined by the height difference between the water level of the fluoride constant head tank and the effluent line. The height difference, and thus the flow rate, can be controlled by the adjustable slider on effluent line.

There are multiple sources of head loss in this system: major head loss in the tubing and minor head loss in the flocculator.

To find major head loss in the straight sections of tubing we will be utilizing the Hagen–Poiseuille equation:

$\Delta H_1 =\frac{32\mu LV}{\rho gd^2}$

Where $L$ is the length of the tube, $V$ is the bulk velocity of the system, and $d$ is the diameter of the tubing.

To find the head loss in the coiled flocculator we will utilize the following equation:

$\Delta H_2 = \frac{32\mu VL}{\rho gd^2} 0.37 De^{0.36}$

Where $De$ is the Dean Number, found experimentally by C.M White ([Garber, 2004](https://www.seas.upenn.edu/~belab/LabProjects/2004/be310s04m5.doc)). It is a dimensionless quantity that establishes a relationship between the inertial, centripetal, and viscous forces in a fluid, and is used to find the pressure drop in a coiled tube. It represented by the following expression:

$De=Re\sqrt\frac{D}{d}$

Where $Re$ is the Reynolds Number:

$Re=\frac{\rho VL}{\mu }$

Therefore,

$\Delta H_2 = \frac{32\mu VL}{\rho gd^2} 0.37 (\frac{\rho VL}{\mu }\sqrt\frac{D}{d})^{0.36}$

The total head loss for the system flow rate will be:

$\Delta H_{tot}=\Delta H_1 + \Delta H_2$

#### Coagulant Flow Rate
<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/headloss_diagram2.png?raw=true" height=500>

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

However, these calculations are no longer a viable method of determining flow rate for the final version of the fluoride gravity system. These equations were only valid for the earlier versions of the gravity apparatus which contained tubing and simple connectors. The addition of an IV drip chamber, discussed further in the following section, altered the head loss and therefore required additional calculation which are not trivial or well developed from our understanding. The team opted to instead carry out measurements and create curves that could be used to determine the optimal heights for the desired flow rates. This is discussed further in the IV drip section.

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
In order for the team to create a standard curve for the PACl flow rate it was necessary to develop a method to firsrt accurately and easily measure the flow rate. This proved to be a challenge due to the small flow rates that the team was aiming to achieve. The team came up with several solutions to easily measure the flow rate of coagulant.

#### Balance

A balance was added to the bottom of the coagulant stock tank to verify coagulant flow rate (Figure 7). The balance measures the mass flow rate out of the coagulant stock tank. As coagulant flows out of the coagulant stock tank into the coagulant constant head tank, the balance measures the rate of mass decrease over time. The mass flow rate can then be converted to volumetric flow rate to obtain the flow rate of coagulant through the system.

<img src="https://github.com/AguaClara/Fluoride-Auto/blob/master/Summer%202018%20fluoride%20report/Gravity_reactor_PACl_adjustable_edit.jpg?raw=true" height=500>

**Figure 7:** The balance was placed under the coagulant stock tank and was used to measure the change in mass over time as the coagulant flows from the stock tank to the constant head tank.

The balance was connected to ProCoDA, and the mass over time was recorded (Figure 8).

![mass_flow](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Mass_Coagulantflow.png?raw=true)

**Figure 8:** The mass flow of coagulant from the coagulant stock tank over time. The slope of the graph was -0.0019, which indicates that the mass flow rate was 1.9 mg/s. The graph appears stepwise because the balance only has a precision of 0.1 g.

The recorded mass flow rate of coagulant can then be converted to volumetric flow rate using a density relationship. However, accuracy with this flow rate measuring technique was suspected to be low. The reason for this was the uncertainty in the ability of the float valve to respond to the low flow rates that we were working with. This uncertainty prompted the introduction of second method for measuring flow rate out of the PACl constant head tank, the IV drip chamber.

#### IV Drip System

Another proposed method to measure and regulate coagulant flow rate was to use an intravenous (IV) system (Figure 11). This system would allow for an easy visual way to measure flow rate just by counting the amount of drops that fall within a given time period. Most IV drip chambers specify the number of drops that equal a milliliter of water; the current setup uses a drip chamber with 20 drops per milliliter. This would allow the user to convert drops per unit time to mL per unit time to get a flow rate. Lastly, it also serves as a way double check the results of the scale derived flow rates.

In order to determine the flow rate the team timed the amount of time it took for 20 drops to fall in the drip chamber. Since the IV drip chamber specified 20 drops per milliliter, the flow rate was calculated by dividing 1 mL by the recorded time. The calculated flow rates can be found [here](https://docs.google.com/spreadsheets/d/1IfbS2UFp3Ce4mH5M0O0il0AwW0HiAQ8-2CF-pYxHCLg/edit?usp=sharing).

The team carried out these measurements at 5 cm intervals and got very insightful information by doing so. It was observed that with a small change in height there was a large change in PACl flow rate. This was concerning because it would make it hard to control flow rates and reproduce them on a consistent basis. To overcome this issue the team decided to increase the length of the microbore tubing. This would increase head loss and increase the total height of the apparatus a bit but would increase reproducibility even more by decreasing the amount the flow rate changed in response to a change in height.

```python
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from scipy import stats

#x coordinates are the height difference between fluoride constant head tank and PACl constant head tank
#y coordinates are the measured flow rates

data_points = np.array([[5, 0.00991333],
                       [10,0.0158],
                       [15,0.0269333],
                       [20,0.03577]])

x_points = data_points[:,0]
y_points = data_points[:,1]

linreg = stats.linregress(x_points, y_points)
slope, intercept, r_value = linreg[0:3]

start = x_points[0] # Change as desired
end = x_points[-1] # last element plus one; change as desired
plt.plot(x_points, y_points, 'o')
plt.plot(np.arange(start,end,0.1), np.arange(start, end,0.1)*slope + intercept)
plt.xlabel('Height Difference between Fluoride Constant Head Tank and PACl Constant Head Tank (cm)')
plt.ylabel('Measured Flow Rate (mL/s)')
plt.title('Measured Flow Rates at Varying Height Differences')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.savefig("flow_rate1.png",dpi=1000)
plt.show()


print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

```


<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/PACl_flowrate_test1.JPG?raw=true">

**Figure 9:**  Data from the first test showing the large change in flow rate relative to the change in delta H.

Increasing the length of the microbore tubing the team was able to obtain data that was much more promising. The team desired a lower slope that would allow for greater operator precision.

```python
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from scipy import stats

#x coordinates are the height difference between fluoride constant head tank and PACl constant head tank
#y coordinates are the measured flow rates

data_points = np.array([[8, 0.001461618533],
                       [10,0.003709630733],
                       [15,0.006501696067],
                       [20,0.009081729333]])

x_points = data_points[:,0]
y_points = data_points[:,1]

linreg = stats.linregress(x_points, y_points)
slope, intercept, r_value = linreg[0:3]

start = x_points[0] # Change as desired
end = x_points[-1] # last element plus one; change as desired
plt.plot(x_points, y_points, 'o')
plt.plot(np.arange(start,end,0.1), np.arange(start, end,0.1)*slope + intercept)
plt.xlabel('Height Difference between Fluoride Constant Head Tank and PACl Constant Head Tank (cm)')
plt.ylabel('Measured Flow Rate (mL/s)')
plt.title('Measured Flow Rates at Varying Height Differences')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.savefig("flow_rate1.png",dpi=1000)
plt.show()


print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)
```

![Test 2](https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/PACl_flowrate_test2.JPG?raw=true)

**Figure 10:** Data from the second test shows a lower slope than that of the first test. This was done by increasing the length of the microbore tubing.

However, the previous tests were preformed with the first version of the drip chamber which posed some challenges.

The first version of this system consisted of the drip chamber connected to a 90 degree elbow that attached to the PACl constant head tank. While running experiments with this setup, it was observed that air bubbles became trapped in the elbow, adding an undetermined amount of head loss to the system. This caused the flow rates to vary drastically between tests. This prompted the team to alter the drip chamber design to improve reproducibility.  

<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/iv_system.jpg?raw=True" height=500>

**Figure 11:** The First version had the IV drip chamber hung from a 90 degree elbow and experienced problems with air bubbles becoming trapped in the elbow.

To reduce the probability of getting air bubbles in the system, the team removed the 90 degree bend and instead connected the drip chamber to the bottom of a newly fabricated constant head tank. A hole was also drilled through the platform to allow the IV chamber to hang freely.

<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/New_constant_PACl_tank.jpeg?raw=true" height=500>

**Figure 12:** New PACl constant head tank without the 90 degree elbow reduce bubbles in the system.

While this fix worked better than the previous version, the team was still encountering issues with reproducibility. The flow rate curves that were measured varied significantly every day that were measured. It was believed the issue stemmed from a number of sources. First, between tests, particularly tests on different days, the PACl stock tank was set to its zero position where no flow would take place. However, the hydrostatic pressure from the flocculator would drive water into the drip chamber, filling it up completely by the time the team returned to work. This forced us to flush the water out and rerun water through the chamber. During this process, air would be introduced into the tubing which many times would stop the flow entirely. A solution that we found to this problem was to pinch the IV tubing to prevent undesired backflow while the system was not in use. (image) Using this technique the team was able to reproduced the same flow rates between tests with less than 1% variations between them.

Even with this solution there were other scenarios that can cause flow rates to vary between tests. This occurred when the team was setting up to run an actual test with fluoride and PACl instead of just water. This required the entire system to be flushed. After adding coagulant to the constant head tank it was observed that air once again changed the flow rate curve that was previously determined. This was believed to be fixed by adding a ball valve before the drip chamber. Closing the valve before emptying out the container prevents air from entering the tubing where it can then alter the flow rate curve.

## Future Work

After the implementation of the new PACl constant head tank, experiments will be rerun to determine the flow rates at different platform heights. These results will allow the team to make further adjustments in order to optimize the system. Microbore tubing can be lengthened or shortened as needed to find the elevation changes desired to allow for a flow rate change that is easy to reproduce. Once that information is known, the team can resize the entire system based on the maximum flow rates that the system would need to achieve. This adjustment would help achieve the goal of making the system as compact as possible. Continued testing for the reproducibility of the flow rate curves is probably also important to continue to carry out to see if there are any shifts in the flow rate with respect to time caused by build up of air or degradation of the IV drip chamber.  Additionally, tests with fluoride and PACl can be done to test its similarity to the fluoride auto's fluoride removal data.

## Conclusion
The Spring 2018 Fluoride Gravity team worked on optimizing the gravity-powered fluoride removal apparatus. Several modifications were made to the system this semester, such as installing a balance and an IV drip system to measure the coagulant flow rate into the system. The length of the microbore tubing has a significant impact on the coagulant flow rate due to the high frictional head loss. Thus, by modifying the length of the microbore tubing and adjusting the height of the coagulant constant head tank, the team determined a simple procedure for adjusting coagulant flow rates. There were however several challenges in determining flow rates analytically and therefore the team proceeded to find theses using empirical methods. The addition of the drip chamber changed the fluid mechanics of the system enough to make the calculations shown in the report inaccurate. It was also observed that the scale measurements are not the most reliable method for measuring flow rate when compared to the IV drip chamber drop counting method. Using the drip chamber to count the number of drops that fall during a given time interval is not only more accurate but also easy to do by anybody and does not require electric balance and ProCoDa.

## Bibliography

American Dental Organization. (2017). Fluoride: Topical and Systemic Supplements. Retrieved from https://www.ada.org/en/member-center/oral-health-topics/fluoride-topical-and-systemic-supplements

Arlappa, N., Aatif Qureshi, I., & Srinivas, R. (2013). Fluorosis in India: An overview. International Journal of Research and Development of Health, 1(3). Retrieved from http://www.ijrdh.com/files/11.Fluorosis.pdf

Bureau of Indian Standards. (2012). IS 10500: Drinking water. Retrieved from https://archive.org/details/gov.in.is.10500.2012/page/n3.

Herrboldt, J. P. (2016)["Fluoride, Natural Organic Matter, and Particles: The Effect of Ligand Competition on the Size Distribution of Aluminum Precipitates in Flocculation."](https://repositories.lib.utexas.edu/bitstream/handle/2152/39194/HERRBOLDT-THESIS-2016.pdf?sequence=1)

India Groundwater: A Valuable but Diminishing Resource. (2017). Retrieved from http://www.worldbank.org/en/news/feature/2012/03/06/india-groundwater-critical-diminishingLeChevallier,

M. W., & Au, K. (2004). Water treatment and pathogen control: Process efficiency in achieving safe drinking-water. Geneva: World Health Organization.

Mondal, D., Dutta, G., & Gupta, S. (2015). Inferring the fluoride hydrogeochemistry and effect of consuming fluoride-contaminated drinking water on human health in some endemic areas of Birbhum district, West Bengal. Environmental Geochemistry and Health, 38(2), 557-576. doi:10.1007/s10653-015-9743-7

United States, NYC Environmental Protection. (2016). New York City 2016 Drinking Water Supply and Quality Report. New York. Retrieved from http://www.nyc.gov/html/dep/pdf/wsstate16.pdf

United States, Environmental Protection Agency. (1996). Potentiometric Determination Fluoride in Aqueous Samples with Ion-Selective Electrode.

World Health Organization. (2004). Fluoride in Drinking Water: A Global Perspective. Fluoride in Drinking Water. Retrieved from http://www.who.int/water_sanitation_health/dwq/chemicals/fluoride.pdf

World Health Organization. (2016, August 29). Water-related diseases. Retrieved from http://www.who.int/water_sanitation_health/diseases-risks/diseases/fluorosis/en/

***

# Manual
The manual provides details on how to construct and operate the gravity-powered fluoride removal apparatus.

## Fabrication Details

### Frame
The frame of the apparatus was built using aluminum 80/20 bars. The two types of bars used here are double rail bars and single rail bars.

<img src="https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Gravity_apparatus_front.JPG?raw=true" height=300>

**Figure 13:** Three 155 cm double rail 80/20 bars were used as the main skeleton of the gravity apparatus. Four 60cm single rail 80/20 cross bars are used along the frame to support the platforms and create stability.

<img src= "https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Gravity_apparatus_side.JPG?raw=true" height=300>

**Figure 14:** Base was made out of 90 cm single rail 80/20 and the supports 30 cm each. The distance between the two vertical double rail 80/20 pieces was 30 cm.  

### Stock Tanks

##### PACl Tank Platforms

Two platforms were made out of single rail 80/20 bars to support the constant PACl tank and the stock tank feeding the constant tank. The platforms were attached to sliders which moved along the double rail frame of the gravity apparatus. PVC sheets were secured to the top side of each platform and a hole drilled through the bottom of the lower platform to allow for the passage of the drip chamber as shown in figure 14.

<img src= "https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Gravity_apparatus_PACl_platform.JPG?raw=true" height=250>

**Figure 15:** Bottom view of the platform that holds the constant PACl head tank. The platform above it also has the same dimensions.

##### Fluoride Tank Platforms:

Two PVC sheet platforms were added to the frame of the gravity apparatus to hold the 10L fluoride constant head tank bucket and the 12L fluoride stock tank that feeds the constant head tank. The dimensions of both of these are shown in figure 15.

<img src= "https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/Gravity_apparatus_fluoride_platflorm.JPG?raw=true" height=300>

**Figure 16:** PVC sheet platform to hold fluoride tank.

### Tubing
The system tubing has a diameter of 0.47625 cm (3/16"). This tubing was used to route water from the fluoride constant head tank to the flocculator, from the flocculator to the sedimentation tube, and from the sedimentation tube to the outflow. The diameter of microbore tubing used was 0.05588 cm (0.022"). Microbore tubing was used from the PACl constant head tank to the T-joint where PACl mixed with the system flow.

### Flocculator

The flocculator was designed by the [Fall 2017 High G Flocculation Team](https://confluence.cornell.edu/display/AGUACLARA/High+G+Flocculation?preview=/348605616/350974755/High%20G%20Flocculation%20Final%20Report%20Fall%202017.pdf). It consists of 0.17 cm inner diameter tubing wrapped around a cardboard cylinder with a diameter of 8 cm. There are 41 turns in the flocculator, which makes up a length of 27 cm.


<img src= "https://github.com/AguaClara/Fluoride_Gravity/blob/master/Fall%202018/flocculator.jpg?raw=true" height=200>

**Figure 17:** The current coiled flocculator design.

### Reactor

The current sedimentation tube design was created by the [Summer 2017 High Rate Sedimentation Team](https://confluence.cornell.edu/display/AGUACLARA/High+Rate+Sedimentation). For fabrication details of the reactor, see ["Fabrication Details > Sedimentation Tube"](https://github.com/AguaClara/Fluoride-Auto/blob/master/Fluoride_Summer2018.md#sedimentation-tube).

## Special Components
The special components for the apparatus include adjustable sliders and the IV drip chamber.

### Adjustable Sliders
The adjustable sliders were purchased from the McMaster-Carr Supply Company. The following components were needed:

* [Side-Mount Bearing, 1-7/8" Long for 2" High Double Rail T-Slotted Framing](https://www1.mcmaster.com/47065T779), Product Number (47065T779)
* [Hand Brake for 1" & 2" Wide Sleeve Bearing Carriage for T-Slotted Framing](https://www1.mcmaster.com/60585K31), Product Number (60585K31)

### IV Drip Chamber
The IV drip chamber used in the apparatus was purchased from Truecare via Amazon. The product name is: ["I.V. Administration Set with GVS Easydrop Flow Rregulator, DEHP-Free, 1 Y-Site, 15 Filter in Drip chamber, Swivel, Luer Lock, 92"](https://www.amazon.com/Administration-Easydrop-Rregulator-DEHP-Free-chamber/dp/B00UNZ8N8I/ref=sr_1_2?ie=UTF8&qid=1539207200&sr=8-2&keywords=iv+drip+set). The team decided to purchase this particular IV drip chamber because it specifies 20 drops per milliliter, which allows for smaller drops and, thus, a smaller flow rate. This allows for more precision when adjusting the coagulant flow rate.


## Operation Manual
### Set-up
1. Fill stock tanks:
    - Fill fluoride stock tank with water and the desired concentration of fluoride.
    - Fill PACl stock tank with DI water and desired concentration of PACl.
2. Open valves at outlets of stock tanks and allow constant head tanks to fill. Once the water level equilibrates in the fluoride and PACl constant head tanks, system operation can begin.
3. To run the system, open the valves at the outlets of the fluoride and PACl constant head tanks.
4. Use the adjustable slider to move the effluent line to its lowest position. This will allow the system to operate at its maximum flow rate.
5. When starting operation for the first time or after a prolonged period of non-use, the sedimentation tube may take a while to fill up with water.
    - Air bubbles trapped in the tubing may prevent the sedimentation tube from filling up.
    - To solve this issue, remove the sedimentation tank from the frame with the tubing still attached and place it on the ground. This will allow air bubbles to flow out of the system and water to fill up the sedimentation tube.
6. To adjust the system flow rate, use the adjustable slider to raise or lower the height of the effluent line.
    - Raising the effluent line will decrease the flow rate.
    - Lowering the effluent line will increase the flow rate.
7. In order to adjust the flow rates of coagulant through the system, use the adjustable slider to raise and lower the platform where the coagulant constant head tank is located. For consistency, the distance between the coagulant stock tank and the coagulant constant head tank was set to be 25 cm.

### Cleaning Procedure
To prevent the system from collecting dust and growing algae, make sure to change out all the water after it has been in use for a prolonged period of time. Flush the system if the water appears turbid or any algae growths appear in the tanks or tubing.

If fluoride removal experiments are done, the whole system should be flushed prior to the start of the next experiment.

To flush the system:
1. Close the fluoride stock and constant head tank valves
2. Unplug the tubing that connects to the valve but not the actual valve.
3. Connect the tubing to the sink by running a long spare tube from the sink to the gravity apparatus. Use a tube connector to join the two ends.
4. Either place the effluent line in a large bucket or add tubing so that it reaches the sink for disposal
5. Run water from the sink through the system for a couple of minutes.

If there is noticeable buildup of residue in the flocculator or tubing further cleaning may be necessary. To clean this the flocculator or tubing should be removed and moved to the sink directly. A small piece of sponge should be cut and placed inside the tubing. Connect the tubing with the small sponge piece to the sink and run it through a few times until the tubing is clean enough to use.

## Experimental Checklist
1. Check that the constant head tanks are filled.
2. Check that all tubing is connected and that there are no leaks.
3. Check that there are no air bubbles in the system. Air bubbles tend to accumulate at the top of the sedimentation tube.  
4. Check that all valves are open.
5. Check that the flow adjustor out of the IV drip chamber is open.

```python
# To convert the document from markdown to pdf
pandoc Fluoride_Grav_Fall2018_Report.md -o Fluoride_Gravity_Research_Report.pdf
```
