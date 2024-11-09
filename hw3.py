from data import CountyDemographics

#Part 1
def population_total(population: list[CountyDemographics])->int:
    total_population = 0
    for county in population:
        if '2014 Population' in county.population:
            total_population += county.population['2014 Population']

    return total_population

#Part 2
def filter_by_state(all_counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in all_counties if county.state == state]

#Part 3
def population_by_education(counties: list[CountyDemographics], education: str) -> float:
    population = 0.0

    for county in counties:
        if education in county.education:
            percentage = county.education[education]
            population += county.population['2014 Population'] * (percentage / 100)
    return population


def population_by_ethnicity(counties, ethnicity_key):
    population = 0
    for county in counties:
        ethnicity = county.ethnicities
        if ethnicity_key in ethnicity:
            population += ethnicity[ethnicity_key]

    return population

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    below_poverty = 0.0

    for county in counties:
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        county_population = county.population.get('2014 Population', 0)
        below_poverty += county_population * (poverty_percentage / 100)

    return below_poverty

#Part 4
def percent_by_education(counties: list[CountyDemographics], education: str) -> float:
    population = 0
    for county in counties:
        population += county.population['2014 Population']
    education_population = population_by_education(counties, education)
    return (education_population/population) * 100


def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    population = 0
    ethnicity_population = 0

    for county in counties:
        if ethnicity in county.ethnicities:
            population += county.population['2014 Population']
            ethnicity_population += county.ethnicities[ethnicity] * county.population['2014 Population'] / 100

    if population == 0:
        return 0

    return (ethnicity_population/population) * 100

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    population = 0.0
    below_poverty = population_below_poverty_level(counties)

    for county in counties:
       population += county.population['2014 Population']

    if population > 0:
        return below_poverty/population * 100
    else:
        return 0.0

#Part 5
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        education_value = county.education.get(education_key, 0)
        if education_value > threshold:
            result.append(county)
    return result

def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        education_value = county.education.get(education_key, 0)
        if education_value < threshold:
            result.append(county)
    return result

def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        ethnicity_value = county.ethnicities.get(ethnicity_key, 0)
        if ethnicity_value > threshold:
            result.append(county)
    return result

def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        ethnicity = county.ethnicities.get(ethnicity_key, 0)
        if ethnicity < threshold:
            result.append(county)
    return result


def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        poverty = county.income.get('Persons Below Poverty Level', 0)
        if poverty > threshold:
            result.append(county)

    return result

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        poverty = county.income.get('Persons Below Poverty Level', 0)
        if poverty < threshold:
            result.append(county)

    return result