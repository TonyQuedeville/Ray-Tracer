"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

import math
from vector import Vector3D

# -----------------------------------------------------------------------------------------------------

# Rayons

class Ray:
    def __init__(self, camera, x=0, y=0):       
        self.r0 = camera.origin + camera.look_at * camera.n + camera.rini + camera.u1 * x + camera.u2 * y
        self.origin = camera.origin
        
        # Calcul de la direction du rayon
        self.direction = (self.r0 - camera.origin) 

class Ray_reflexion:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction