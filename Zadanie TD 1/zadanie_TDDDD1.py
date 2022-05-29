import unittest
import zadanietd1
import zadanitd1

class myslnik(unittest.TestCase):
    
    def test_myslnik(self):
        key = "-"
        container = zadanietd1.zdanie("Prosze - sprawdz to")
        message = "Nie ma myslnika"
        self.assertIn(key, container, message)

    def test_brakmyslnik(self):
        key = "-"
        container = zadanitd1.zdaniee("Prosze  sprawdz to")
        message = "Jestmyslnik"
        self.assertNotIn(key, container, message)


if __name__ == '__main__':
    unittest.main() 