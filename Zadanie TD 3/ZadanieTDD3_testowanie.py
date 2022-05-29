import zadanieTDD3
import unittest

class Test_kredyt(unittest.TestCase):
    def test_kredytu(self):
        saldo = zadanieTDD3.saldo(0)
        kredyt = zadanieTDD3.kredyt(2300)
        stan_konta = saldo + kredyt
        if (type(stan_konta) == int):
            self.assertEqual(stan_konta, 2300)

    def test_debetu(self):
        saldo = zadanieTDD3.saldo(0)
        kredyt = zadanieTDD3.kredyt(2300)
        stan_konta = saldo + kredyt
        if (type(stan_konta) == int):
            if (stan_konta >= 0):
                debet = False
        self.assertEqual((debet),(False))
        





if __name__ == '__main__':
    unittest.main() 