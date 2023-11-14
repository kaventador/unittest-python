import unittest
import unit
class UnitTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(unit.add(4,5),9)
        self.assertEqual(unit.add(-1,4),3)
    def test_subtrac(self):
        self.assertEqual(unit.subtract(5,0),5)
    def test_multiply(self):
        self.assertEqual(unit.multiply(2,6),12)
        self.assertEqual(unit.multiply(7,0),0)
    def test_devision(self):
        self.assertEqual(unit.division(4,2),2)
        self.assertRaises(ZeroDivisionError,unit.division(4,2),2)

if __name__ == "__main__":
    unittest.main

#python -m unittest test_unit.py
#python -m unittest discover

