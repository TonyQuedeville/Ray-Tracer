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

class Image:
    def __init__(self, seq=("image", 1)):
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
        self.scene = Scene(self.width, self.height, camera, 1, 1)
        
        # Instance des objets géométriques
        plan = Plane((0, 3, 0), (0, -1, 0), (.5, .5, .5))
        sphere = Sphere((0, 0, 5), 2, (1, 0, 0))
        
        # Instance des sources lumineuses
        light1 = Light((0, -3, 0), 1, (1, 1, 1))

        # Ajout de la camera, des objets géométriques et des sources lumineuses à la scène
        self.scene.set_camera(self.scene.camera)
        self.scene.add_object(plan)
        self.scene.add_object(sphere)
        self.scene.add_light(light1)