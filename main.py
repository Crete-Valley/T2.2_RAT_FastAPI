from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint, confloat
from typing import List, Dict, Optional, Any
import math
from enum import Enum


# data imports
from Economic_KPIs import Economic_KPIs
from Environmental_KPIs import Environmental_KPIs
from Social_KPIs import Social_KPIs
from Technological_KPIs import Technological_KPIs
from Cobenefits_KPIs import Co_benefits_KPIs

from Barriers_Disadvantages import Barriers_disadvantages

from Climate_vulnerability import Climate_vulnerability

from Weather_variables import Weather_variables

# barriers & incentives mapping files
from incentives_mapping import incentives_mapping
from incentives import incentives
from incentives_id import incentives_id

# All predefined KPIs in one dictionary
KPI_CATEGORIES = {
    "Economic_KPIs": Economic_KPIs,
    "Environmental_KPIs": Environmental_KPIs,
    "Social_KPIs": Social_KPIs,
    "Technological_KPIs": Technological_KPIs,
    "Cobenefits_KPIs": Co_benefits_KPIs
}

# Initialization of custom KPIs (added by the user) dictionary structure
custom_kpis: Dict[str, Dict[str, Dict[str, Dict[str, Any]]]] = {}



app = FastAPI()

## MODELS ##



class KPICategory(str, Enum):
    economic = "Economic_KPIs"
    environmental = "Environmental_KPIs"
    social = "Social_KPIs"
    technological = "Technological_KPIs"
    cobenefits = "Cobenefits_KPIs"

class PrimaryUse(str, Enum):
    planning = "Planning"
    performance = "Performance"
    tracking = "Tracking"

class BarriersCategory(str, Enum):
    Resource_Scarcity = "Resource Scarcity"
    Public_Resistance = "Public Resistance"
    Short_Term_Focus = "Short-Term Focus"
    Regulatory_Delay = "Regulatory Delay"

class WeatherVariables(str, Enum):
    temperature = "Temperature"
    liquid_precipitation = "Liquid precipitation"
    frozen_precipitation = "Frozen precipitation"
    wind_speeds_and_direction = "Wind speeds and directions"
    drought = "Drought"
    flooding = "Flooding"
    wildfires = "Wildfires"
    extreme_weather_events = "Extreme weather events"
    lighting = "Lightning"

class ProgressStage(str, Enum):
    very_early_stage = "Very early stage"
    early_progress = "Early progress"
    midway = "Midway"
    advanced = "Advanced"
    near_completion = "Near/at completion"

class KPIInput(BaseModel):
    category: KPICategory
    subcategory: str
    id: str
    selected_primary_use: PrimaryUse
    current_value: Optional[confloat(ge=0)] = None
    target_value: Optional[confloat(ge=0)] = None
    progress_stage: Optional[ProgressStage] = None
    start_date: conint(ge=1)
    end_date: conint(ge=1)
    data_quality: conint(ge=1, le=5)

class CustomKPIInput(BaseModel):
    category: KPICategory
    subcategory: Optional[str]
    name: str
    primary_use: Optional[List[PrimaryUse]]
    units: Optional[str] = None
    description: Optional[str] = None
    roles: Optional[List[str]] = None

class EditCustomKPIInput(BaseModel):
    name: Optional[str] = None
    primary_use: Optional[List[PrimaryUse]] = None
    units: Optional[str] = None
    description: Optional[str] = None
    roles: Optional[List[str]] = None

class KPIRequest(BaseModel):
    selected_kpis: List[KPIInput]
    project_start: conint(ge=1)
    project_end: conint(ge=1)
    current_date: conint(ge=1)


class BarriersInput(BaseModel):
    persona: BarriersCategory
    id: str
    likelihood: conint(ge=1, le=5)
    impact: conint(ge=1, le=5)


class BarriersRequest(BaseModel):
    selected_barriers: List[BarriersInput]


class VulnerabilitySelection(BaseModel):
    main_category: str
    sub_category: str
    impact_type: str


class VulnerabilityRequest(BaseModel):
    selected_vulnerabilities: List[VulnerabilitySelection]



