#Luttrell, Jason Module 6.2 Test City Functions
#Tests the Display of a city and country once the city and countries are input

import unittest
from city_functions import displayCityCountry

#create a class for the test case
class NamesTestCase(unittest.TestCase):
    #create a test for the displayCityCountry function using strings for
    #city and country
    def test_city_country(self):
        city = 'los angeles'
        country = 'united states' 
     
        CityCountry = displayCityCountry(City=city,Country=country)
        self.assertEqual(CityCountry, 'Los Angeles, United States')
    
    #create a test for the displayCityCountry function using strings for
    #city and country
    def test_city_country_list(self):
        CityCountryList = ['los angeles', 'united states']
             
        CityCountry = displayCityCountry(List=CityCountryList)
        self.assertEqual(CityCountry, 'Los Angeles, United States')

if __name__ == '__main__':
    unittest.main()