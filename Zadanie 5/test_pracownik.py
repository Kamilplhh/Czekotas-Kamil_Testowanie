from pracownik import Pracownik 
import unittest

class TestImie(unittest.TestCase):
	def setUp(self):
		self.test_dane = Pracownik("Jan","Kowalski",2000)
	
	def test_email(self):
		self.mrozi = self.test_dane.email()
		self.assertEqual(self.mrozi,"Jan.Kowalski@testemail.com")

	def test_nazwa(self):
		self.mroziz = self.test_dane.nazwa()
		self.assertEqual(self.mroziz,"Jan Kowalski")

	def test_podwyzka(self):
		self.mrozix = self.test_dane.podwyzka()
		self.assertEqual(self.mrozix,4000)

	

		


if __name__ == '__main__':
        unittest.main()
