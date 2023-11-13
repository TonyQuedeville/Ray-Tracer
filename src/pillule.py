"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

#  Imports

from camera import Camera
from scene import Scene
from sphere import Sphere
from cylinder import Cylinder
from cube import Cube
from plane import Plane
from light import Light

# -----------------------------------------------------------------------------------------------------

# Image

class Pillule:
    def __init__(self, seq=("pillule", 1)):
        self.width = 800.0 
        self.height = 600.0
        
        # Sequence
        self.seq = seq
        self.camera_start_P = (0, 0, 0)
        self.camera_end_P = (0, 0, 0)
        self.camera_start_L = (0, 0, 1)
        self.camera_end_L = (0, 0, 1)
        
        # Camera
        camera = Camera((0, 0, 0), (0, 0, 1))
        
        # Instance de la Scene
        self.scene = Scene(self.width, self.height, camera, 1, .5)
        
        # Instance des objets géométriques
        # Plan
        plan = Plane((0, 1.2, 0), (0, -1, 0), (.5, .5, .5))
        
        # Pillule moitier haute
        sphere_H = Sphere((1.5, -1.3, 3), .5, (1, 0, 0))
        cylindre_H = Cylinder((1.5, -1.3, 3), .5, .5, (1, 0, 0))
        # Pillule moitier basse
        sphere_B = Sphere((1.5, -.3, 3), .5, (1, 1, 1))
        cylindre_B = Cylinder((1.5, -.8, 3), .5, .5, (1, 1, 1))
        
        # Cube
        cube = Cube((.25, .6, 2), (.35, .35, .35), (.3, 0, .7))
        
        # Balle Cube
        balle = Sphere((-1.7, 0, 2.3), .3, (1, .5, 0))
        cube_b = Cube((-1.7, 0, 2.3), (.45, .45, .45), (0, 0.3, 0))

        # Bille
        bille = Sphere((-0.8, .2, 3.5), 1, (1, 1, 0), 1)   

        # Instance des sources lumineuses
        light1 = Light((-2, -1, 0), 1, (1, 1, 1))

        # Ajout de la camera, des objets géométriques et des sources lumineuses à la scène
        self.scene.set_camera(self.scene.camera)
        self.scene.add_light(light1)
        
        self.scene.add_object(plan)
        self.scene.add_object(sphere_H)
        self.scene.add_object(cylindre_H)
        self.scene.add_object(cylindre_B)
        self.scene.add_object(sphere_B)
        self.scene.add_object(cube_b)
        self.scene.add_object(balle)
        self.scene.add_object(cube)
        self.scene.add_object(bille)