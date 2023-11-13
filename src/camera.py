"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

import math
from vector import Vector3D
from ray import Ray

# -----------------------------------------------------------------------------------------------------

# Camera 

class Camera:
    def __init__(self, origin=(0, 0, 0), look_at=(0, 0, 1), orientation=(0, -1, 0), fov=90, width=800.0, height=600.0):
        self.origin = Vector3D(*origin)  # Position de la caméra
        self.look_at = Vector3D(*look_at) # Point que la caméra regarde
        self.orientation = Vector3D(*orientation) # Vecteur "haut" de la caméra (0,1,0)
        self.fov = fov  # L'angle de champ (field of view) en degrés
        self.width = width # Largeur de l'ecran
        self.height = height # Hauteur de l'ecran
        self.ratio = width / height # Ratio de taille d'écran
        self.n = 1.0 # Distance unitaire entre camera et écran
        
        # Resolution
        self.H = 2 * self.n * math.tan(math.radians(fov) / 2.0)
        self.L = self.H * self.ratio
    
        # Calcul de r0 : Coordonnée du pixel dans l'espace 3D
        o1 = self.look_at.cross(self.orientation)
        self.u1 = o1.normalize() * (self.L / self.width)
        o2 = self.look_at.cross(self.u1)
        self.u2 = o2.normalize() * (self.H / self.height)
        
        self.rini = self.u1 * -(self.width / 2.0) - self.u2 * (self.height / 2.0) 
        
    def generate_ray(self, x, y):
        ray = Ray(self, x, y)
        return ray
