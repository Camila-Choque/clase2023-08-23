from app.pepe import suma
import unittest

class Test(unittest.TestCase):
    def test_init(self):
        self.assertEqual(suma(1,2),3)

if __name__=="__main__":
    unittest.main()