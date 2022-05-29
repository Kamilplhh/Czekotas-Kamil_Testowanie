import sqlite3
import unittest
import zadanie8
import os


class Testowanie(unittest.TestCase):

    def setUp(self):
        zadanie8.create_database()

    




    def test_select_all(self):
        self.assertEqual(zadanie8.select_all('Filip Czoch'),[('Baza 44', 'Filip Czoch', 'Polska', 11, 'Kcamil Grzegorzec', 'GBS')])

    def test_delete_all(self):
        zadanie8.delete_all('Paulo Sousa')
        self.assertEqual(zadanie8.select_all('Paulo Sousa'),[])

    
    def test_update_all(self):
        zadanie8.update_all(14 , 'Polska')
        self.assertEqual(zadanie8.select_all('Filip Czoch'),[('Baza 44', 'Filip Czoch', 'Polska', 14, 'Kcamil Grzegorzec', 'GBS')])

    def tearDown(self):
        os.remove('boisko.db')


if __name__ == '__main__':
        unittest.main()