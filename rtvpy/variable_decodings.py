# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Tutorials/03_getting_meanings.ipynb.

# %% auto 0
__all__ = ['season_1_codes', 'season_2_codes', 'educ_level_codes', 'religion_codes', 'tenure_status_codes',
           'material_walls_codes', 'material_roof_codes', 'material_floor_codes', 'fuel_source_cooking_codes',
           'cooking_tech_codes', 'lighting_source_codes', 'toilet_facility_codes', 'bedding_type_adults_codes',
           'perennial_crops_grown_codes', 'business_type_codes', 'save_mode_codes', 'all_variable_names',
           'get_column_groups', 'get_meanings', 'getMeanings', 'pick_and_add_columns']

# %% ../nbs/Tutorials/03_getting_meanings.ipynb 2
def get_column_groups() -> dict:
    """Define and return column groups as a dictionary"""
    return {
        'demographic': [
            'year', 'hhh_sex', 'hhh_age', 'pre_cohort', 'pre_hhid', 'pre_name', 'pre_village',
            'pre_cluster', 'pre_parish', 'pre_subcounty', 'pre_district',
            'region', 'pre_district', 'GPS-Latitude', 'GPS-Longitude',
            'hhh_marital_status', 'hhh_religion', 'hhh_educ_level',
            'hhh_read_write', 'leadership_head', 'tot_hhmembers', 'Quartile',
        ],
        'ppi': [
            'house_rooms', 'Tenure_status_of_the_household', 'Material_walls',
            'Material_roof', 'Material_floor', 'Fuel_source_cooking',
            'Cooking_tech', 'Lighting_source', 'Type_of_Toilet_Facility',
            'Every_Member_at_least_ONE_Pair_of_Shoes', 'Bedding_type_adults',
        ],
        'health_access': [
            'health_status', 'Distance_travelled_one_way_OPD_treatment',
            'Time_travel_one_way_trip_OPD_treatment_minutes',
        ],
        'water_access': [
            'Average_Water_Consumed_Per_Day', 'Main_source_of_water_for_consumption',
            'hh_water_collection_Minutes', 'water_distance_collect_water_round_trip',
        ],
        'assets': [
            'farm_implements_owned', 'bicycle_owned', 'solar_owned',
            'radios_owned', 'phones_owned',
        ],
        'seven_day_spending': [
            'cereals_week', 'cereals_days', 'tubers_week', 'tubers_days',
            'fruits_week', 'fruits_days', 'vegetables_week', 'vegetables_days',
            'meat_poultry_offals', 'meat_poultry_offals_days', 'fish_week',
            'fish_days', 'sugar_week', 'sugar_days', 'eggs', 'eggs_days',
            'milk_week', 'milk_days', 'pulses_week', 'pulses_days',
        ],
        'thirty_day_spending': [
            'expenditure_Fuel_lighting', 'expenditure_Utilities',
            'expenditure_Phone_credit', 'expenditure_Transport',
            'expenditure_washing_cleaning_products', 'expenditure_Rent_paid_homestead',
            'expenditure_durable_products',
        ],
        'year_spending': [
            'expenditure_clothing_women', 'expenditure_clothing_men',
            'expenditure_clothing_children_girls', 'expenditure_clothing_children_boys',
            'expenditure_Medical_care', 'expenditure_Maintenance_house',
            'expenditure_Improvements_home', 'expenditure_Household_items',
            'expenditure_Gifts', 'expenditure_Recreation',
        ],
        'farming_spending': ['Expenditure_farm', 'farming_inputs'],
        'land_ownership': [
            'Does_your_Household_own_any_Land', 'Type_of_land_ownership',
            'Size_land_owned', 'Land_size_for_Crop_Agriculture_Acres',
            'Land_size_for_Grazing_Livestock__Acres', 'Land_Not_used__Fallow_LandAcre',
            'Land_Rented_out_for_income_Acres', 'Number_of_Seasons_rented_land_out',
        ],
        'seasonal_agriculture': [
            'Season1_cropped',
            'Season2_cropped',
            'Improved_seed',
            'Season_1',
            'Season_1_1',
            'Season_1_2',
            'Season_1_3','Season_1_4',
            'Season_1_5',
            'Season_1_6',
            'Season_1_7',
            'Season_1_8',
            'Season_1_9',
            'Season_1_10', 
            'Season_1_11',
            'Season_1_11',
            'Season_1_12',
            'Season_1_13',
            'Season_1_14',
            'Season_1_15',
            'Season_1_97',
            'season_1_cropping_mthd',
            'season_1_intercrop_crops',
            'Season_2',
            'Season_2_1',
            'Season_2_2',
            'Season_2_3','Season_2_4',
            'Season_2_5',
            'Season_2_6',
            'Season_2_7',
            'Season_2_8',
            'Season_2_9',
            'Season_2_10', 
            'Season_2_11',
            'Season_2_11',
            'Season_2_12',
            'Season_2_13',
            'Season_2_14',
            'Season_2_15',
            'Season_2_97',
            'season_2_cropping_mthd',
            'season_2_intercrop_crops',
            # quantities
            'sn_1_Ground_Nuts_planted',
            'Food_Banana_Qty_Planted',
            'Coffee_Qty_Planted',
            'sn_1_Maize_planted',
            'sn_1_Sweet_Potatoes_planted',
            'sn_1_Cassava_planted',
            'sn_1_beans_planted',
            'sn_2_Ground_Nuts_planted',
            'sn_2_Maize_planted',
            'sn_2_Sweet_Potatoes_planted',
            'sn_2_Cassava_planted',
            'sn_2_beans_planted',
        ],
        'perennial_cropping': ['perennial_cropping', 'perennial_crops_grown'],
        'employment': ['work_salaried', 'work_casual'],
        'remittances': ['remittances_r'],
        'business': ['business_number', 'Business_type'],
        'household_saving_borrowing': [
            'save_mode', 'save_mode_1', 'save_mode_2', 'save_mode_3',
            'save_mode_4', 'save_mode_5', 'save_mode_6', 'save_mode_7',
            'save_mode_97', 'save_mode_99', 'borrowed_past_12_months',
        ],
        'standard_evaluations': [
            'latrine_present', 'tippy_tap_present', 'soap_ash_present',
            'kitchen_present', 'bathroom_present', 'compound_clean',
            'diskrack_present', 'non_bio_waste_mgt_present',
            'non_bio_waste_mgt_method', 'composts_num', 'water_mgt_methods',
            'hh_produce_lq_manure', 'hh_produce_organics',
        ],
        'incomes': [
            'Formal Employment (USD)', 'Personal Business & Self Employment (USD)',
            'Casual Labour (USD)', 'Remittances & Gifts (USD)',
            'Rent Income (Property & Land) USD', 'Season1 Crops Income (USD)',
            'Season2 Crops Income (USD)', 'Seasonal Crops Income (USD)',
            'Perenial Crops Income (USD)', 'Livestock Income (USD)',
            'Season 1 Agriculture Value (USD)', 'Season 2 Agriculture Value (USD)',
            'Seasonal  Agriculture Value (USD)', 'Perennial Agriculture Value (USD)',
            'Agriculture Value (USD)', 'Livestock Income / Consumed (USD)',
            'Livestock Asset Value (USD)', 'HH Income (USD)',
            ' HH Production (USD)', 'HH Income + Production (USD)',
            'Program Value (USD)', 'Assets'
        ]
    }


