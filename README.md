# REV Readiness Assessment Tool (RAT) - FastAPI

This project is a stateless prototype without a persistence layer. 
It is designed as a **foundation that makes the workflow clear and easy to follow.**

---
## Three independent modules:
1) **KPI assessment module**
2) **Barriers & Disadvantages assessment module**
3) **Climate Vulnerability module**
---
### Climate vulnerability
An informational module (no calculations) that provides 
insights of how key climate variables impact energy assets.
#### Relevant endpoints:
- @app.get("/climate_vulnerability") 
   - Returns all vulnerability data (full Climate_vulnerability dictionary)
- @app.post("/climate_vulnerability_text") 
   - Returns the descriptive text for a specific category -> subcategory -> impact type
     - Request example: 
          ```json  
          {
            "selected_vulnerabilities": [
                {
           "main_category": "Residential assets",
           "sub_category": "Air-conditioning",
           "impact_type": "Temperature"
                }
             ]
          }
     - Response example: 
        ```json
        {
          "vulnerability_descriptions": [
            {
              "main_category": "Residential assets",
              "sub_category": "Air-conditioning",
              "impact_type": "Temperature",
              "description": "Rising temperatures can strain AC systems, especially during heat waves, increasing demand and potentially causing equipment overload."
            }
          ]
        }
- @app.get("/weather_variables")
  - Returns all information of weather variables (full Weather_variables dictionary)
- @app.get("/weather_variable/{variable_name}")
  - Returns information of a specific weather variable 

---

### Barriers & Disadvantages
A module that assesses barriers & disadvantages that may hinder 
REV's development and maps them to incentives that can help address them
#### Relevant endpoints:
- @app.get("/barriers_disadvantages")
  - Returns all barriers & disadvantages information (full Barriers_disadvantages dictionary)
- @app.get("/barrier/{persona}/{barrier_id}")
  - Returns a specific barrier 
- @app.post("/barriers_score") 
  - **the main computational endpoint for barriers and disadvantages**:
  - Gets the input for the selected barriers (likelihood and impact, integers from 1-5)
  - Calculates and returns the scores for each barrier and persona and the corresponding incentives
    - Request example:
        ```json
      {
          "selected_barriers": [
            {
              "persona": "Resource Scarcity",
              "id": "RS02",
              "likelihood": 3,
              "impact": 1
            },
        {
              "persona": "Resource Scarcity",
              "id": "RS03",
              "likelihood": 3,
              "impact": 5
            },
        {
              "persona": "Public Resistance",
              "id": "PR02",
              "likelihood": 3,
              "impact": 4
            }
          ]
        }
    - Response example:
    ```json
       {
    "Resource Scarcity": {
      "RS02": {
        "description": "Limited access to technological tools",
        "likelihood": 3,
        "impact": 1,
        "incentives": [
          {
            "id": 18,
            "type": "Non-monetary",
            "category": "Knowledge-Based Incentives",
            "incentive": "Technical assistance",
            "explanation": "Expert guidance and advisory services. Offers support to enhance success rates and reduce complexities.",
            "source": "PROSEU"
          },
          {
            "id": 20,
            "type": "Non-monetary",
            "category": "Knowledge-Based Incentives",
            "incentive": "Peer-to-peer Learning System",
            "explanation": "A system where citizens can ask for and share energy-saving tips directly within an app. Bringing opportunities to learn from each other, encouraging knowledge exchange and active participation.",
            "source": "ENPOWER"
          }
        ]
      },
      "RS03": {
        "description": "Abolition of funding schemes for net-metering projects",
        "likelihood": 3,
        "impact": 5,
        "incentives": [
          {
            "id": 2,
            "type": "Monetary",
            "category": "Financial Incentives",
            "incentive": "Energy Performance Contracting (EPC) – Shared Savings Model",
            "explanation": "Financing model where energy savings fund energy efficiency / renewable energy projects. Ideal for cases lacking technology expertise, manpower, or capital. Energy Service Company (ESCO) implements and manages the project and is compensated based on performance.",
            "source": "NZC"
          },
          {
            "id": 3,
            "type": "Monetary",
            "category": "Financial Incentives",
            "incentive": "Public and private investment - Green bonds. Social bonds",
            "explanation": "A new type of bond product created in the UK enabling local municipalities to use investment-based crowdfunding as a way of raising finance for environmental and social projects.",
            "source": "PROSEU"
          },
          {
            "id": 24,
            "type": "Non-monetary",
            "category": "Market-based incentives",
            "incentive": "Special tenders supporting RES",
            "explanation": "Governments organize specific tenders for renewable energy projects, often with preferential treatment.",
            "source": "PROSEU"
          },
          {
            "id": 26,
            "type": "Non-monetary",
            "category": "Recommendation",
            "incentive": "Recommendation 1 - Reinstate Funding for Energy Communities",
            "explanation": "This barrier cannot be completely mitigated by the previously mentioned incentives. The removal of the net metering support scheme, without providing any other support, puts energy communities in a difficult situation as their business models relied on that scheme. National policy should therefore reintroduce dedicated funding streams for energy communities.",
            "source": "PROSEU"
          }
        ]
      },
      "Persona impact": 3,
      "Persona likelihood": 3,
      "Persona Risk score": 9,
      "Risk level": "Low",
      "Persona Risk percentage": 42.86
    },
    "Public Resistance": {
      "PR02": {
        "description": "Historical legacies and institutional distrust toward government bodies",
        "likelihood": 3,
        "impact": 4,
        "incentives": [
          {
            "id": 17,
            "type": "Non-monetary",
            "category": "Participatory Incentives",
            "incentive": "Local Champions / Ambassadors",
            "explanation": "Elders or other respected community members should be involved to encourage reluctant community members to participate.",
            "source": "ENPOWER"
          },
          {
            "id": 20,
            "type": "Non-monetary",
            "category": "Knowledge-Based Incentives",
            "incentive": "Peer-to-peer Learning System",
            "explanation": "A system where citizens can ask for and share energy-saving tips directly within an app. Bringing opportunities to learn from each other, encouraging knowledge exchange and active participation.",
            "source": "ENPOWER"
          }
        ]
      },
      "Persona impact": 3,
      "Persona likelihood": 4,
      "Persona Risk score": 12,
      "Risk level": "Medium",
      "Persona Risk percentage": 57.14
    },
    "Short-Term Focus": {
      "Persona impact": 0,
      "Persona likelihood": 0,
      "Persona Risk score": 0,
      "Risk level": "None",
      "Persona Risk percentage": 0
    },
    "Regulatory Delay": {
      "Persona impact": 0,
      "Persona likelihood": 0,
      "Persona Risk score": 0,
      "Risk level": "None",
      "Persona Risk percentage": 0
    }
  }

--- 

### KPIs assessment module
#### Relevant endpoints: 
- @app.get("/kpis")
  - Returns all KPI information (predefined from dictionaries (e.g., Economic_KPIs etc. + custom added ones)
- @app.get("/custom_kpis")
  - Returns only custom added KPIs
- @app.get("/kpi/{category}/{kpi_id}")
  - Returns a specific KPI's information (predefined or custom added one)
    - @app.post("/add_custom_kpi") 
      - Endpoint for adding a custom kpi. 
      - Needs to belong in one of the 5 categories (economic, etc.), 
      - Primary use(s) and roles are lists 
      - For Primary use(s) only "Tracking", "Planning" and "Performance" are available options to populate that list.
      - In the current implementation roles represent an informational field on which would be the appropriate users to provide input for this KPI. Ideally, the final implementation should be that a user can provide input for this KPI if he has one of the appropriate roles.
        - Request example:
            ```json
          {
          "category": "Economic_KPIs",
          "subcategory": "new subcategory-existing subcategory",
          "name": "ADDED KPI no.1",
          "primary_use": ["Planning", "Tracking"],
            "units": "MW",
            "description": "This KPI measures..",
            "roles": ["Municipality", "Asset owner"]
          }
        - Response example:
        ```json
          {
          "message": "Custom KPI added under Economic_KPIs/new subcategory/existing subcategory with ID 'custom_KPI_2'.",
          "id": "custom_KPI_2",
          "category": "Economic_KPIs",
          "subcategory": "new subcategory-existing subcategory"
          }
- @app.put("/edit_custom_kpi/{category}/{subcategory}/{kpi_id}") 
  - Edits a custom added KPI
- @app.delete("/delete_custom_kpi/{category}/{subcategory}/{kpi_id}") 
  - Deletes a custom added KPI
- @app.post("/kpis_score") 
  - **Main computational endpoint of kpi assessment module**
  - Gets input for selected kpis (predefined + custom added), 
  - Computes scores per category for every combination of a,b value (integers from 3 to 5 representing time sensitivity and data quality sensitivity) 
  - Returns results for a kpi 
    - **KPI Input:**
      - data quality is integer from 1 to 5,
      - "selected_primary_use" must be one of the available options e.g., if a KPI has in primary use list ["Planning", "Performance"], then "selected_primary_use" cannot be "Tracking"
      - start date and end date of a KPI represent when you begin and stop addressing the KPI and must be inside the **project's** start date and end date 
      - Progress for a KPI can be provided through two ways, either "progress_stage" :"Advanced", "Near/at completion" etc., which correspond to predefined values **OR** through current and target value (advanced mode in tool UI)
      - Besides KPI dates, the endpoint utilizes the project's start/end date and the current date (which month during the project we are currently at)
      - If start date of a KPI > current date, then this KPI is not taken into account in calculations
      - If end date of a KPI < current date, then the progress value freezes at the progress reached at its end date and is not affected by time corrections as we move during the project.
  - Returns the detailed input for each kpi and scores per kpi category, a) at a scale of 0 to 1, at a scale of 1 to 5 and descriptively