# Utilities
def calculate_kpi_score(
    current_value: float, target_value: float,
    start_date: int, end_date: int, current_date: int,
    data_quality: int, a: int, b: int
) -> Optional[float]:

    if current_date < start_date:
        return None

    if target_value == 0:
        raise ValueError("Target value cannot be zero.")

    progress = min(current_value / target_value, 1.0)

    # Freeze value after KPI end date
    effective_current_date = min(current_date, end_date)

    elapsed_fraction = (
        (effective_current_date - start_date + 1) /
        (end_date - start_date + 1)
    )

    # no time penalty if ahead of expected progress
    if progress >= elapsed_fraction:
        time_adjusted_progress = progress
    else:
        time_adjusted_progress = progress * math.exp(-(elapsed_fraction ** a))

    final_progress = time_adjusted_progress * (data_quality / 5) ** (1 / b)
    return round(final_progress, 2)


def calculate_qualitative_kpi_score(
    distance: float,
    start_date: int,
    end_date: int,
    current_date: int,
    data_quality: int,
    a: int,
    b: int
) -> Optional[float]:
    """
    Returns None if KPI has not started yet, so caller can exclude it from averages.
    """

    if current_date < start_date:
        return None

    effective_current_date = min(current_date, end_date)

    elapsed_fraction = (
        (effective_current_date - start_date + 1) /
        (end_date - start_date + 1)
    )

    if distance >= elapsed_fraction:
        time_adjusted_distance = distance
    else:
        time_adjusted_distance = distance * math.exp(-(elapsed_fraction ** a))

    final_score = time_adjusted_distance * (data_quality / 5) ** (1 / b)
    return round(final_score, 2)


def determine_kpi_level(score: float) -> str:
    if 0 <= score < 0.2:
        return "Very Low"
    elif score < 0.4:
        return "Low"
    elif score < 0.6:
        return "Medium"
    elif score < 0.8:
        return "High"
    elif score <= 1:
        return "Very High"
    return "Invalid"

def convert_score_to_five_scale(score: Optional[float]) -> Optional[float]:
    if score is None:
        return None
    return round(1 + 4 * score, 2)

def determine_risk_level(score: float) -> str:
    if 1 <= score < 5:
        return "Very Low"
    elif score < 10:
        return "Low"
    elif score < 15:
        return "Medium"
    elif score < 20:
        return "High"
    elif score <= 25:
        return "Very High"
    return "Invalid"




@app.get("/kpis")
def get_kpis():
    combined = {}

    # First copy predefined KPIs
    for category, subcats in KPI_CATEGORIES.items():
        combined[category] = dict(subcats)

    # Then add custom ones
    for category, subcats in custom_kpis.items():
        if category not in combined:
            combined[category] = {}
        for subcat, items in subcats.items():
            if subcat not in combined[category]:
                combined[category][subcat] = {}
            combined[category][subcat].update(items)

    return combined


@app.get("/barriers_disadvantages")
def get_barriers_disadvantages():
    return Barriers_disadvantages


@app.get("/weather_variables")
def get_weather_variables():
    return Weather_variables


@app.get("/climate_vulnerability")
def get_climate_vulnerability():
    return Climate_vulnerability


@app.get("/custom_kpis")
def get_custom_kpis():
    return custom_kpis

@app.get("/kpi/{category}/{kpi_id}")
def get_single_kpi(category: KPICategory, kpi_id: str):
    # Search predefined KPIs
    kpis = KPI_CATEGORIES.get(category.value)
    if kpis:
        for subcat, items in kpis.items():
            if kpi_id in items:
                return {kpi_id: items[kpi_id]}

    # Search custom KPIs
    custom = custom_kpis.get(category.value, {})
    for subcat, items in custom.items():
        if kpi_id in items:
            return {kpi_id: items[kpi_id]}

    raise HTTPException(status_code=404, detail=f"KPI ID '{kpi_id}' not found in category '{category.value}'")


