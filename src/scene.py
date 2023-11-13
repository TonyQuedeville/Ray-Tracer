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

# Scène

class Scene:
    def __init__(self, width, height, camera, ambiante_intensity=1, contrast=1, objects=[], lights=[]):
        self.width = width
        self.height = height
        self.camera = camera  # Caméra de la scène
        self.objects = objects or [] # Liste d'objets dans la scène (sphères, cubes, cylindres, etc.)
        self.nb_objet = 0
        self.lights = lights  # Liste de sources lumineuses
        self.obj_name = ""
        self.nb_ray = 0
        self.color_fond = Vector3D(0.6, 0.6, 1)
        self.contrast = contrast # contrast entre 0 et 1
        
        self.ambiante_intensity = ambiante_intensity
        if ambiante_intensity > 1.0:
            ambiante_intensity = 1.0
        if ambiante_intensity > 0:
            self.ambiante_light = Vector3D(1,1,1)
        else:
            self.ambiante_light = None

    def set_camera(self, camera):
        # Méthode pour définir la caméra de la scène
        self.camera = camera

    def add_object(self, obj):
        # Méthode pour ajouter un objet géométrique à la scène
        self.objects.append(obj)
        self.nb_objet += 1
        obj.id = self.nb_objet

    def add_light(self, light):
        # Méthode pour ajouter une source lumineuse à la scène
        self.lights.append(light)

    def trace_ray(self, ray):        
        # Initialisation de la couleur par défaut
        color_vec = self.color_fond
        light_color = Vector3D(0, 0, 0)
    
        # Intersection avec les objets de la scène
        closest_intersection = None
        obj = None
        nb_obj = 0

        for o in self.objects:
            nb_obj =+ 1
            intersection = o.intersect(ray) # tuple(t, hit_point, color)

            # Selection de l'objet le plus proche
            if intersection is not None:                        
                if closest_intersection is None or intersection[0] < closest_intersection[0]: # si l'objet suivant est plus proche que le précédent
                    closest_intersection = intersection
                    obj = o

        # Gestion de l'ombrage
        if obj is not None:            
            t, hit_point, color = closest_intersection
            obj_color = Vector3D(color[0], color[1], color[2])
            normal = obj.normal(hit_point)  # Calcul la normale à la surface au point d'intersection

            # Lumière ambiante (diffuse)
            if self.lights:
                color_vec = obj_color 
            else:
                color_vec = color_vec * self.ambiante_intensity
            
            # Réflexions
            if obj.id != nb_obj and obj.reflexion > 0:
                reflection_ray = obj.calculate_reflection_ray(ray, hit_point)
                if reflection_ray is None:
                    color_vec = Vector3D(*obj.color)
                else:
                    reflected_color = obj.reflet(self, reflection_ray)
                    color_vec = Vector3D(*obj.color) + reflected_color 
            
            # Lumières projectionnelles (liste de projecteurs)
            if self.lights:
                total_diffuse_intensity = 0

                shaded_color = color_vec * self.contrast
                
                for light in self.lights:                
                    light_position = Vector3D(light.position[0], light.position[1], light.position[2])
                    light_color = Vector3D(light.color[0], light.color[1], light.color[2])                    
                    light_direction = (light_position - hit_point).normalize()
                    lambert = max(0, normal * light_direction)
                    diffuse_intensity =  lambert * light.intensity
                    
                    total_diffuse_intensity += diffuse_intensity
                    
                    color_light = Vector3D(
                        color_vec.x * light_color.x * total_diffuse_intensity,
                        color_vec.y * light_color.y * total_diffuse_intensity,
                        color_vec.z * light_color.z * total_diffuse_intensity
                        )
                    color_vec = shaded_color + color_light
                    
                color_vec.x = min(1., color_vec.x)
                color_vec.y = min(1., color_vec.y)
                color_vec.z = min(1., color_vec.z)
                
                color_vec = color_vec / len(self.lights)        

                # Ombres
        
        return (color_vec.x, color_vec.y, color_vec.z) # couleur du pixel R,G,B