# %% ../nbs/Tutorials/03_getting_meanings.ipynb 3
import pandas as pd
import numpy as np

def get_meanings(df, columns_and_codes):
    results = {}
    
    for column_name, codes in columns_and_codes:
        def process_row(row):
            value = row[column_name]
            
            if pd.isna(value):
                return np.nan
            
            try:
                if isinstance(value, (int, float)):
                    return [codes[int(value)]]
                
                code_numbers = str(value).strip().split()
                return [codes[int(num)] for num in code_numbers if num.isdigit()]
                
            except (ValueError, KeyError):
                return np.nan
            
        results[column_name] = df.apply(process_row, axis=1)
    
    return results

# %% ../nbs/Tutorials/03_getting_meanings.ipynb 4
# 2022_year1_2021_year2
season_1_codes = {
    1: "Beans", 2: "Ground Nuts", 3: "Soya", 4: "Peas", 5: "Maize", 6: "Millet", 7: "Sorghum",
    8: "Barley", 9: "Rice", 10: "Irish Potatoes", 11: "Sweet Potatoes", 12: "Cassava", 13: "Yams",
    14: "Garlic", 15: "Ginger", 16: "Tobacco", 97: "Other, specify"
},

season_2_codes = {
    1: "Beans", 2: "Ground Nuts", 3: "Soya", 4: "Peas", 5: "Maize", 6: "Millet", 7: "Sorghum",
    8: "Barley", 9: "Rice", 10: "Irish Potatoes", 11: "Sweet Potatoes", 12: "Cassava", 13: "Yams",
    14: "Garlic", 15: "Ginger", 16: "Tobacco", 97: "Other, specify"
},

