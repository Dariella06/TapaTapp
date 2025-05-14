import unittest

def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b

class TestSuma(unittest.TestCase):
    """Test per a la funció suma"""

    def test_suma_positius(self):
        """Test per a la suma de dos números positius"""
        self.assertEqual(suma(3, 4), 7)
        
    def test_suma_negatius(self):
        """Test per a la suma de dos números negatius"""
        self.assertEqual(suma(-3, -4), -7)
        
    def test_suma_zero(self):
        """Test per a la suma amb zero"""
        self.assertEqual(suma(0, 4), 4)

# Per executar les proves
if __name__ == '__main__':
    unittest.main()
