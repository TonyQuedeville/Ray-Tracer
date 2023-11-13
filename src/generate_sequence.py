"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

#  Imports

import pygame
from vector import Vector3D
from camera import Camera
from scene import Scene
from clown import Clown
from sphere import Sphere
from cylinder import Cylinder
from cube import Cube
from light import Light

# -----------------------------------------------------------------------------------------------------

def generate_sequence(classe=None):  
    # Initialisation
    if classe is None: 
        return None
    
    file_name = classe.seq[0]
    nb_img= classe.seq[1]
    
    #  Première image d'initialisation
    xp, yp, zp = classe.camera_start_P
    xl, yl,zl = classe.camera_start_L
    xb, yb, zb = classe.bille_start 
    
    print("------ image :", file_name + str(0), ".ppm ------")
    print("position camera: (" , xp, ":", yp, ":", zp, ")")
    print("direction camera: (" , xl, ":", yl, ":", zl, ")")
    classe.scene.camera.origin = Vector3D(xp, yp, zp)
    classe.scene.camera.look_at = Vector3D(xl, yl, zl)
    print("position bille: (" , xb, ":", yb, ":", zb, ")")
    classe.scene.objects[classe.bille_id - 1].center = Vector3D(xb, yb, zb)
    
    # Rendu de l'image
    rendered_image = render_image(classe.scene, classe.width, classe.height)

    # Sauvegardez l'image générée
    save_image(rendered_image, '../images/' + file_name + str(0) + '.ppm')
    
    # Images suivantes
    for img_id in range(nb_img-1):
        xp = (classe.camera_end_P[0] - classe.camera_start_P[0]) / (nb_img - 1) * (img_id + 1) + classe.camera_start_P[0]
        yp = (classe.camera_end_P[1] - classe.camera_start_P[1]) / (nb_img - 1) * (img_id + 1) + classe.camera_start_P[1]
        zp = (classe.camera_end_P[2] - classe.camera_start_P[2]) / (nb_img - 1) * (img_id + 1) + classe.camera_start_P[2]
        xl = (classe.camera_end_L[0] - classe.camera_start_L[0]) / (nb_img - 1) * (img_id + 1) + classe.camera_start_L[0]
        yl = (classe.camera_end_L[1] - classe.camera_start_L[1]) / (nb_img - 1) * (img_id + 1) + classe.camera_start_L[1]
        zl = (classe.camera_end_L[2] - classe.camera_start_L[2]) / (nb_img - 1) * (img_id + 1) + classe.camera_start_L[2]
        
        xb = (classe.bille_end[0] - classe.bille_start[0]) / (nb_img - 1) * (img_id + 1) + classe.bille_start[0]
        yb = (classe.bille_end[1] - classe.bille_start[1]) / (nb_img - 1) * (img_id + 1) + classe.bille_start[1]
        zb = (classe.bille_end[2] - classe.bille_start[2]) / (nb_img - 1) * (img_id + 1) + classe.bille_start[2]
        
        print("------ image :", file_name + str(img_id+1), ".ppm ------")
        print("position camera: (" , xp, ":", yp, ":", zp, ")")
        print("direction camera: (" , xl, ":", yl, ":", zl, ")")
        classe.scene.camera.origin = Vector3D(xp, yp, zp)
        classe.scene.camera.look_at = Vector3D(xl, yl, zl)
        print("position bille: (" , xb, ":", yb, ":", zb, ")")
        classe.scene.objects[classe.bille_id - 1].center = Vector3D(xb, yb, zb)
        
        # Rendu de l'image
        rendered_image = render_image(classe.scene, classe.width, classe.height)

        # Sauvegardez l'image générée
        save_image(rendered_image, '../images/' + file_name + str(img_id+1) + '.ppm')

# -----------------------------------------------------------------------------------------------------

# Rendu de l'image
def render_image(scene, width, height):
    #  Initialisation de l'image en Noire
    image = [[(0, 0, 0) for _ in range(int(width))] for _ in range(int(height))]

    # Définition des pixels par objet
    for y in range(int(height)):
        for x in range(int(width)):
            # Rayon correspondant à un pixel de l'image
            ray = scene.camera.generate_ray(x, y)

            # Lancer du rayon et obtention de la couleur
            color = scene.trace_ray(ray)

            # Couleur du pixel de l'image
            image[y][x] = color

    return image

# -----------------------------------------------------------------------------------------------------

#  Sauvegarde de l'image
def save_image(image, filename):
    # Méthode pour enregistrer une image au format PPM
    with open(filename, 'w') as f:
        # Én-tête du fichier PPM
        f.write("P3\n")
        f.write(f"{len(image[0])} {len(image)}\n")
        f.write("255\n")

        # Pixels
        for row in image:
            for pixel in row:
                r, g, b = pixel
                f.write(f"{int(r * 255)} {int(g * 255)} {int(b * 255)}\n")

# -----------------------------------------------------------------------------------------------------
