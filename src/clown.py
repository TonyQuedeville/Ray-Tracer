"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

#  Imports

from camera import Camera
from scene import Scene
from plane import Plane
from sphere import Sphere
from cylinder import Cylinder
from cube import Cube
from light import Light

# -----------------------------------------------------------------------------------------------------

# Clown

class Clown:
    def __init__(self, seq):
        self.width = 800.0 
        self.height = 600.0
        
        # Sequence
        self.seq = seq
        self.camera_start_P = (2, 1.3, -0.3)
        self.camera_end_P = (-7, -1.3, -5)
        # self.camera_end_P = (-2, -1.3, -0.3)
        
        self.camera_start_L = (-0.25, -0.15, 1)
        self.camera_end_L = (1, 0.15, 1)
        # self.camera_end_L = (0.25, 0.15, 1)
        
        # Camera
        camera = Camera(self.camera_start_P, self.camera_start_L)
        
        # Instance de la Scene
        self.scene = Scene(self.width, self.height, camera, 1, .5)
        
        # Instance des objets géométriques
        # Plan
        plan = Plane((0, 5.2, 0), (0, -1, 0), (.7, .7, .7))        
        #  Tête
        tete = Sphere((0, 0, 5), 2, (1, .8, .8))
        # Yeux
        oeil_G = Sphere((-.5, -.6, 3.5), .4, (0.8, 0.8, 1))
        pupil_G = Sphere((-.5, -.6, 3.15), .1, (0.5, 0.5, 0))
        oeil_D = Sphere((.5, -.6, 3.5), .4, (0.8, 0.8, 1))
        pupil_D = Sphere((.5, -.6, 3.15), .1, (0.5, 0.5, 0))
        # Oreilles
        oreil_G = Sphere((-1.8, -.2, 4.5), .6, (1, .8, .8))
        oreil_D = Sphere((1.8, -.2, 4.5), .6, (1, .8, .8))
        # Nez
        nez = Sphere((0, 0, 3.1), .4, (1, .3, .3))
        #  Bouche
        bouche = Cylinder((0, .47, 3.4), .5, 0.3, (1, .3, .3))
        # Coup
        coup = Cylinder((0, 1.5, 5.1), 1, 0.6, (1, .8, .8))
        # Chapeau
        chapeau = Cylinder((0, -2.5, 5), 1, 1.6, (.2, .2, .2))
        contour_H = Cylinder((0, -2.5, 5), 1.1, .15, (1, 1, .2))
        contour_B = Cylinder((0, -1.7, 5), 1.8, .15, (1, 1, .2))  
        # Antenne
        antenne = Cylinder((0, -4.5, 5), .05, 2, (1, 1, 1)) 
        cube_A = Cube((0, -4.5, 5), (.2, .2, .2), (1, 0, 0))
        # Boite
        box = Cube((0, 3, 5), (2.2, 2.2, 2.2), (.5, 1,.5))
        cube_Av = Cube((0, 3, 4), (.5, .5, .5), (1, 1, 0))
        cube_D = Cube((1, 3, 5), (.5, .5, .5), (1, 1, 0))
        cube_G = Cube((-1, 3, 5), (.5, .5, .5), (1, 1, 0))
        cube_Ar = Cube((0, 3, 6), (.5, .5, .5), (1, 1, 0))
        
        # Bille
        self.bille_start = (-16, 2.1, 10)
        self.bille_end = (14, 2.1, 12)
        bille = Sphere(self.bille_start, 2, (0, 0, 0), 1)
        
        # Instance des sources lumineuses
        light1 = Light((0, -3, 0), .7, (1, 1, 1))

        # Ajout de la camera, des objets géométriques et des sources lumineuses à la scène
        self.scene.set_camera(camera)
        
        self.scene.add_object(plan)
        self.scene.add_object(tete)
        self.scene.add_object(oeil_G)
        self.scene.add_object(pupil_G)
        self.scene.add_object(oeil_D)
        self.scene.add_object(pupil_D)
        self.scene.add_object(oreil_G)
        self.scene.add_object(oreil_D)
        self.scene.add_object(nez)
        self.scene.add_object(bouche)
        self.scene.add_object(coup)
        self.scene.add_object(chapeau)
        self.scene.add_object(contour_H)
        self.scene.add_object(contour_B)
        self.scene.add_object(antenne)
        self.scene.add_object(cube_A)
        self.scene.add_object(box)
        self.scene.add_object(cube_Av)
        self.scene.add_object(cube_G)
        self.scene.add_object(cube_D)
        self.scene.add_object(cube_Ar)
        self.scene.add_object(bille)
        self.bille_id = self.scene.nb_objet

        self.scene.add_light(light1)