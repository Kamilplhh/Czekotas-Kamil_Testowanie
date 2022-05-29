import rzuty
import unittest

class Test_sumapunktow(unittest.TestCase):
    
    def test_suma(self):
        sumapktow = rzuty.rzut1(1)+rzuty.rzut2(1)+rzuty.rzut3(1)
        self.assertEqual(sumapktow, 3)

    def test_strike(self):
        strike = 10
        x = rzuty.rzut1(10)
        y = rzuty.rzut2(6)
        z = rzuty.rzut3(3)
        xy = x + y
        xyz = x + y + z
        if (x == strike):
            suma = x + y + z
            self.assertEqual(suma,xyz)
        else:
            sumadwa = x + y
            self.assertEqual(sumadwa,xy)

    def test_spare(self):
        spare = 10
        x = rzuty.rzut1(4)
        y = rzuty.rzut2(6)
        z = rzuty.rzut3(3)
        xy = x + y
        xyz = x + y + z
        if (xy == spare):
            suma = xy + z
            self.assertEqual(suma,xyz)
        else:
            sumadwa = x + y
            self.assertEqual(sumadwa,xy)
        
        
        

if __name__ == '__main__':
    unittest.main() 