- Request example:
   ```json
   {
    "selected_kpis": [
      {
        "category": "Economic_KPIs",
        "subcategory": "Financial viability",
        "id": "EFV1",
        "selected_primary_use": "Performance",
        "progress_stage": "Very early stage",
        "start_date": 5,
        "end_date": 10,
        "data_quality": 3
      },
      {
        "category": "Technological_KPIs",
        "subcategory": "Grid Security",
        "id": "TGS1",
        "selected_primary_use": "Tracking",
        "progress_stage": "Very early stage",
        "start_date": 4,
        "end_date": 13,
        "data_quality": 4
      },
      {
        "category": "Economic_KPIs",
        "subcategory": "Budget Management & Optimization (per project/technology)",
        "id": "EBO1",
        "selected_primary_use": "Planning",
        "current_value": 10,
        "target_value": 100,
        "start_date": 4,
        "end_date": 13,
        "data_quality": 4
      }
    ],
    "project_start": 1,
    "project_end": 15,
    "current_date": 6
  } 
- Response:
```json
 {
  "project_start": 1,
  "project_end": 15,
  "current_date": 6,
  "results_by_ab": {
    "a=3,b=3": {
      "a": 3,
      "b": 3,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.08,
          "level": "Very Low",
          "score_1_to_5": 1.32,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.08,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=3,b=4": {
      "a": 3,
      "b": 4,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.08,
          "level": "Very Low",
          "score_1_to_5": 1.32,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.08,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=3,b=5": {
      "a": 3,
      "b": 5,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=4,b=3": {
      "a": 4,
      "b": 3,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.08,
          "level": "Very Low",
          "score_1_to_5": 1.32,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.08,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=4,b=4": {
      "a": 4,
      "b": 4,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=4,b=5": {
      "a": 4,
      "b": 5,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=5,b=3": {
      "a": 5,
      "b": 3,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.08,
          "level": "Very Low",
          "score_1_to_5": 1.32,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.08,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=5,b=4": {
      "a": 5,
      "b": 4,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.09,
          "level": "Very Low",
          "score_1_to_5": 1.36,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    },
    "a=5,b=5": {
      "a": 5,
      "b": 5,
      "category_scores": {
        "Economic_KPIs": {
          "score": 0.1,
          "level": "Very Low",
          "score_1_to_5": 1.4,
          "kpis": [
            {
              "id": "EFV1",
              "name": "Net Present Value (NPV)",
              "selected_primary_use": "Performance",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.09,
              "start_date": 5,
              "end_date": 10
            },
            {
              "id": "EBO1",
              "name": "CAPEX (annual) – Alkaline Electrolysis",
              "selected_primary_use": "Planning",
              "mode": "numeric",
              "progress_stage": null,
              "progress (%)": 10,
              "score": 0.1,
              "start_date": 4,
              "end_date": 13
            }
          ]
        },
        "Technological_KPIs": {
          "score": 0.1,
          "level": "Very Low",
          "score_1_to_5": 1.4,
          "kpis": [
            {
              "id": "TGS1",
              "name": "Loss of Load Duration (blackout resilience)",
              "selected_primary_use": "Tracking",
              "mode": "qualitative",
              "progress_stage": "Very early stage",
              "progress (%)": 10,
              "score": 0.1,
              "start_date": 4,
              "end_date": 13
            }
          ]
        }
      }
    }
  }
}