@app.get("/barrier/{persona}/{barrier_id}")
def get_single_barrier(persona: BarriersCategory, barrier_id: str):
    barriers = Barriers_disadvantages.get(persona.value)
    if not barriers:
        raise HTTPException(status_code=404, detail=f"Persona '{persona.value}' not found.")

    if barrier_id in barriers:
        return {barrier_id: barriers[barrier_id]}

    raise HTTPException(status_code=404, detail=f"Barrier ID '{barrier_id}' not found in persona '{persona.value}'")


@app.get("/weather_variable/{variable_name}")
def get_single_weather_variable(variable_name: WeatherVariables):
    description = Weather_variables.get(variable_name)
    if not description:
        raise HTTPException(status_code=404, detail=f"Weather variable '{variable_name}' not found.")
    return {variable_name: description}


@app.post("/add_custom_kpi")
def add_custom_kpi(kpi: CustomKPIInput):
    category = kpi.category.value
    subcategory = kpi.subcategory or "Custom"

    # Initialize category/subcategory if missing
    if category not in custom_kpis:
        custom_kpis[category] = {}
    if subcategory not in custom_kpis[category]:
        custom_kpis[category][subcategory] = {}

    # Collect all existing custom KPI IDs globally
    all_existing_ids = []
    for cat_data in custom_kpis.values():
        for subcat_data in cat_data.values():
            all_existing_ids.extend(subcat_data.keys())

    # Find next available global custom KPI ID
    max_num = 0
    for kpi_id in all_existing_ids:
        if kpi_id.startswith("custom_KPI_"):
            try:
                num = int(kpi_id.split("_")[-1])
                if num > max_num:
                    max_num = num
            except ValueError:
                continue

    new_id = f"custom_KPI_{max_num + 1}"

    # if primary_use is omitted, store empty list
    primary_uses = [pu.value for pu in kpi.primary_use] if kpi.primary_use else []

    # Store custom KPI
    custom_kpis[category][subcategory][new_id] = {
        "Name": kpi.name,
        "Primary use": primary_uses,
        "Units of measurement": kpi.units or "",
        "Description": kpi.description or "",
        "Roles": kpi.roles or []
    }

    return {
        "message": f"Custom KPI added under {category}/{subcategory} with ID '{new_id}'.",
        "id": new_id,
        "category": category,
        "subcategory": subcategory
    }


AB_VALUES = [3, 4, 5]
AB_COMBINATIONS = [(a, b) for a in AB_VALUES for b in AB_VALUES]