educ_level_codes = {
    1: "None", 2: "Primary one", 3: "Primary Two", 4: "Primary Three", 5: "Primary Four",
    6: "Primary Five", 7: "Primary Six", 8: "Primary Seven", 9: "Secondary one", 10: "Secondary Two",
    11: "Secondary Three", 12: "Secondary Four", 13: "Secondary Five", 14: "Secondary Six",
    15: "Certificate", 16: "Vocational Training", 17: "Diploma", 18: "Bachelors",
    19: "Postgraduate", 20: "Doctorate"
},

religion_codes = {
    1: "Non-Religion", 2: "Anglican", 3: "Catholic", 4: "Moslem", 5: "Seventh Adventist",
    6: "Orthodox", 7: "Pentecostal/Born Again", 8: "Buddhist", 9: "Jehovah Witness",
    10: "Traditional (Animist)"
},

tenure_status_codes = {
    1: "Freehold (Privately Owned)", 2: "Rented", 3: "Supplied by the Employer",
    4: "Supplied by relatives", 5: "Customary Land", 6: "Lease land", 7: "Mailo land",
    8: "State owned land", 97: "Other"
},

material_walls_codes = {
    1: "Unburnt Bricks/Mud/Reeds/Other Materials",
    2: "Burn,Bricks/Cement/Wood/Tin/Iron Sheet/Concrete/Stones/Cement Blocks"
},

material_roof_codes = {
    1: "Thatch/Tins, Grass", 2: "Iron Sheets/Concrete/Tiles/Asbestos/Other", 97: "Other"
},

material_floor_codes = {
    1: "Earth", 2: "Cement", 3: "Mosaic/Tiles", 97: "Other"
},

fuel_source_cooking_codes = {
    1: "Firewood/Dung/Grass/Reeds", 2: "Charcoal/Paraffin/Stove/Gas/Biogas",
    3: "Electricity/Other"
},

cooking_tech_codes = {
    1: "Traditional Stove", 2: "Traditional Stone open Air", 3: "Improved Charcoal Stove",
    4: "Improved Fire Stove", 5: "Gas Stove", 6: "Gas Cooker", 7: "Paraffin Stove", 8: "Electric plate"
},

lighting_source_codes = {
    1: "Candle", 2: "Torch", 3: "Firewood", 4: "Paraffin lantern", 5: "Electricity/Solar"
},

toilet_facility_codes = {
    1: "No facility / Bush / Polythene Bag", 2: "Uncovered Pit Latrine / Covered Pit Latrine with no Slab / Ecosan Compost",
    3: "Covered Pit Latrine with Slab", 4: "VIP flushable"
},

bedding_type_adults_codes = {
    1: "Bare", 2: "Cloth", 3: "Mat", 4: "Dead grass", 5: "Bed frame", 6: "Hammock", 7: "Mattress"
},

perennial_crops_grown_codes = {
    1: "Food Banana", 2: "Ripe Banana", 3: "Alcohol Banana", 4: "Coffee", 5: "Vanilla", 6: "Tea",
    7: "Sugar cane", 8: "Jackfruit", 9: "Mangoes", 10: "Oranges", 11: "Passion Fruits",
    12: "Tomato Fruits", 13: "Apple", 14: "Guava", 15: "Avocado", 16: "Eucalyptus", 17: "Pine",
    18: "Mahogany", 19: "Cyprus", 20: "Oak", 21: "Musizi", 22: "Acacia", 23: "Hog Thorn", 24: "Neem",
    25: "Caliandra", 26: "Graveria", 27: "Bamboo", 28: "Cocoa", 97: "Other, specify"
},

