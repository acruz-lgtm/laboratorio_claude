# Calculadora

Script de Python con funciones básicas de aritmética.

## Funciones disponibles

- `sumar(a, b)`: devuelve la suma de `a` y `b`.
- `restar(a, b)`: devuelve la resta de `a` menos `b`.
- `multiplicar(a, b)`: devuelve la multiplicación de `a` por `b`.
- `dividir(a, b)`: devuelve la división de `a` entre `b`. Si `b` es 0, lanza un `ValueError` con el mensaje "No se puede dividir entre cero" en lugar de provocar un error de división entre cero.

## Cómo usarlo

Ejecuta el script directamente para ver un ejemplo de uso:

```bash
python calculadora.py
```

O impórtalo desde otro script de Python:

```python
from calculadora import sumar, restar, multiplicar, dividir

print(sumar(2, 3))        # 5
print(restar(5, 1))       # 4
print(multiplicar(4, 6))  # 24
print(dividir(10, 2))     # 5.0

try:
    dividir(10, 0)
except ValueError as error:
    print(f"Error: {error}")  # Error: No se puede dividir entre cero
```
