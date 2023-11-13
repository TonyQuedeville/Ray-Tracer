"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

from math import sqrt
from vector import Vector3D

# -----------------------------------------------------------------------------------------------------

# Cylindre

class Cylinder:
    def __init__(self, center=(0, 0, 0), radius=1, height=1, color=(1, 1, 1), reflexion=0):
        self.id = 0
        self.type = "cylinder"
        self.center = Vector3D(*center)  # Centre du cylindre
        self.radius = radius  # Rayon du cylindre
        self.height = height  # Hauteur du cylindre
        self.color = color    # Couleur du cylindre
        self.reflexion = reflexion  # Propriétés de reflexion
    
    def intersect(self, ray):
        ray_origin = ray.origin
        ray_direction = ray.direction
        oc = ray_origin - self.center

        a = ray_direction.x * ray_direction.x + ray_direction.z * ray_direction.z
        b = 2.0 * (oc.x * ray_direction.x + oc.z * ray_direction.z)
        c = oc.x * oc.x + oc.z * oc.z - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            t1 = (-b - sqrt(discriminant)) / (2.0 * a)
            t2 = (-b + sqrt(discriminant)) / (2.0 * a)

            # Vérifiez que le point d'intersection est dans la plage de la hauteur du cylindre
            hit_point1 = ray_origin + ray_direction * t1
            hit_point2 = ray_origin + ray_direction * t2

            if self.center.y <= hit_point1.y <= self.center.y + self.height:
                return t1, hit_point1, self.color
            elif self.center.y <= hit_point2.y <= self.center.y + self.height:
                return t2, hit_point2, self.color

        return None

    def normal(self, hit_point):
        if (hit_point - self.center).lenth() < 0.00001:
            return Vector3D(0,1,0)
        
        if (hit_point - (self.center + self.height)).lenth() < 0.00001:
            return Vector3D(0,-1,0)
        
        return Vector3D(hit_point.x - self.center.x, 0, hit_point.z - self.center.z)