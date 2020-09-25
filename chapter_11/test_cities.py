import unittest
from city_function import describe_city

class CityTestCase(unittest.TestCase):  #注意是unittest.TestCse
    def test_describe_city(self):
        city = describe_city('shanghai', 'china','90000')
        self.assertEqual(city, 'Shanghai, China - Population 90000')

unittest.main()  #不要忘记括号
