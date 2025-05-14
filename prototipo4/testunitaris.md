# Pruebas Unitarias en Python

## 1. ¿Qué son las pruebas unitarias?

Las pruebas unitarias son pruebas automatizadas que verifican que todas las funciones o módulos de tu código funcionen correctamente. Su objetivo principal es garantizar que cada unidad del software funcione como se espera de forma independiente.

## 2. Bibliotecas de pruebas en Python

Python ofrece varias bibliotecas para realizar pruebas. Las más utilizadas son:

- **unittest`** (incluida por defecto en Python)
- **pytest**

### ¿Cómo funciona unittest?

La biblioteca unittest funciona creando clases que heredan de unittest.TestCase. Dentro de estas clases se definen métodos que comienzan con test, y que contienen las pruebas que se desean ejecutar.

## 3. ¿Cómo funcionan las pruebas unitarias?

Las pruebas unitarias ayudan a comprobar que el código funciona correctamente al nivel más básico. Se escriben pequeños casos de prueba para funciones o métodos individuales. Si una prueba falla, se sabe exactamente qué parte del código está defectuosa.

## 4. Afirmaciones más importantes en unittest

A continuación se listan algunas de las afirmaciones (assertions) más comunes en unittest:

- `assertEqual(a, b)`  
  Verifica que `a == b`

- `assertNotEqual(a, b)`  
  Verifica que `a != b`

- `assertTrue(x)` / `assertFalse(x)`  
  Verifican si una expresión es verdadera o falsa

- `assertIsNone(x)`  
  Verifica que `x` sea `None`

- `assertRaises(Error, función)`  
  Verifica que se lance una excepción al ejecutar la función
