"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

# Light

class Light:
    def __init__(self, position, intensity, color):
        self.position = position  # Position de la source lumineuse
        if intensity > 1:
            intensity = 1
        self.intensity = intensity  # Intensité lumineuse
        self.color = color  # Couleur de la lumière