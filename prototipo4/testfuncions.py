import unittest

def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

class TestFuncions(unittest.TestCase):
    """Test per a les funcions resta i divideix"""

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)  # 10 - 5 = 5
        self.assertEqual(resta(3, 7), -4)  # 3 - 7 = -4
        self.assertEqual(resta(0, 4), -4)  # 0 - 4 = -4

    def test_divideix(self):
        self.assertEqual(divideix(10, 2), 5)  # 10 / 2 = 5
        self.assertEqual(divideix(7, 3), 2.3333333333333335)  # 7 / 3 ≈ 2.33
        self.assertEqual(divideix(10, 0), "Error: divisió per zero")  # Error en dividir per zero

if __name__ == '__main__':
    unittest.main()