business_type_codes = {
    1: "Fishing/Fish Mongering", 2: "Retail Shop/Whole sale Shop/Produce dealer (store)",
    3: "Mobile Money", 4: "Hawker", 5: "Timber/Trees trade/Carpentry", 6: "Livestock trading",
    7: "Driver/Motorbike rider/Bicycle rider", 8: "Butchery/Butcher", 9: "Restaurant/Bar",
    10: "Hairdresser/Barber", 11: "Tailor/Cobbler", 12: "Charcoal / Firewood",
    13: "Grain milling (Posho/Millet/Cassava)", 14: "Mechanic (Motorbikes/cars/bicycle)",
    15: "Drug shop (Human&Vet)/Health Facility", 16: "Brewing", 17: "Craft Making (Baskets/Mats/Molding)",
    18: "Hardware", 19: "Brick making", 20: "Masonry", 21: "Fuel Station (Petrol/Diesel/Paraffin)",
    22: "Mining (Sand/Rocks/Aggregate/Gold)", 23: "Food vendor(food/drinks/Cereals/vegetables",
    24: "Private School", 25: "Scrap (Metal/Plastic)", 26: "Welding", 27: "Stone Quarrying"
},

save_mode_codes = {
    1: "Bank Account", 2: "Saving and Credit cooperatives (SACCO)", 3: "A mobile Money accounts",
    4: "With a shopkeeper", 5: "With family and friends", 6: "At a safe place at home",
    7: "RTV VSLA (Cash round)", 8: "Non RTV VSLA (Cash Round)", 9: "Self Help Group", 99: "No savings"
},


# %% ../nbs/Tutorials/03_getting_meanings.ipynb 5
# 2023_year1_2022_year2

season_1_codes = {
    1: "Beans", 2: "Ground Nuts", 3: "Soya Beans", 4: "Peas", 5: "Maize",
    6: "Millet", 7: "Sorghum", 8: "Barley", 9: "Rice", 10: "Garlic",
    11: "Ginger", 12: "Irish Potatoes", 13: "Sweet Potatoes", 14: "Cassava",
    15: "Yams", 97: "Other, specify"
}

season_2_codes = {
    1: "Beans", 2: "Ground Nuts", 3: "Soya Beans", 4: "Peas", 5: "Maize",
    6: "Millet", 7: "Sorghum", 8: "Barley", 9: "Rice", 10: "Garlic",
    11: "Ginger", 12: "Irish Potatoes", 13: "Sweet Potatoes", 14: "Cassava",
    15: "Yams", 97: "Other, specify"
}

educ_level_codes = {
    1: "None", 2: "Primary one", 3: "Primary Two", 4: "Primary Three", 5: "Primary Four",
    6: "Primary Five", 7: "Primary Six", 8: "Primary Seven", 9: "Secondary one", 10: "Secondary Two",
    11: "Secondary Three", 12: "Secondary Four", 13: "Secondary Five", 14: "Secondary Six",
    15: "Certificate", 16: "Vocational Training", 17: "Diploma", 18: "Bachelors",
    19: "Postgraduate", 20: "Doctorate"
}

religion_codes = {
    1: "Non-Religion", 2: "Anglican", 3: "Catholic", 4: "Moslem",
    5: "Seventh Day Adventist", 6: "Orthodox", 7: "Pentecostal/Born Again",
    8: "Buddhist", 9: "Jehovah Witness", 10: "Traditional (Animist)", 97: "Others, specify"
}

tenure_status_codes = {
    1: "Freehold (Privately Owned)", 2: "Rented", 3: "Supplied by the Employer",
    4: "Supplied by relatives", 5: "Customary Land", 6: "Lease land", 7: "Mailo land",
    8: "State owned land", 97: "Other"
}

material_walls_codes = {
    1: "Unburnt Bricks/Mud/Reeds/Other Materials",
    2: "Burn,Bricks/Cement/Wood/Tin/Iron Sheet/Concrete/Stones/Cement Blocks"
}


