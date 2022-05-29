import zadanie_TDD4
import unittest

class Test_portefla(unittest.TestCase):
    def test_wartosci(self):
        saldo = zadanie_TDD4.portfel(self)
        self.assertEqual(saldo,0)

    def test_poczatek(self):
        saldo = zadanie_TDD4.portfel(self)
        stanpocz = saldo + 1000
        self.assertEqual(stanpocz,1000)


    def test_dodawanie(self):
        saldo = zadanie_TDD4.portfel(self)
        stanpocz = saldo + 1000
        stan = stanpocz + 2000
        self.assertEqual(stan, 3000)

    def test_wydawanie(self):
        saldo = zadanie_TDD4.portfel(self)
        stanpocz = saldo + 1000
        stan = stanpocz - 1000
        self.assertEqual(stan,0)






if __name__ == '__main__':
    unittest.main() 