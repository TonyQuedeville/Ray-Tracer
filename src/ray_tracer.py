"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
    
    Liens utiles :
    https://physique.cmaisonneuve.qc.ca/svezina/nyc/note_nyc/NYC_CHAP_6_IMPRIMABLE_4.pdf
"""

# -----------------------------------------------------------------------------------------------------

#  Imports

import pygame
from vector import Vector3D
from generate_sequence import generate_sequence
from play_sequence import play_sequence
from image import Image
from clown import Clown
from pillule import Pillule

# -----------------------------------------------------------------------------------------------------

# Main
def main():
    # seq = ('image', 1)    
    # image = Image(seq)
    # classe = image
    
    # seq = ('pillule', 1)    
    # pillule = Pillule(seq)
    # classe = pillule
    
    seq = ('clown', 31)    
    # clown = Clown(seq)
    # classe = clown
    
    # generate_sequence(classe) 
    
    if play_sequence(seq) is None:
        print("Pas de sequence !")

if __name__ == "__main__":
    main()