material_roof_codes = {
    1: "Thatch/Tins, Grass", 2: "Iron Sheets/Concrete/Tiles/Asbestos/Other", 97: "Other"
}

material_floor_codes = {
    1: "Earth", 2: "Cement", 3: "Mosaic/Tiles", 97: "Other"
}

fuel_source_cooking_codes = {
    1: "Firewood/Dung/Grass/Reeds", 2: "Charcoal/Paraffin/Stove/Gas/Biogas",
    3: "Electricity/Other"
}

cooking_tech_codes = {
    1: "Traditional Stove", 2: "Traditional Stone open Air", 3: "Improved Charcoal Stove",
    4: "Improved Fire Stove", 5: "Gas Stove", 6: "Gas Cooker", 7: "Paraffin Stove", 8: "Electric plate"
}

lighting_source_codes = {
    1: "Candle", 2: "Torch", 3: "Firewood", 4: "Paraffin lantern", 5: "Electricity/Solar"
}

toilet_facility_codes = {
    1: "No facility / Bush / Polythene Bag", 2: "Uncovered Pit Latrine / Covered Pit Latrine with no Slab / Ecosan Compost",
    3: "Covered Pit Latrine with Slab", 4: "VIP flushable"
}

bedding_type_adults_codes = {
    1: "Bare", 2: "Cloth", 3: "Mat", 4: "Dead grass", 5: "Bed frame", 6: "Hammock", 7: "Mattress"
}

perennial_crops_grown_codes = {
    1: "Food Banana", 2: "Ripe Banana", 3: "Alcohol Banana", 4: "Coffee",
    5: "Vanilla", 6: "Tea", 7: "Sugar cane", 8: "Avocado", 9: "Jackfruit",
    10: "Mangoes", 11: "Oranges", 12: "Passion Fruits", 13: "Tomato Fruits",
    14: "Apple", 15: "Guava", 16: "Eucalyptus", 17: "Pine", 18: "Mahogany",
    19: "Cyprus", 20: "Oak", 21: "Musizi", 22: "Acacia", 23: "Hog Thorn",
    24: "Neem", 25: "Caliandra", 26: "Graveria", 27: "Bamboo", 28: "Cocoa",
    29: "Tobacco", 30: "Pineapple", 97: "Other, specify"
}

business_type_codes = {
    1: "Fishing/Fish Mongering", 2: "Retail Shop/Wholesale Shop/Produce dealer (store)", 
    3: "Mobile Money", 4: "Nursery bed", 5: "Hawker", 6: "Timber/Trees trade/Carpentry",
    7: "Livestock trading", 8: "Driver/Motorbike rider/Bicycle rider", 9: "Butchery/Butcher",
    10: "Restaurant/Bar", 11: "Hairdresser/Barber", 12: "Tailor/Cobbler", 13: "Charcoal/Firewood",
    14: "Grain milling (Posho/Millet/Cassava)", 15: "Mechanic (Motorbikes/cars/bicycle)",
    16: "Drug shop (Human & Vet)/Health Facility", 17: "Brewing",
    18: "Craft Making (Baskets/Mats/Molding)", 19: "Hardware", 20: "Brick making",
    21: "Masonry", 22: "Fuel Station (Petrol/Diesel/Paraffin)", 
    23: "Mining (Sand/Rocks/Aggregate/Gold)", 24: "Food vendor (food/drinks/Cereals/vegetables)",
    25: "Private School", 26: "Scrap Metal", 27: "Welding", 28: "Stone Quarrying", 
    97: "Others, specify"
}

save_mode_codes = {
    1: "Bank Account", 2: "Saving and Credit cooperatives (SACCO)", 3: "A mobile Money account",
    4: "With a shopkeeper", 5: "With family and friends", 6: "At a safe place at home",
    7: "RTV VSLA (Cash Round)", 97: "Other VSLA", 99: "None"
}

