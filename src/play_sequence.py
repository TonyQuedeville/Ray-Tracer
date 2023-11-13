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

def play_sequence(seq=None):
    # Initialisation
    if seq is None: 
        return None
    
    images_ppm = []
    file_name = seq[0]
    nb_img= seq[1]
    id_img = 0
    sens = 1
    pause = False
    
    # Initialisez Pygame
    pygame.init()

    # Chargez l'image PPM
    for img_id in range(nb_img):
        images_ppm.append(pygame.image.load('../images/' + file_name + str(img_id) + '.ppm'))
    
    # Créez une fenêtre Pygame de la taille de l'image
    screen = pygame.display.set_mode(images_ppm[0].get_size())
    
    # Horloge pour cadencer la boucle infinie. (Eviter la surchauffe du processeur)
    clock = pygame.time.Clock()
    
    # Affichez l'image dans la fenêtre
    screen.blit(images_ppm[id_img], (0, 0))
    
    # Rafraîchissez l'écran
    pygame.display.flip()

    # Attendez que l'utilisateur ferme la fenêtre
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE: 
                    if pause == False:
                        pause = True
                    else:
                        pause = False
                elif event.key == pygame.K_LEFT: 
                    id_img += 1
                    if id_img >= nb_img - 1:
                        id_img = 0
                elif event.key == pygame.K_RIGHT:
                    id_img -= 1
                    if id_img < 0:
                        id_img = nb_img - 1
        
        if not pause :
            if nb_img > 1:
                if id_img >= nb_img - 1:
                    sens = -1
                if id_img <= 0:
                    sens = 1
                id_img += sens
        
        # Afficher l'image dans la fenêtre
        screen.blit(images_ppm[id_img], (0, 0))            
        # Rafraîchi l'écran
        pygame.display.flip()
    
        # Limiter la boucle à x FPS (cadence de jeu)
        clock.tick_busy_loop(10)

    # Quittez Pygame
    pygame.quit()