@app.post("/kpis_score")
def calculate_kpi_scores(data: KPIRequest):
    seen_ids = set()

    stage_to_distance = {
        "Very early stage": 0.1,
        "Early progress": 0.3,
        "Midway": 0.5,
        "Advanced": 0.7,
        "Near/at completion": 0.9
    }

    if data.project_end <= data.project_start:
        raise HTTPException(
            400,
            f"project_end ({data.project_end}) must be greater than project_start ({data.project_start})."
        )

    if not (data.project_start <= data.current_date <= data.project_end):
        raise HTTPException(
            400,
            f"current_date ({data.current_date}) must be inside the project timeline "
            f"[{data.project_start}, {data.project_end}]."
        )

    # Validate all KPIs once
    validated_kpis = []

    for kpi in data.selected_kpis:
        if kpi.id in seen_ids:
            raise HTTPException(400, f"Duplicate KPI ID found: '{kpi.id}'.")
        seen_ids.add(kpi.id)

        if kpi.end_date <= kpi.start_date:
            raise HTTPException(
                400,
                f"end_date ({kpi.end_date}) must be greater than start_date ({kpi.start_date}) for KPI '{kpi.id}'."
            )

        if not (data.project_start <= kpi.start_date < kpi.end_date <= data.project_end):
            raise HTTPException(
                400,
                f"KPI '{kpi.id}' has timeline [{kpi.start_date}, {kpi.end_date}] outside project timeline "
                f"[{data.project_start}, {data.project_end}]."
            )

        has_current = kpi.current_value is not None
        has_target = kpi.target_value is not None
        has_progress_stage = kpi.progress_stage is not None

        if has_current != has_target:
            raise HTTPException(
                400,
                f"KPI '{kpi.id}' must provide both current_value and target_value for numeric mode."
            )

        if has_current and has_target and has_progress_stage:
            raise HTTPException(
                400,
                f"KPI '{kpi.id}' cannot provide both current/target values and progress_stage. Choose only one mode."
            )

        if not ((has_current and has_target) or has_progress_stage):
            raise HTTPException(
                400,
                f"KPI '{kpi.id}' must provide either current_value and target_value, or progress_stage."
            )

        predefined_data = KPI_CATEGORIES.get(kpi.category.value, {})
        custom_data = custom_kpis.get(kpi.category.value, {})

        id_exists = any(kpi.id in subcat for subcat in predefined_data.values()) or \
                    any(kpi.id in subcat for subcat in custom_data.values())
        if not id_exists:
            raise HTTPException(400, f"KPI ID '{kpi.id}' not found under category '{kpi.category.value}'.")

        kpi_entry = None
        for subcat in predefined_data.values():
            if kpi.id in subcat:
                kpi_entry = subcat[kpi.id]
                break
        if not kpi_entry:
            for subcat in custom_data.values():
                if kpi.id in subcat:
                    kpi_entry = subcat[kpi.id]
                    break

        if not kpi_entry:
            raise HTTPException(400, f"KPI ID '{kpi.id}' not found under category '{kpi.category.value}'.")

        allowed_primary_uses = kpi_entry.get("Primary use", [])
        if isinstance(allowed_primary_uses, str):
            allowed_primary_uses = [x.strip() for x in allowed_primary_uses.split(",")]

        if allowed_primary_uses and kpi.selected_primary_use.value not in allowed_primary_uses:
            raise HTTPException(
                400,
                f"KPI '{kpi.id}' does not support selected_primary_use '{kpi.selected_primary_use.value}'. "
                f"Allowed values: {allowed_primary_uses}"
            )

        kpi_name = ""
        for subcat in predefined_data.values():
            if kpi.id in subcat:
                kpi_name = subcat[kpi.id].get("Name", "")
                break
        if not kpi_name:
            for subcat in custom_data.values():
                if kpi.id in subcat:
                    kpi_name = subcat[kpi.id].get("Name", "")
                    break

        validated_kpis.append({
            "kpi": kpi,
            "name": kpi_name,
            "has_current": has_current,
            "has_target": has_target,
            "has_progress_stage": has_progress_stage
        })

    # Compute results for every (a, b)
    combination_results = {}

    for a, b in AB_COMBINATIONS:
        category_scores: Dict[str, Dict] = {}

        for item in validated_kpis:
            kpi = item["kpi"]
            has_current = item["has_current"]
            has_target = item["has_target"]
            has_progress_stage = item["has_progress_stage"]
            kpi_name = item["name"]

            progress_pct = None
            score = None

            if has_current and has_target:
                if kpi.target_value == 0:
                    raise HTTPException(400, f"Target value cannot be zero for KPI '{kpi.id}'.")

                distance = min(kpi.current_value / kpi.target_value, 1.0)

                if data.current_date < kpi.start_date:
                    progress_pct = None
                    score = None
                else:
                    progress_pct = round(distance * 100, 2)

                    score = calculate_kpi_score(
                        kpi.current_value,
                        kpi.target_value,
                        kpi.start_date,
                        kpi.end_date,
                        data.current_date,
                        kpi.data_quality,
                        a,
                        b
                    )

            elif has_progress_stage:
                distance = stage_to_distance.get(kpi.progress_stage.value)
                if distance is None:
                    raise HTTPException(400, f"Invalid progress stage '{kpi.progress_stage.value}' for KPI '{kpi.id}'.")

                if data.current_date < kpi.start_date:
                    progress_pct = None
                    score = None
                else:
                    progress_pct = round(distance * 100, 2)

                    score = calculate_qualitative_kpi_score(
                        distance,
                        kpi.start_date,
                        kpi.end_date,
                        data.current_date,
                        kpi.data_quality,
                        a,
                        b
                    )

            if kpi.category.value not in category_scores:
                category_scores[kpi.category.value] = {"scores": [], "kpis": []}

            if score is not None:
                category_scores[kpi.category.value]["scores"].append(score)


            category_scores[kpi.category.value]["kpis"].append({
                "id": kpi.id,
                "name": kpi_name,
                "selected_primary_use": kpi.selected_primary_use.value,
                "mode": "numeric" if has_current and has_target else "qualitative",
                "progress_stage": kpi.progress_stage.value if kpi.progress_stage else None,
                "progress (%)": progress_pct,
                "score": score,
                "start_date": kpi.start_date,
                "end_date": kpi.end_date,
            })

        result = {}
        for category, cat_data in category_scores.items():
            scores = cat_data["scores"]
            if scores:
                avg_score = round(sum(scores) / len(scores), 2)
                level = determine_kpi_level(avg_score)
                score_1_to_5 = convert_score_to_five_scale(avg_score)
            else:
                avg_score = None
                level = "Not Available"
                score_1_to_5 = None

            result[category] = {
                "score": avg_score,
                "level": level,
                "score_1_to_5": score_1_to_5,
                "kpis": cat_data["kpis"]
            }

        combination_results[f"a={a},b={b}"] = {
            "a": a,
            "b": b,
            "category_scores": result
        }

    return {
        "project_start": data.project_start,
        "project_end": data.project_end,
        "current_date": data.current_date,
        "results_by_ab": combination_results
    }