# %% ../nbs/Tutorials/03_getting_meanings.ipynb 6
all_variable_names = [
    # demographic
    'year',
    'pre_name',
    'hhh_age',
    'hhh_sex',
    'pre_cohort',
    'pre_hhid',
    'pre_village',
    'pre_cluster',
    'pre_parish',
    'pre_subcounty',
    'pre_district',
    'region',
    'pre_district',
    'GPS-Latitude',
    'GPS-Longitude',
    'hhh_marital_status',
    'hhh_religion',
    'hhh_educ_level',
    'hhh_read_write',
    'leadership_head',
    'tot_hhmembers',
    'Quartile',

    # ppi
    'house_rooms',
    'Tenure_status_of_the_household',
    'Material_walls',
    'Material_roof',
    'Material_floor',
    'Fuel_source_cooking',
    'Cooking_tech',
    'Lighting_source',
    'Type_of_Toilet_Facility',
    'Every_Member_at_least_ONE_Pair_of_Shoes',
    'Bedding_type_adults',

    # access to health
    'health_status',
    'Distance_travelled_one_way_OPD_treatment',
    'Time_travel_one_way_trip_OPD_treatment_minutes',

    # access to water
    'Average_Water_Consumed_Per_Day',
    'Main_source_of_water_for_consumption',
    'hh_water_collection_Minutes',
    'water_distance_collect_water_round_trip',

    # assets
    'farm_implements_owned',
    'bicycle_owned',
    'solar_owned',
    'radios_owned',
    'phones_owned',

    # spending in the last seven days
    'cereals_week',
    'cereals_days',
    'tubers_week',
    'tubers_days',
    'fruits_week',
    'fruits_days',
    'vegetables_week',
    'vegetables_days',
    'meat_poultry_offals',
    'meat_poultry_offals_days',
    'fish_week',
    'fish_days',
    'sugar_week',
    'sugar_days',
    'eggs',
    'eggs_days',
    'milk_week',
    'milk_days',
    'pulses_week',
    'pulses_days',


    # spending in the last 30 days
    'expenditure_Fuel_lighting',
    'expenditure_Utilities',
    'expenditure_Phone_credit',
    'expenditure_Transport',
    'expenditure_washing_cleaning_products',
    'expenditure_Rent_paid_homestead',
    'expenditure_durable_products',

    # spending the last 12 months
    'expenditure_clothing_women',
    'expenditure_clothing_men',
    'expenditure_clothing_children_girls',
    'expenditure_clothing_children_boys',
    'expenditure_Medical_care',
    'expenditure_Maintenance_house',
    'expenditure_Improvements_home',
    'expenditure_Household_items',
    'expenditure_Gifts',
    'expenditure_Recreation',

    # land ownership
    'Does_your_Household_own_any_Land',
    'Type_of_land_ownership',
    'Size_land_owned',   'Land_size_for_Crop_Agriculture_Acres',
    'Land_size_for_Grazing_Livestock__Acres',
    'Land_Not_used__Fallow_LandAcre',
    'Land_Rented_out_for_income_Acres',
    'Number_of_Seasons_rented_land_out',

    # Seasonal
    'Season1_cropped',
    'Season2_cropped',
    'Improved_seed',
    'Season_1',
    'Season_1_1',
    'Season_1_2',
    'Season_1_3','Season_1_4',
    'Season_1_5',
    'Season_1_6',
    'Season_1_7',
    'Season_1_8',
    'Season_1_9',
    'Season_1_10', 
    'Season_1_11',
    'Season_1_11',
    'Season_1_12',
    'Season_1_13',
    'Season_1_14',
    'Season_1_15',
    'Season_1_97',
    'season_1_cropping_mthd',
    'season_1_intercrop_crops',
    'Season_2',
    'Season_2_1',
    'Season_2_2',
    'Season_2_3','Season_2_4',
    'Season_2_5',
    'Season_2_6',
    'Season_2_7',
    'Season_2_8',
    'Season_2_9',
    'Season_2_10', 
    'Season_2_11',
    'Season_2_11',
    'Season_2_12',
    'Season_2_13',
    'Season_2_14',
    'Season_2_15',
    'Season_2_97',
    'season_2_cropping_mthd',
    'season_2_intercrop_crops',
    # quantities
    'sn_1_Ground_Nuts_planted',
    'Food_Banana_Qty_Planted',
    'Coffee_Qty_Planted',
    'sn_1_Maize_planted',
    'sn_1_Sweet_Potatoes_planted',
    'sn_1_Cassava_planted',
    'sn_1_beans_planted',
    'sn_2_Ground_Nuts_planted',
    'sn_2_Maize_planted',
    'sn_2_Sweet_Potatoes_planted',
    'sn_2_Cassava_planted',
    'sn_2_beans_planted',

    # Perennial Cropping
    'perennial_cropping',
    'perennial_crops_grown',

    # Expenditure on farming inputs
    'Expenditure_farm',
    'farming_inputs',

    # business
    'business_number',
    'Business_type', 

    # household saving and borrowing
    'save_mode',
    'save_mode_1',
    'save_mode_2',
    'save_mode_3',
    'save_mode_4',
    'save_mode_5',
    'save_mode_6',
    'save_mode_7',
    'save_mode_97',
    'save_mode_99',
    'borrowed_past_12_months',

    # standard evaluations
    'latrine_present',
    'tippy_tap_present',
    'soap_ash_present',
    'kitchen_present',
    'bathroom_present',
    'compound_clean',
    'diskrack_present',
    'non_bio_waste_mgt_present',
    'non_bio_waste_mgt_method',
    'composts_num',
    'water_mgt_methods',
    'hh_produce_lq_manure',
    'hh_produce_organics',

    'work_salaried',
    'work_casual',
    'remittances_r',

  # income variables    
    'Formal Employment (USD)',   
    'Personal Business & Self Employment (USD)',   
    'Casual Labour (USD)',     'Remittances & Gifts (USD)',     
    'Rent Income (Property & Land) USD',     
    'Season1 Crops Income (USD)',    
    'Season2 Crops Income (USD)',   
    'Seasonal Crops Income (USD)',     
    'Perenial Crops Income (USD)',   
    'Livestock Income (USD)',  
    'Season 1 Agriculture Value (USD)',   
    'Season 2 Agriculture Value (USD)',    
    'Seasonal  Agriculture Value (USD)',    
    'Perennial Agriculture Value (USD)',    
    'Agriculture Value (USD)',  
    'Livestock Income / Consumed (USD)',  
    'Livestock Asset Value (USD)',    
    'HH Income (USD)',  
    ' HH Production (USD)',   
    'HH Income + Production (USD)',    
    'Program Value (USD)',
    'Assets'
]

