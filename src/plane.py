"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

from vector import Vector3D

# -----------------------------------------------------------------------------------------------------

# Plan

class Plane:
    def __init__(self, point, normal, color, reflexion=0): 
        self.id = 0
        self.type = "plane"
        self.center = Vector3D(*point)   # Un point du plan
        self.norm = Vector3D(*normal)    # Vecteur normal au plan
        self.color = color               # Couleur du plan
        self.reflexion = reflexion       # Propriétés de reflexion
    
    def intersect(self, ray):        
        a = self.norm * ray.direction
        b = self.norm * (self.center - ray.origin)
        
        if abs(a) > 0.000001:
            t = b / a
            if t >= 0:
                hit_point = ray.origin + ray.direction * t
                return t, hit_point, self.color
        else:
            return None
    
    def normal(self, hit_point):
        return self.norm


