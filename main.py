def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

# Остаток от деления
def modulus(a, b):
   if b == 0:
      raise ValueError("На ноль делить нельзя")
   return a % b