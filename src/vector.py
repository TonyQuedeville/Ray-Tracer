"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

import math
from select import select

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, (int, float)):  # Si other est un nombre
            return Vector3D(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, Vector3D):  # Si other est un vecteur
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Unsupported operand type for addition !")  

    def __sub__(self, other):
        if isinstance(other, (int, float)):  # Si other est un scalaire
            return Vector3D(self.x - other, self.y - other, self.z - other)
        elif isinstance(other, Vector3D):  # Si other est un vecteur
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("Unsupported operand type for substraction !")        

    def __mul__(self, other):
        if isinstance(other, (int, float)): # Si other est un nombre 
            return Vector3D(self.x * other, self.y * other, self.z * other)
        if isinstance(other, (Vector3D)):  # Si other est un vecteur (dot)
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError("Unsupported operand type for multiplication !")

    def cross(self, other): # produit scalaire
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Vector3D(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Unsupported operand type for /")

    def lenth(self): # equivaux à la valeur absolue d'un vecteur
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        length = self.lenth()
        if length > 0:
            return Vector3D(self.x / length, self.y / length, self.z / length)
        else:
            return self

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"