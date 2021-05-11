import unittest
from main import grocery_simulator


class MyTestCase(unittest.TestCase):
    def test_scenario1(self):
        result = grocery_simulator('./tests/test_text_files/ex1.txt')
        self.assertEqual(result, 'Finished at: t=7 minutes')

    def test_scenario2(self):
        result = grocery_simulator('./tests/test_text_files/ex2.txt')
        self.assertEqual(result, 'Finished at: t=13 minutes')

    def test_scenario3(self):
        result = grocery_simulator('./tests/test_text_files/ex3.txt')
        self.assertEqual(result, 'Finished at: t=6 minutes')

    def test_scenario4(self):
        result = grocery_simulator('./tests/test_text_files/ex4.txt')
        self.assertEqual(result, 'Finished at: t=9 minutes')

    def test_scenario5(self):
        result = grocery_simulator('./tests/test_text_files/ex5.txt')
        self.assertEqual(result, 'Finished at: t=11 minutes')


if __name__ == '__main__':
    unittest.main()
