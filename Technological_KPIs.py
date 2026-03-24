Technological_KPIs = {

"Grid Security": {
"TGS1": {
    "Name": "Loss of Load Duration (blackout resilience)",
    "Primary use": ["Performance", "Tracking"],
    "Units of measurement": "Minutes",
    "Description": "Estimates minutes/hours per year that critical loads can be supplied during upstream outages using local DER/ESS and islanding procedures; demonstrates resilience capability valued by citizens and authorities.",
    "Roles": ["CEL Manager", "Asset Operator", "Data/Monitoring Lead"]
        },
"TGS2": {
    "Name": "Reduction of RES curtailment for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "The difference between the renewable energy curtailments at transmission network level before and after the integration of all the proposed solutions.",
    "Roles": ["TSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
},
"TGS3": {
    "Name": " Reduction of peak load for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "The difference between the transmission grid peak load before and after the integration of all the proposed solutions.",
    "Roles": ["TSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
},
"TGS4": {
    "Name": "Reduction of RES curtailment for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "The difference between the renewable energy curtailments at distribution network before and after the integration of all the proposed solutions.",
    "Roles": ["DSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
        },
"TGS5": {
    "Name": " Reduction of peak load for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "The difference between the distribution grid peak load before and after the integration of all the proposed solutions.",
    "Roles": ["DSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
},
"TGS6": {
    "Name": "Frequency deviation ratio (FDR)",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Measures the share of time system frequency is outside the allowed band or the RMS deviation; reflects stability performance in a DER-rich context.",
    "Roles": ["TSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
},
"TGS7": {
    "Name": "Impact of events involving the REV",
    "Primary use": "Performance",
    "Units of measurement": "R_δv/event (each tracked involvement factor/event)",
    "Description": "Counts and characterises events where REV assets supported distribution system needs (frequency, voltage/reactive, congestion), including delivered service volumes; evidences useful services to DSO/TSO and markets.",
    "Roles": ["DSO", "Aggregator/Flexibility Provider", "CEL Manager"]
},
"TGS8": {
    "Name": "Voltage deviation ratio (VDR) for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Measures the share of time monitored transmission network buses exceed voltage limits or the RMS deviation; ensures power quality for customers and asset longevity.",
    "Roles": ["TSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
},
"TGS9": {
    "Name": "Voltage deviation ratio (VDR) for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Measures the share of time monitored distribution network buses exceed voltage limits or the RMS deviation; ensures power quality for customers and asset longevity.",
    "Roles": ["DSO", "Aggregator/Flexibility Provider", "Data/Monitoring Lead"]
},
"TGS10": {
    "Name": "Energy curtailment of RES/DERs for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "MWh/y",
    "Description": "Sums renewable/DER energy curtailed over a year due to transmission network or market constraints; highlights lost green output and where flexibility or grid upgrades are most valuable.",
    "Roles": ["TSO", "Asset Operator", "Data/Monitoring Lead"]
        },
"TGS11": {
    "Name": "Energy curtailment of RES/DERs for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "MWh/y",
    "Description": "Sums renewable/DER energy curtailed over a year due to distribution network or market constraints; highlights lost green output and where flexibility or grid upgrades are most valuable.",
    "Roles": ["DSO", "Asset Operator", "Data/Monitoring Lead"]
        },
"TGS12": {
    "Name": "Active power capability for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "States available upward/downward active power from REV assets at the primary substation during service windows; indicates ability to provide balancing and congestion relief.",
    "Roles": ["Aggregator/Flexibility Provider", "TSO", "Asset Operator"]
        },
"TGS13": {
    "Name": "Active power capability for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "States available upward/downward active power from REV assets at the primary substation during service windows; indicates ability to provide balancing and congestion relief.",
    "Roles": ["Aggregator/Flexibility Provider", "TSO", "Asset Operator"]
        },
"TGS14": {
    "Name": "Reactive power capability for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "States available leading/lagging reactive power from REV assets at the transmission node; indicates potential to support voltage and increase RES hosting capacity.",
    "Roles": ["TSO", "Aggregator/Flexibility Provider", "Asset Operator"]
        },
"TGS15": {
    "Name": "Reactive power capability for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "States available leading/lagging reactive power from REV assets at the distribution  node; indicates potential to support voltage and increase RES hosting capacity.",
    "Roles": ["DSO", "Aggregator/Flexibility Provider", "Asset Operator"]
        },
"TGS16": {
    "Name": "Grid‑efficiency improvement (losses) for the Transmission Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the change in transmission network losses (MWh or %) within the boundary; captures efficiency gains from local balancing and better power flows.",
    "Roles": ["TSO", "Data/Monitoring Lead", "Municipal Energy Office"]
        },
"TGS17": {
    "Name": "Grid‑efficiency improvement (losses) for the Distribution Network",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the change in  distribution network losses (MWh or %) within the boundary; captures efficiency gains from local balancing and better power flows.",
    "Roles": ["DSO", "Data/Monitoring Lead", "Municipal Energy Office"]
        },
},

"Renewable Energy Integration": {
"TEI1": {
     "Name": "Total renewable electricity production",
     "Primary use": "Tracking",
     "Units of measurement": "kWh el/y",
     "Description": "Sums annual kWh from PV, wind, biogas-CHP and fuel-cell electricity within the boundary; headline indicator of the REV’s green power output.",
     "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
         },
"TEI2": {
     "Name": "Total renewable thermal production",
     "Primary use": "Tracking",
     "Units of measurement": "kWh th/y",
     "Description": "Sums annual kWh(th) from geothermal, biomass/biogas and solar thermal; headline indicator of green heat provision.",
     "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI3": {
     "Name": "Share of electricity demand covered by RES",
     "Primary use": "Tracking",
     "Units of measurement": "%",
     "Description": "Reports the fraction of local electricity demand met by locally used RES electricity; measures self-sufficiency and import reduction.",
     "Roles": ["CEL Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
},
"TEI4": {
     "Name": "Share of thermal demand covered by RES",
     "Primary use": "Tracking",
     "Units of measurement": "%",
     "Description": "Reports the fraction of local thermal demand met by renewable heat; measures progress in decarbonising heating and cooling.",
     "Roles": ["CEL Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
},
"TEI5": {
    "Name": "Installed RES capacity (thermal)",
    "Primary use": "Planning",
    "Units of measurement": "MW",
    "Description": "Reports commissioned thermal RES capacity in kW(th) within the boundary; indicates readiness of assets to deliver renewable heat.",
    "Roles": ["Asset Operator", "Municipal Energy Office", "CEL Manager"]
        },
"TEI6": {
    "Name": "Installed RES capacity (electrical)",
    "Primary use": "Planning",
    "Units of measurement": "MW",
    "Description": "Reports commissioned electrical RES capacity in kW(el) within the boundary; indicates readiness of assets to deliver renewable power.",
    "Roles": ["Asset Operator", "Municipal Energy Office", "CEL Manager"]
},
"TEI7": {
     "Name": "Electricity demand satisfied by PVs",
     "Primary use": "Tracking",
     "Units of measurement": "%",
     "Description": "Reports the share of local electricity demand met by PV generation used in the boundary annually; clarifies PV’s contribution and diversification.",
     "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI8": {
     "Name": "Electricity demand satisfied by wind",
     "Primary use": "Tracking",
     "Units of measurement": "%",
     "Description": "Reports the share of local electricity demand met by wind generation used in the boundary annually; clarifies wind’s contribution and diversification.",
     "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI9": {
     "Name": "Electricity demand satisfied by hydrogen",
     "Primary use": "Tracking",
     "Units of measurement": "%",
     "Description": "Reports the share of local electricity demand met by hydrogen-derived electricity within the boundary annually; clarifies the role of H₂ in the supply mix.",
     "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI10": {
     "Name": "Electricity demand satisfied by biogas",
     "Primary use": "Tracking",
     "Units of measurement": "%",
     "Description": "Reports the share of local electricity demand met by biogas-derived electricity within the boundary annually; clarifies the role of biogas in the supply mix.",
     "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI11": {
    "Name": "Thermal demand satisfied by biomass",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the share of local thermal demand met by biomass heat annually; clarifies biomass’s contribution to heating.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI12": {
    "Name": "Thermal demand satisfied by hydrogen",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the share of local thermal demand met by hydrogen-derived heat annually; clarifies hydrogen’s contribution to heating.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI13": {
    "Name": "Thermal demand satisfied by biogas",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the share of local thermal demand met by biogas heat annually; clarifies biogas contribution to heating.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "Municipal Energy Office"]
},
"TEI14": {
    "Name": "Thermal demand satisfied by geothermal energy",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the share of local thermal demand met by geothermal heat annually; clarifies geothermal’s contribution to heating.",
    "Roles": ["Data/Monitoring Lead", "Municipal Energy Office", "CEL Manager"]
        },
 },

"Energy Savings & Diversity": {
"TES1": {
    "Name": "Total energy consumption savings",
    "Primary use": "Tracking",
    "Units of measurement": "MWh/y",
    "Description": "Reports the reduction in final energy use versus baseline (weather-normalised) within the boundary; shows demand-side impact on bills and emissions.",
    "Roles": ["CEL Manager", "Municipal Energy Office", "Asset Operator"]
        },
"TES2": {
    "Name": "Energy diversity for cooling & heating",
    "Primary use": "Planning",
    "Units of measurement": "Number",
    "Description": "Counts the distinct thermal supply technologies in active use (or applies a diversity index); signals resilience to supply or price shocks.",
    "Roles": ["CEL Manager", "Municipal Energy Office", "Asset Operator"]
},
"TES3": {
    "Name": "Energy diversity for electricity",
    "Primary use": "Planning",
    "Units of measurement": "Number",
    "Description": "Counts the distinct electrical sources in active use (or applies a diversity index); signals robustness and flexibility of the supply mix.",
    "Roles": ["CEL Manager", "Municipal Energy Office", "Asset Operator"]
},
},

"Energy Autonomy":{
"TEA1": {
    "Name": "Energy savings from the grid",
    "Primary use": "Performance",
    "Units of measurement": "MWh/year",
    "Description": "Reports the reduction in grid electricity imports relative to baseline; evidences growing autonomy and lower exposure to external prices.",
    "Roles": ["Data/Monitoring Lead", "Municipal Energy Office"]
        },
"TEA2": {
    "Name": "External energy consumption (imports)",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Reports imported energy as a share of total consumption; tracks remaining dependency that local assets must cover over time.",
    "Roles": ["TSO", "Data/Monitoring Lead", "Market/Trading Lead"]
},
"TEA3": {
    "Name": "Local energy exported",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Reports exported energy as a share of local generation; shows surplus availability, market linkage and potential revenues.",
    "Roles": ["DSO", "Asset Operator", "CEL Manager", "Data/Monitoring Lead"]
},
"TEA4": {
    "Name": "Total storage capacity (ESS, H₂)",
    "Primary use": "Planning",
    "Units of measurement": "kWh",
    "Description": "Sums usable storage capacity across vectors in MWh(eq); indicates flexibility buffer for peak shaving, resilience and arbitrage.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
},

"Generation Technologies Efficiency":{
"TTE1": {
    "Name": "Energy production efficiency – PV",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual PV output with expected potential (capacity factor or utilisation); reveals siting, O&M and curtailment issues affecting performance.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
"TTE2": {
    "Name": "Energy production efficiency – Wind",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual wind output with expected potential (capacity factor or utilisation); reveals siting, O&M and curtailment issues affecting performance.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
"TTE3": {
    "Name": "Energy production efficiency – Biomass electricity",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual biomass electricity output with expected potential; highlights fuel/logistics and O&M performance.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
"TTE4": {
    "Name": "Energy production efficiency – Biogas electricity",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual biogas electricity output with expected potential; highlights feedstock, CHP uptime and network constraints.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
"TTE5": {
    "Name": "Energy production efficiency – Biogas thermal",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual biogas thermal output with expected potential; highlights feedstock supply and heat-network utilisation.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
"TTE6": {
    "Name": "Energy production efficiency – Geothermal",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual geothermal heat output with expected potential; highlights subsurface/resource and system availability.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "O&M Contractor"]
},
"TTE7": {
    "Name": "Energy production efficiency – Hydrogen fuel cell",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Compares actual annual electricity from fuel cells with expected potential; highlights H₂ supply, conversion efficiency and uptime.",
    "Roles": ["Asset Operator", "Data/Monitoring Lead", "Aggregator/Flexibility Provider"]
},
"TTE8": {
    "Name": "Battery round‑trip efficiency",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Reports discharged energy divided by charged energy over a representative period; quantifies conversion losses that affect economics and sizing.",
    "Roles": ["Asset Operator", "O&M Contractor", "Data/Monitoring Lead"]
        },
"TTE9": {
    "Name": "Availability of the renewable energy source",
    "Primary use": "Tracking",
    "Units of measurement": "%",
    "Description": "Reports the proportion of time an asset is available for dispatch; indicates operational reliability and service readiness.",
    "Roles": ["Community Energy Manager", "Market/Trading Lead", "CEL Manager"]
},
},

"Trading and Markets":{
"TM1": {
    "Name": "Energy exchanged via P2P trading",
    "Primary use": "Tracking",
    "Units of measurement": "MWh",
    "Description": "Sums kWh traded directly between peers within the platform boundary; demonstrates prosumer engagement and local market activity that can lower system costs.",
    "Roles": ["Market/Trading Lead", "Aggregator/Flexibility Provider", "CEL Manager"]
},
"TM2": {
    "Name": "REV revenues from DAM participation",
    "Primary use": "Performance",
    "Units of measurement": "€ or €/MWh",
    "Description": "Reports net revenues attributable to REV assets in the day-ahead market; shows monetisation potential to sustain OPEX and reinvestment.",
    "Roles": ["Market/Trading Lead", "Municipal Energy Office", "Data/Monitoring Lead"]
},
"TM3": {
    "Name": "Social welfare increase from REV in DAM",
    "Primary use": "Performance",
    "Units of measurement": "€",
    "Description": "Estimates the change in market social surplus caused by REV participation versus a counterfactual; evidences system-level benefits for regulators and policymakers.",
    "Roles": ["Transport Authority/CPO", "Municipal Energy Office", "Data/Monitoring Lead"]
},
},

"Transportation": {
"TT1": {
    "Name": "Energy consumption of public EV chargers",
    "Primary use": "Tracking",
    "Units of measurement": "MWh/day or MWh/y",
    "Description": "Reports metered kWh delivered by public chargers in the boundary; indicates scale and growth of e-mobility services for planning and tariffs.",
    "Roles": ["Transport Authority/CPO", "Fleet/Transport Authority", "CEL Manager"]
},
"TT2": {
    "Name": "PEV battery capacity offered via V2G",
    "Primary use": "Tracking",
    "Units of measurement": "MWh/day",
    "Description": "Reports aggregate usable capacity from enrolled vehicles providing V2G; indicates mobilisable flexibility for peak shaving and ancillary services.",
    "Roles": ["Transport Authority/CPO", "Asset Operator", "Data/Monitoring Lead"]
},
"TT3": {
    "Name": "Fuel efficiency before and after (transport)",
    "Primary use": "Performance",
    "Units of measurement": "Lt/km",
    "Description": "Reports the change in energy per kilometre for the same duty cycle when switching technologies (e.g., diesel to EV or hydrogen); links technology choice to operating cost and emissions.",
    "Roles": ["Transport Authority/CPO", "Municipal Transport Office", "Data/Monitoring Lead"]
},
"TT4": {
    "Name": "Fuel consumption for in‑boundary transport by fuel",
    "Primary use": "Tracking",
    "Units of measurement": "MJ/kg/kWh",
    "Description": "Reports annual consumption split by fuel type (diesel, petrol, electricity, hydrogen, etc.); maps the mobility energy mix and targets for transition.",
    "Roles": ["Finance/PMO", "Municipal Energy Office", "Investor/ESCO"]
},
},

}

