import unittest
from fixtures import Person

class PersonTest(unittest.TestCase):
    def test_fullname(self):
        p1 = Person('kasra','nikshabani')
        p2 = Person('ahmad','karimi')
        self.assertEqual(p1.full_name(),'kasra nikshabani')
        self.assertEqual(p2.full_name(),'ahmad karimi')

    def test_email(self):
        p1 = Person('kasra', 'nikshabani')
        p2 = Person('ahmad', 'karimi')
        self.assertEqual(p1.email(),'kasranikshabani@email.com')
        self.assertEqual(p2.email(),'ahmadkarimi@email.com')

if __name__ == 'name':
    unittest.main


