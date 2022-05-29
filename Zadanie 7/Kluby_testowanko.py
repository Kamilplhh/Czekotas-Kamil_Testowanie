import unittest
from pisanko import Txt
import os

class testowanie(unittest.TestCase):

    def setUp(self):
        self.test = Txt("Manchester City", "Bayern")

    def test_probson(self):
        self.proba = self.test.Plik()
        proba = open("Kluby.txt", "r")
        tab = []
        for i in proba:
            tab.append(i)

        self.assertEqual(tab[0].strip("\n"),"Manchester City")




    def tearDown(self):
        os.remove("Kluby.txt")
    


if __name__ == '__main__': 
    unittest.main()