# %% ../nbs/Tutorials/03_getting_meanings.ipynb 7
import pandas as pd
import numpy as np

def getMeanings(df, columns_and_codes):
    """
    Parameters:
    df: DataFrame
    columns_and_codes: list of tuples, each containing (column_name, code_dictionary)
    Example: [('bed_type', bed_codes), ('room_type', room_codes)]
    """
    results = {}
    
    for column_name, codes in columns_and_codes:
        def process_row(row):
            if pd.isna(row[column_name]):
                return np.nan  
            code_numbers = str(row[column_name]).strip().split()
            return [codes[int(num)] for num in code_numbers if num.isdigit()]

        
        results[column_name] = df.apply(process_row, axis=1)
    
    return results

# %% ../nbs/Tutorials/03_getting_meanings.ipynb 11
import pandas as pd
import numpy as np

# pick out columns in variables from dataframe, add as empty columns if missing
def pick_and_add_columns(dataframe: pd.DataFrame = None, variables: list = None) -> pd.DataFrame:
    """
    Picks out columns in 'variables' from 'dataframe' and adds them as empty columns if missing.

    Args:
        dataframe: Pandas DataFrame.
        variables: List of column names to select.

    Returns:
        Pandas DataFrame with selected columns, adding empty columns if missing.
    """
    if dataframe is None or variables is None:
        raise ValueError("dataframe and variables must be provided")

    # Identify missing columns
    missing_vars = [var for var in variables if var not in dataframe.columns]
    
    # Create a DataFrame for missing columns with NaN values
    if missing_vars:
        missing_df = pd.DataFrame({var: np.nan for var in missing_vars}, index=dataframe.index)
        # Concatenate missing columns to the original dataframe
        dataframe = pd.concat([dataframe, missing_df], axis=1)

    # Return only the specified columns
    return dataframe[variables]

