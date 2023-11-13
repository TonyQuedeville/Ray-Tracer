"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

from math import sqrt
from vector import Vector3D
from ray import Ray_reflexion

# -----------------------------------------------------------------------------------------------------

# Sphère

class Sphere:
    def __init__(self, center=(0, 0, 5), radius=1.0, color=(1, 1, 1), reflexion=0.0):
        self.id = 0
        self.type = "sphere"
        self.center = Vector3D(*center)  # Centre de la sphère
        self.radius = radius  # Rayon de la sphère
        # self.color = color  # Couleur de la sphère
        self.color = (color[0] * (1-reflexion), color[1] * (1-reflexion), color[2] * (1-reflexion))
        self.reflexion = reflexion  # Propriétés de reflexion de la sphère
        
        self.incident_direction = None
        self.reflection_direction = None

    def intersect(self, ray):        
        # Calcul des coefficients de l'équation quadratique
        rs0 = ray.origin - self.center       
        a = ray.direction * ray.direction
        b = rs0 * ray.direction * 2.0
        c = rs0 * rs0 - self.radius**2

        # Calcul du discriminant
        discriminant = b * b - a * c * 4.0

        if discriminant > 0.0 :
            # Il y a deux points d'intersection
            t1 = (-b - sqrt(discriminant)) / (a * 2.0)
            t2 = (-b + sqrt(discriminant)) / (a * 2.0)

            # Renvoie le point d'intersection le plus proche du rayon
            if t1 > 0:
                hit_point = ray.origin + (ray.direction * t1)
                return t1, hit_point, self.color
            elif t2 > 0:
                hit_point = hit_point = ray.origin + (ray.direction * t2)
                return t2, hit_point, self.color

        # Pas d'intersection
        return None    
    
    def normal(self, hit_point):
        return (hit_point - self.center).normalize()
    
    def calculate_reflection_ray(self, incident_ray, hit_point):
        incident_direction = incident_ray.direction.normalize()
        normal = self.normal(hit_point)
        reflection_direction = incident_direction - ( normal * (normal * incident_direction) * 2)
        reflection_direction = reflection_direction.normalize()
        if reflection_direction * normal <= 0:
            return None
        reflection_ray = Ray_reflexion(hit_point + reflection_direction * 0.001, reflection_direction)
        self.incident_direction = incident_direction
        self.reflection_direction = reflection_direction
        return reflection_ray


    # Rendu de reflexion
    def reflet(self, scene, ray, depth=0, max_depth=5):
        color_vec = scene.color_fond
        
        # Intersection avec les objets de la scène
        closest_intersection = None
        obj = None
        
        for o in scene.objects:
            if o.reflexion <= 0:
                # Initialisation de la couleur par défaut
                light_color = Vector3D(0, 0, 0)            
            
                intersection = o.intersect(ray) # tuple(t, hit_point, color)
            
                # Selection de l'objet le plus proche
                if intersection is not None:
                    object_exclu = False
                    if o.type != "plane":
                        # Comparaison des coordonnées 
                        if ray.origin.x < self.center.x and self.center.x < o.center.x or ray.origin.y < self.center.y and self.center.y < o.center.y or ray.origin.z < self.center.z and self.center.z < o.center.z:
                            # print(f"Incident Direction: {self.incident_direction} Reflection Direction: {self.reflection_direction}")
                            # print(o.type, o.id, "exclu !")
                            object_exclu = True
                        elif ray.origin.x > self.center.x and self.center.x > o.center.x or ray.origin.y > self.center.y and self.center.y > o.center.y or ray.origin.z > self.center.z and self.center.z > o.center.z:
                            # print(f"Incident Direction: {self.incident_direction} Reflection Direction: {self.reflection_direction}")
                            # print(o.type, o.id, "exclu !")
                            object_exclu = True
                        else:
                            object_exclu = False
                    
                    if not object_exclu:
                        if closest_intersection is None or intersection[0] < closest_intersection[0]: # si l'objet suivant est plus proche que le précédent
                            closest_intersection = intersection
                            obj = o
                
                # Gestion de l'ombrage
                if obj is not None:            
                    t, hit_point, color = closest_intersection
                    obj_color = Vector3D(color[0], color[1], color[2]) 
                    normal = obj.normal(hit_point)  # Calcul la normale à la surface au point d'intersection
                    
                    # Lumière ambiante (diffuse)
                    if scene.lights:
                        color_vec = obj_color 
                    else:
                        color_vec = color_vec * scene.ambiante_intensity
                    
                    # Lumières projectionnelles (liste de projecteurs)
                    if scene.lights:
                        total_diffuse_intensity = 0
                        
                        # shaded_color = Vector3D(.1, .1, .1) / self.contrast
                        shaded_color = color_vec * scene.contrast
                        for light in scene.lights:                
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
                        
                        color_vec = color_vec / len(scene.lights)

        return Vector3D(color_vec.x, color_vec.y, color_vec.z)

# -----------------------------------------------------------------------------------------------------