# barrier → incentive IDs
barrier_to_incentive_ids = {
    item["barrier"].strip(): item["incentives"]
    for item in incentives_id
}

# incentive name → full incentive object
incentive_name_to_obj = {i["incentive"]: i for i in incentives}

# barrier → incentive names (from incentives_mapping)
barrier_to_incentive_names = {
    item["barrier"].strip(): item["incentives"]
    for item in incentives_mapping
}

# Fallback if we want incentive objects via ID
id_to_incentive = {i["id"]: i for i in incentives}


@app.post("/barriers_score")
def calculate_barriers_scores(data: BarriersRequest):
    seen_ids = set()
    category_data = {
        persona: {
            "sum_numerator": 0.0,
            "sum_likelihood": 0.0,
            "sum_impact": 0.0
        }
        for persona in Barriers_disadvantages.keys()
    }

    for barrier in data.selected_barriers:
        persona = barrier.persona.value
        barrier_id = barrier.id

        # Validate
        if barrier_id in seen_ids:
            raise HTTPException(400, f"Duplicate barrier ID: {barrier_id}")
        seen_ids.add(barrier_id)

        if persona not in Barriers_disadvantages:
            raise HTTPException(400, f"Invalid persona: {persona}")
        if barrier_id not in Barriers_disadvantages[persona]:
            raise HTTPException(400, f"Barrier ID '{barrier_id}' not in persona '{persona}'")

        # Barrier info
        description = Barriers_disadvantages[persona][barrier_id]
        score = barrier.likelihood * barrier.impact

        cat = category_data[persona]
        cat["sum_numerator"] += score
        cat["sum_likelihood"] += barrier.likelihood
        cat["sum_impact"] += barrier.impact

        # Find matching incentives
        barrier_name = description.strip()
        matched_ids = barrier_to_incentive_ids.get(barrier_name, [])
        incentives_full = [id_to_incentive[i] for i in matched_ids if i in id_to_incentive]

        # Store barrier info
        cat[barrier_id] = {
            "description": description,
            "likelihood": barrier.likelihood,
            "impact": barrier.impact,
            "incentives": incentives_full
        }

    # Final calculation
    result = {}

    total_score = 0.0

    for persona, values in category_data.items():
        numerator = values["sum_numerator"]
        sum_likelihood = values["sum_likelihood"]
        sum_impact = values["sum_impact"]

        a = numerator / sum_impact if sum_impact else 0.0
        b = numerator / sum_likelihood if sum_likelihood else 0.0
        c = a * b

        # Cleanup helpers
        for k in ["sum_numerator", "sum_likelihood", "sum_impact"]:
            values.pop(k)

        values["Persona impact"] = round(a, 2)
        values["Persona likelihood"] = round(b, 2)
        values["Persona Risk score"] = round(c, 2)
        values["Risk level"] = "None" if c == 0 else determine_risk_level(c)

        result[persona] = values
        total_score += c

    for persona, values in result.items():
        if total_score == 0:
            percentage = 0.0
        else:
            percentage = (values["Persona Risk score"] / total_score) * 100

        values["Persona Risk percentage"] = round(percentage, 2)

    return result

