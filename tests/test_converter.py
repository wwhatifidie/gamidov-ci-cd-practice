import unittest
from converter import km_to_m

class TestConverter(unittest.TestCase):
    def test_1(self): self.assertEqual(km_to_m(1.5), 1500.0)
    def test_2(self): self.assertEqual(km_to_m(1), 1000.0)
    def test_3(self): self.assertEqual(km_to_m(0), 0.0)
    def test_4(self): self.assertEqual(km_to_m(2), 2000.0)
    def test_5(self): self.assertEqual(km_to_m(0.5), 500.0)
    def test_6(self): self.assertEqual(km_to_m(10), 10000.0)
    def test_7(self): self.assertEqual(km_to_m(3.14), 3140.0)
    def test_8(self): self.assertEqual(km_to_m(0.001), 1.0)
    def test_9(self): self.assertEqual(km_to_m(100), 100000.0)
    def test_10(self): self.assertEqual(km_to_m(1.234), 1234.0)
      
