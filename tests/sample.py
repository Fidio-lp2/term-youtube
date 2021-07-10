import unittest

class MyTest(unittest.TestCase):
    def test_4plus5(self):
        expectedValue = 10
        self.assertEqual(expectedValue, 4 + 5)

if __name__ == "__main__":
    unittest.main()
