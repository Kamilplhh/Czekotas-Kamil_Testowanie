import unittest
import calculator


class Testcalc(unittest.TestCase):

  
    def test_dod(self): 

        self.assertEqual(calculator.dod(3, 5), 8) 
        self.assertEqual(calculator.dod(-1, 1), 0)

    def test_odej(self): 

        self.assertEqual(calculator.odej(5, 3), 2) 
        self.assertEqual(calculator.odej(2, 1), 1)
    
    def test_mnoz(self): 

        self.assertEqual(calculator.mnoz(3, 2), 6) 
        self.assertEqual(calculator.mnoz(4, 3), 12)

    def test_dziel(self): 

        self.assertEqual(calculator.dziel(20, 5), 4) 
        self.assertEqual(calculator.dziel(12, 3), 4)
        with self.assertRaises(Exception) as cm:
            calculator.dziel(2,0)

    def test_potega(self): 

        self.assertEqual(calculator.potega(2,2), 4)
        self.assertEqual(calculator.potega(3,2), 9)

    def test_pierw(self): 

        self.assertEqual(calculator.pierw(4), 2) 
        self.assertEqual(calculator.pierw(169), 13)

    def test_procenty(self):

        self.assertEqual(calculator.procenty(20,100), 20)


    def test_fah(self):

        self.assertEqual(calculator.fah(0),32)
        self.assertEqual(calculator.fah(1),33.8)


    def test_kel(self):
        
        self.assertEqual(calculator.kel(0), 273.15)
        


    
if __name__ == '__main__':
        unittest.main()

