Economic_KPIs = {

"Financial viability" :{
"EFV1": {
    "Name": "Net Present Value (NPV)",
    "Primary use": "Performance",
    "Units of measurement": "M€",
    "Description": "Calculates discounted net cash flows over the project life at an agreed rate; indicates investment attractiveness and supports financing decisions.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
        },
"EFV2": {
    "Name": "Life‑cycle cost of energy generation (LCOE/LCOH/LCOH₂)",
    "Primary use": "Performance",
    "Units of measurement": "Years",
    "Description": "Computes discounted lifetime costs per unit of delivered energy for electricity, heat or hydrogen; enables fair comparison across technologies and informs least‑cost planning.",
    "Roles": ["Finance/PMO", "Investor/ESCO", "Municipal Energy Office"]
        },
"EFV3": {
    "Name": "Internal Rate of Return (IRR)",
    "Primary use": "Performance",
    "Units of measurement": "%",
    "Description": "Finds the discount rate that sets NPV to zero; summarises expected return used by investors to screen projects.",
    "Roles": ["Finance/PMO", "Investor/ESCO", "Municipal Energy Office"]
        },
"EFV4": {
    "Name": "Payback Period",
    "Primary use": "Performance",
    "Units of measurement": "Years",
    "Description": "Counts years needed for cumulative net benefits to equal the initial investment; provides a simple liquidity and risk indicator.",
    "Roles": ["Municipal Economic Development", "Research/Impact Lead", "CEL Manager"]
        },
"EFV5": {
    "Name": "Social Economic/prosperity indicator",
    "Primary use": "Performance",
    "Units of measurement": "€/y",
    "Description": "Estimates local value added per euro invested, based on defined scope of direct and induced effects; captures broader prosperity and supports public acceptance.",
    "Roles": ["Municipal Finance/Social Services", "Community Energy Manager", "Investor/ESCO"]
        },
"EFV6": {
    "Name": "Financing offered for engagement",
    "Primary use": "Performance",
    "Units of measurement": "€",
    "Description": "Totals funds made available to help citizens participate (grants, subsidies, on‑bill financing); reduces entry barriers and improves equity of access.",
    "Roles": ["Community Energy Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
        },
},

"Direct cost savings for CEL members":{
"ECS1": {
    "Name": "Energy bills’ reduction (heating)",
    "Primary use": ["Planning", "Tracking"],
    "Units of measurement": "€",
    "Description": "Calculates annual household bill savings for heating versus business‑as‑usual, normalised for weather; demonstrates affordability benefits that matter most to citizens.",
    "Roles": ["Community Energy Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
        },
"ECS2": {
    "Name": "Energy bills’ reduction (cooling)",
    "Primary use": ["Planning", "Tracking"],
    "Units of measurement": "€",
    "Description": "Calculates annual household bill savings for cooling versus business‑as‑usual, normalised for weather; demonstrates affordability benefits that matter most to citizens.",
    "Roles": ["Community Energy Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
        },
"ECS3": {
    "Name": "Energy bills’ reduction (electricity)",
    "Primary use": ["Planning", "Tracking"],
    "Units of measurement": "€",
    "Description": "Calculates annual household bill savings for electricity versus business‑as‑usual; demonstrates affordability benefits and strengthens engagement.",
    "Roles": ["Community Energy Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
        },
"ECS4": {
    "Name": "Energy cost reduction for CEL communities",
    "Primary use": ["Planning", "Tracking"],
    "Units of measurement": "€/MWh",
    "Description": "Measures the decrease in total energy expenses (heating, cooling, electricity) for all members of the CELs on a yearly basis; reflects the financial benefits delivered to community members compared to baseline energy costs from conventional sources.",
    "Roles": ["Community Energy Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
        },
"ECS5": {
    "Name": "Economic savings from avoided imports",
    "Primary use": ["Planning", "Tracking"],
    "Units of measurement": "€/y",
    "Description": "Quantifies the monetary value of energy costs avoided by reducing reliance on imported energy (e.g., fossil fuels or externally generated electricity).",
    "Roles": ["Community Energy Manager", "Municipal Energy Office", "Data/Monitoring Lead"]
        },
"ECS6": {
    "Name": "Savings in fuel costs from AFVs/green vehicles",
    "Primary use": "Tracking",
    "Units of measurement": "€/km",
    "Description": "Calculates annual or per‑kilometre savings versus conventional vehicles for the same duty cycle; supports fleet business cases and adoption.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
},

"Budget Management & Optimization (per project/technology)": {
"EBO1": {
    "Name": "CAPEX (annual) – Alkaline Electrolysis",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure committed or paid for supply, installation and connection of electrolyser assets in the year (scope noted); informs budgeting and benchmarking.",
    "Roles":["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO2": {
    "Name": "CAPEX (annual) – Fuel cell",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure committed or paid for fuel‑cell assets in the year (scope noted); informs budgeting and benchmarking.",
    "Roles": ["Transport Authority/CPO", "Finance/PMO", "Procurement"]
        },
"EBO3": {
    "Name": "CAPEX (annual) – Fuel Cell Electric Bus",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure committed or paid for fuel‑cell buses and depot systems in the year; supports fleet transition planning.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO4": {
    "Name": "CAPEX (annual) – Small wind energy converters",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure for small wind assets installed in the year; tracks investment in distributed wind.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO5": {
    "Name": "CAPEX (annual) – PV technology",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure for PV plants and rooftop systems in the year; tracks investment pace in solar capacity.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO6": {
    "Name": "CAPEX (annual) – Batteries",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure for stationary battery systems in the year; tracks flexibility investment.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO7": {
    "Name": "CAPEX (annual) – Biogas system",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure for biogas plants and related infrastructure in the year; supports circular‑economy planning.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO8": {
    "Name": "CAPEX (annual) – Geoexchange system",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure for shallow geothermal/geoexchange systems in the year; tracks low‑carbon heat deployment.",
    "Roles": ["Asset Operator", "Finance/PMO", "Procurement"]
        },
"EBO9": {
    "Name": "CAPEX (annual) – Biomass system",
    "Primary use": "Planning",
    "Units of measurement": "€/kW/year",
    "Description": "Totals capital expenditure for biomass boilers/CHP in the year; tracks renewable heat deployment.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO10": {
    "Name": "OPEX (annual) – Alkaline Electrolysis",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual fixed and variable O&M costs for electrolyser systems (scope noted); informs tariff setting and viability.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO11": {
    "Name": "OPEX (annual) – Fuel cell",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual fixed and variable O&M costs for fuel‑cell systems; informs operating budgets.",
    "Roles": ["Transport Authority/CPO", "Finance/PMO", "O&M Contractor"]
        },
"EBO12": {
    "Name": "OPEX (annual) – Fuel Cell Electric Bus",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual O&M for FC buses, including stacks, maintenance and depot; supports TCO tracking.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO13": {
    "Name": "OPEX (annual) – Small wind energy converters",
    "Primary use": "Planning",
    "Units of measurement": "€/kW el/year",
    "Description": "Totals annual O&M for small wind assets; supports reliability and cost optimisation.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO14": {
    "Name": "OPEX (annual) – PV technology",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual O&M for PV systems; supports benchmarking and warranty management.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO15": {
    "Name": "OPEX (annual) – Batteries",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual O&M for stationary batteries; supports lifecycle planning.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO16": {
    "Name": "OPEX (annual) – Biogas system",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual O&M for biogas plants; highlights feedstock and processing costs.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO17": {
    "Name": "OPEX (annual) – Geoexchange system",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual O&M for geoexchange systems; supports heat network operations.",
    "Roles": ["Asset Operator", "Finance/PMO", "O&M Contractor"]
        },
"EBO18": {
    "Name": "OPEX (annual) – Biomass system",
    "Primary use": "Planning",
    "Units of measurement": "€/kWh el/year",
    "Description": "Totals annual O&M for biomass systems; supports fuel supply and maintenance planning.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
        },
"EBO19": {
    "Name": "LCOE – Small wind energy converters",
    "Primary use": "Performance",
    "Units of measurement": "€/kWh el/year",
    "Description": "Computes lifetime levelised cost of electricity for small wind in €/MWh; supports technology ranking and siting decisions.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
        },
"EBO20": {
    "Name": "LCOE – Biogas system",
    "Primary use": "Performance",
    "Units of measurement": "€/kWh el/year",
    "Description": "Computes lifetime levelised cost of electricity for biogas‑CHP in €/MWh; supports valorisation of organic wastes.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
},
"EBO21": {
    "Name": "LCOE – PV technology",
    "Primary use": "Performance",
    "Units of measurement": "€/kWh el/year",
    "Description": "Computes lifetime levelised cost of electricity for PV in €/MWh; enables fair cost comparison and planning.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
},
"EBO22": {
    "Name": "LCOH(th) – Geoexchange system",
    "Primary use": "Performance",
    "Units of measurement": "€/kWh th/year",
    "Description": "Computes lifetime levelised cost of delivered heat from geoexchange in €/MWh(th); guides least‑cost thermal planning.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
},
"EBO23": {
    "Name": "LCOH(th) – Biomass system",
    "Primary use": "Performance",
    "Units of measurement": "€/kWh th/year",
    "Description": "Computes lifetime levelised cost of delivered heat from biomass in €/MWh(th); guides renewable heat deployment.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
        },
"EBO24": {
    "Name": "LCOH₂ – Alkaline Electrolysis",
    "Primary use": "Performance",
    "Units of measurement": "€/kg H₂/year",
    "Description": "Computes €/kg hydrogen at the electrolyser outlet over lifetime costs; informs the pace and scope of hydrogen deployment.",
    "Roles": ["Techno-economic Analyst", "Asset Operator", "Municipal Energy Office"]
},
"EBO25": {
    "Name": "LCOH₂ (electricity from H₂) – Fuel cell",
    "Primary use": "Performance",
    "Units of measurement": "€/kg H₂/year",
    "Description": "Computes €/MWh(el) when reconverting hydrogen in fuel cells including H₂ cost; informs use‑cases for power from hydrogen.",
    "Roles": ["CPO", "Finance/PMO", "Municipal Energy Office"]
        },
"EBO26": {
    "Name": "Levelized Cost of Charging (EV)",
    "Primary use": "Performance",
    "Units of measurement": "€/kWh",
    "Description": "Divides total charging system costs (capex annuity, opex, energy, grid fees) by kWh delivered; indicates end‑user charging price and affordability.",
    "Roles": ["Asset Operator", "Finance/PMO"]
        },
"EBO27": {
    "Name": "Resource cost per ton (organics)",
    "Primary use": "Performance",
    "Units of measurement": "€/t",
    "Description": "Reports average €/t for procuring and handling organic feedstocks (wet/dry specified); critical for biogas and biomass viability.",
    "Roles": ["Waste Management Entity", "Finance/Engineering Lead", "Asset Operator"]
        },
"EBO28": {
    "Name": "Grid cost – MV upgrades",
    "Primary use": "Planning",
    "Units of measurement": "€",
    "Description": "Reports one‑off costs for medium‑voltage reinforcement and connection attributable to the project; informs siting decisions and total investment needs.",
    "Roles": ["DSO", "Finance/Engineering Lead", "Asset Operator"]
        },
"EBO29": {
    "Name": "Grid cost – HV upgrades",
    "Primary use": "Planning",
    "Units of measurement": "€",
    "Description": "Reports one‑off costs for high‑voltage reinforcement and connection attributable to the project; informs siting decisions and total investment needs.",
    "Roles": ["TSO", "Finance/Engineering Lead", "Asset Operator"]
        },
},
}