@app.post("/climate_vulnerability_text")
def get_climate_vulnerability_text(data: VulnerabilityRequest):
    descriptions = []
    seen_keys = set()

    for v in data.selected_vulnerabilities:
        # Uniqueness check
        key = (v.main_category, v.sub_category, v.impact_type)
        if key in seen_keys:
            raise HTTPException(
                status_code=400,
                detail=f"Duplicate vulnerability entry: {key}"
            )
        seen_keys.add(key)

        # Main category check
        main = Climate_vulnerability.get(v.main_category)
        if main is None:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid main_category: '{v.main_category}'"
            )

        # Subcategory check
        sub = main.get(v.sub_category)
        if sub is None:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid sub_category: '{v.sub_category}' under main_category: '{v.main_category}'"
            )

        # Impact type check
        impact_text = sub.get(v.impact_type)
        if impact_text is None:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid impact_type: '{v.impact_type}' under sub_category: '{v.sub_category}' in main_category: '{v.main_category}'"
            )

        descriptions.append({
            "main_category": v.main_category,
            "sub_category": v.sub_category,
            "impact_type": v.impact_type,
            "description": impact_text
        })

    return {"vulnerability_descriptions": descriptions}


@app.put("/edit_custom_kpi/{category}/{subcategory}/{kpi_id}")
def edit_custom_kpi(
        category: KPICategory,
        subcategory: str,
        kpi_id: str,
        data: EditCustomKPIInput
):
    cat = category.value

    if cat not in custom_kpis or subcategory not in custom_kpis[cat]:
        raise HTTPException(status_code=404, detail=f"Custom KPI path '{cat}/{subcategory}' not found.")

    if kpi_id not in custom_kpis[cat][subcategory]:
        raise HTTPException(status_code=404, detail=f"KPI ID '{kpi_id}' not found under '{cat}/{subcategory}'.")

    kpi_data = custom_kpis[cat][subcategory][kpi_id]

    # Only update fields that are not None
    if data.name is not None:
        kpi_data["Name"] = data.name
    if data.primary_use is not None:
        kpi_data["Primary use"] = [pu.value for pu in data.primary_use]
    if data.units is not None:
        kpi_data["Units of measurement"] = data.units
    if data.description is not None:
        kpi_data["Description"] = data.description
    if data.roles is not None:
        kpi_data["Roles"] = data.roles

    return {"message": f"KPI '{kpi_id}' updated successfully under '{cat}/{subcategory}'.", "updated_kpi": kpi_data}


@app.delete("/delete_custom_kpi/{category}/{subcategory}/{kpi_id}")
def delete_custom_kpi(category: KPICategory, subcategory: str, kpi_id: str):
    cat_value = category.value

    # Check if category and subcategory exist in custom_kpis
    if cat_value not in custom_kpis or subcategory not in custom_kpis[cat_value]:
        raise HTTPException(
            status_code=404,
            detail=f"Custom KPI path '{cat_value}/{subcategory}' not found."
        )

    # Remove the KPI if it exists in custom_kpis
    kpis_dict = custom_kpis[cat_value][subcategory]
    if kpi_id not in kpis_dict:
        raise HTTPException(
            status_code=404,
            detail=f"KPI ID '{kpi_id}' not found under '{cat_value}/{subcategory}'."
        )

    del kpis_dict[kpi_id]

    # Clean up empty subcategory
    if not kpis_dict:
        del custom_kpis[cat_value][subcategory]

    # Clean up empty category
    if not custom_kpis[cat_value]:
        del custom_kpis[cat_value]

    return {"message": f"KPI '{kpi_id}' deleted successfully from '{cat_value}/{subcategory}'."}

