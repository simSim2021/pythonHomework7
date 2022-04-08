import unittest

import classHouse
from classHouse import*


class HouseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def test__init__(self):
        third_house = House(54.5, 3, 3, 'block of flats', 2000)
        self.assertIsInstance(third_house, House)

    def test_get_apartment_number(self):
        """test method get_apartment_number  """
        self.assertLess(classHouse.first_house.get_apartment_number(), classHouse.second_house.get_apartment_number())

    def test_get_room_list(self):
        i = 0
        third_house = House(67.8, 5, 2, 'block of flats', 1961)

        list_required = House.get_room_list(2)
        for i in range(len(list_required)):
            self.assertIn(third_house, list_required)
            "self.assertIn(third_house, House.get_room_list(2))"

    def test_service_time_calc(self):
        third_house = House(59.5, 2, 3, 'town house', 2005)
        self.assertEqual(third_house.service_time_calc(third_house.service_time), 17)


if __name__ == '__main__':
    unittest.main()
