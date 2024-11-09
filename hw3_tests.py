import data
import build_data
import unittest
import hw3

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]
california = [county for county in reduced_data if county.state == 'CA']

class TestCases(unittest.TestCase):
    pass

    # Part 1
    def test_population_total(self):
        expected_total = sum(county.population['2014 Population'] for county in reduced_data)
        self.assertEqual(hw3.population_total(reduced_data), expected_total)

    def test_population_total2(self):
        expected_total = 318857056
        self.assertEqual(hw3.population_total(full_data), expected_total)

    # Part 2
    def test_filter_by_state(self):
        alabama = hw3.filter_by_state(reduced_data, 'AL')
        expected = len([county for county in reduced_data if county.state == 'AL'])
        self.assertEqual(len(alabama), expected)
        self.assertTrue(all(county.state == 'AL' for county in alabama))

    def test_filter_by_state2(self):
        california = hw3.filter_by_state(reduced_data, 'CA')
        expected = len([county for county in reduced_data if county.state == 'CA'])
        self.assertEqual(len(california), expected)
        self.assertTrue(all(county.state == 'CA' for county in california))

    # Part 3
    def test_population_by_education(self):
        result = hw3.population_by_education([reduced_data[2]], "Bachelor's Degree or Higher")
        self.assertAlmostEqual(result, 87911.145, 2)

    def test_population_by_education2(self):
        result = hw3.population_by_education(reduced_data, "Bachelor's Degree or Higher")
        self.assertAlmostEqual(result, 195114.091, 2)

    def test_population_by_ethnicity_existing_key(self):
        result = hw3.population_by_ethnicity(reduced_data, 'Two or More Races')
        self.assertEqual(result, 19.4)

    def test_population_by_ethnicity_existing_key2(self):
        first = reduced_data[0]
        second = reduced_data[1]
        result = hw3.population_by_ethnicity([first, second], 'Two or More Races')
        self.assertEqual(result, 4.6)

    def test_population_below_poverty_level(self):
        result = hw3.population_below_poverty_level(reduced_data)
        expected_result = 107711.714
        self.assertAlmostEqual(result, expected_result, 2)

    def test_population_below_poverty_level2(self):
        first = reduced_data[0]
        second = reduced_data[1]
        result = hw3.population_below_poverty_level([first, second])
        expected_result = 19165.589
        self.assertAlmostEqual(result, expected_result, 2)

    # Part 4
    def test_percent_by_education(self):
        population = sum(county.population['2014 Population'] for county in reduced_data)
        degree = hw3.population_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected_result = degree/population * 100
        result = hw3.percent_by_education(reduced_data, "Bachelor's Degree or Higher")
        self.assertAlmostEqual(result, expected_result, 2)

    def test_percent_by_education2(self):
        first = reduced_data[0]
        second = reduced_data[1]
        population = first.population['2014 Population'] + second.population['2014 Population']
        degree = hw3.population_by_education([first, second],"Bachelor's Degree or Higher")
        expected_result = degree/population * 100
        result = hw3.percent_by_education([first, second], "Bachelor's Degree or Higher")
        self.assertAlmostEqual(result, expected_result, 2)

    def test_percent_by_ethnicity(self):
        result = hw3.percent_by_ethnicity(reduced_data, "White Alone")
        expected_result = 84.496
        self.assertAlmostEqual(result, expected_result, 2)

    def test_percent_by_ethnicity2(self):
        result = hw3.percent_by_ethnicity(reduced_data, "Norwegian")
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_percent_below_poverty_level(self):
        result = hw3.percent_below_poverty_level(reduced_data)
        expected_result = 16.42
        self.assertAlmostEqual(result, expected_result, 2)

    def test_percent_below_poverty_level2(self):
        first = reduced_data[0]
        second = reduced_data[1]
        result = hw3.percent_below_poverty_level([first, second])
        expected_result = 16.37
        self.assertAlmostEqual(result, expected_result, 2)

    # Part 5
    def test_education_greater_than(self):
        result = hw3.education_greater_than(reduced_data, "Bachelor's Degree or Higher", 35.0)
        expected_counties = [reduced_data[3]]
        self.assertEqual(result, expected_counties)

    def test_education_greater_than2(self):
        result = hw3.education_greater_than(california, "Bachelor's Degree or Higher", 50.0)
        expected_counties = []
        self.assertEqual(result, expected_counties)

    def test_education_less_than(self):
        result = hw3.education_less_than(reduced_data, "Bachelor's Degree or Higher", 15.0)
        expected_counties = [reduced_data[1]]
        self.assertEqual(result, expected_counties)

    def test_education_less_than2(self):
        result = hw3.education_less_than(reduced_data, "Bachelor's Degree or Higher", 1.0)
        expected_counties = []
        self.assertEqual(result, expected_counties)

    def test_ethnicity_greater_than(self):
        result = hw3.ethnicity_greater_than(reduced_data, 'Hispanic or Latino', 30.0)
        expected_counties = [reduced_data[3]]
        self.assertEqual(result, expected_counties)

    def test_ethnicity_greater_than2(self):
        result = hw3.ethnicity_greater_than(california, 'Hispanic or Latino', 90.0)
        expected_counties = []
        self.assertEqual(result, expected_counties)

    def test_ethnicity_less_than(self):
        result = hw3.ethnicity_less_than(reduced_data, 'Hispanic or Latino', 3.0)
        expected_counties = [reduced_data[0]]
        self.assertEqual(result, expected_counties)

    def test_ethnicity_less_than2(self):
        result = hw3.ethnicity_less_than(reduced_data, 'Hispanic or Latino', 2.0)
        expected_counties = []
        self.assertEqual(result, expected_counties)

    def test_below_poverty_level_greater_than(self):
        expected = [data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    ]
        result = hw3.below_poverty_level_greater_than(california, 15)
        self.assertEqual(expected, result)

    def test_below_poverty_level_greater_than2(self):
        expected = []
        result = hw3.below_poverty_level_greater_than(california, 50)
        self.assertEqual(expected, result)

    def test_below_poverty_level_less_than(self):
        expected = [data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),]
        result = hw3.below_poverty_level_less_than(california, 15)
        self.assertEqual(expected, result)

    def test_below_poverty_level_less_than2(self):
        expected = []
        result = hw3.below_poverty_level_less_than(california, 10)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
