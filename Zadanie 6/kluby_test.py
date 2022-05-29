import unittest
from kluby import Trener

class TestTrener(unittest.TestCase):
    def setUp(self):
        self.test_dane = Trener("Polska", "Lewandowski")

    def mrozix(self):
        self.mrozi = self.test_dane.jest_trener()
        self.assertEqual(self.mrozi,True)
        
if __name__ == '__main__': 
    unittest.main()