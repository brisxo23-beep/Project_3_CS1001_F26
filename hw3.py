from data import CountyDemographics

#PART 1
#this returns the total 2014 population of all counties in the list
#input is a list of CountyDemographics objects
#outputs is the total population as an integer 
def population_total(countries: list[CountyDemographics]) -> int:
    total = 0
    for county in countries:
        total += county.population["2014 Population"]
    return total

#PART 2
#return: all county objects belonging to the specified state
#Input: A list of counties and a two-letter state abbreviation 
#Output: A list of matching CountyDemographics objects 
def filter_by_state(counties: list[CountyDemographics],state: str) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.state == state:
            result.append(county)
    return result


#PART 3
#return: This calculates the estaimated population with the specific education level
#Input: A list of conties and an educated dictionary key
#Output: The estimated number of people as a float
def population_by_education(counties: list[CountyDemographics], key:str) -> float:
    total = 0.0
    for county in counties:
        percent = county.education.get(key,0)
        population = county.population["2014 Population"]
        total += population * percent / 100
    return total 

#return: this will calculate the estimeaded population of the specified ethnicity 
#Input: a List of counties and an ethinicity dictionary key
#Output: The estimated number of people as a float
def population_by_ethnicity(counties, key):
    total = 0.0
    for county in counties:
        percent = county.ethnicities.get(key,0)
        population = county.population["2014 Population"]
        total += population * percent / 100
    return total

# Calculate the estimated population below the poverty level.
# Input: A list of counties.
# Output: The estimated number of people as a float.
def population_below_poverty_level(counties):
    total = 0.0
    for county in counties:
        percentage = county.income.get("Persons Below Poverty Level", 0)
        population = county.population["2014 Population"]
        total += population * percentage / 100
    return total

#PART 4
#return: This calculate the overall percentage of the poplation with the specified educated level
#Input:A list of counties and an education dictionary key 
#Output: The overall percentage as a float 
def percent_by_education(counties,key):
    total = population_total(counties)
    if total == 0:
        return 0.0
    sub = population_by_education(counties, key)
    return 100 * sub / total

def percent_by_ethnicity(counties, key):
    total = population_total(counties)
    if total == 0:
        return 0.0
    sub = population_by_ethnicity(counties, key)
    return 100 * sub / total

def percent_below_poverty_level(counties):
    total = population_total(counties)
    if total == 0:
        return 0.0
    sub = population_below_poverty_level(counties)
    return 100 * sub / total

#PART 5
#return: counties where the specified education percentage is greater than the threshold
#Input: a list of counties, a key, and a threshold
#Output:a list of matching CountyDemographics objects
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.education.get(key, 0) > threshold:
            result.append(county)
    return result
#return counties where the specified education percentage is strictly less than the threshold
# input: a list of counties, a key, and a threshold
# Output: a list of matching countyDemographics objects
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.education.get(key, 0) < threshold:
            result.append(county)
    return result 

# Return counties where the specified ethnicity percentage is strictly greater than the threshold.
# Input: A list of counties, an ethnicity key, and a threshold.
# Output: A list of matching CountyDemographics objects.
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.ethnicities.get(key, 0) > threshold:
            result.append(county)
    return result

# Return counties where the specified ethnicity percentage is strictly less than the threshold.
# Input: A list of counties, an ethnicity key, and a threshold.
# Output: A list of matching CountyDemographics objects.
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.ethnicities.get(key, 0) < threshold:
            result.append(county)
    return result

# Return counties where the specified ethnicity percentage is strictly greater than the threshold.
# Input: A list of counties, an ethnicity key, and a threshold.
# Output: A list of matching CountyDemographics objects.
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.income.get("Persons Below Poverty Level", 0) > threshold:
            result.append(county)
    return result

# Return counties where the poverty percentage is strictly less than the threshold.
# Input: A list of counties and a numeric threshold.
# Output: A list of matching CountyDemographics objects.
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.income.get("Persons Below Poverty Level", 0) < threshold:
            result.append(county)
    return result 