"""
    Projet Zone01 Ray Tracer
    Tony Quedeville
    02/11/2023
"""

# -----------------------------------------------------------------------------------------------------

from vector import Vector3D

# -----------------------------------------------------------------------------------------------------

# Cube

class Cube:
    def __init__(self, center=(0, 0, 0), size=(1, 1, 1), color=(1, 1, 1), reflexion=0):
        self.id = 0
        self.type = "cube"
        self.center = Vector3D(*center)  # Centre du cube
        self.size = size      # Taille du cube (vecteur pour en faire un pavé aux arretes de logueurs différentes)
        self.color = color    # Couleur du cube
        self.reflexion = reflexion  # Propriétés de reflexion
        
    def intersect(self, ray):
        ray_origin = ray.origin
        ray_direction = ray.direction
        # ray_origin = Vector3D(ray_origin[0], ray_origin[1], ray_origin[2])

        t_near = float('-inf')
        t_far = float('inf')

        for i in range(3):
            if i == 0:
                if ray_direction.x == 0:
                    if ray_origin.x < self.center.x - self.size[i] / 2 or ray_origin.x > self.center.x + self.size[i] / 2:
                        return None
                else:
                    t1x = (self.center.x - self.size[i] / 2 - ray_origin.x) / ray_direction.x
                    t2x = (self.center.x + self.size[i] / 2 - ray_origin.x) / ray_direction.x
                    t_near = max(t_near, min(t1x, t2x))
                    t_far = min(t_far, max(t1x, t2x))
            elif i == 1:
                if ray_direction.y == 0:
                    if ray_origin.y < self.center.y - self.size[i] / 2 or ray_origin.y > self.center.y + self.size[i] / 2:
                        return None
                else:
                    t1y = (self.center.y - self.size[i] / 2 - ray_origin.y) / ray_direction.y
                    t2y = (self.center.y + self.size[i] / 2 - ray_origin.y) / ray_direction.y
                    t_near = max(t_near, min(t1y, t2y))
                    t_far = min(t_far, max(t1y, t2y))
            elif i == 2:
                if ray_direction.z == 0:
                    if ray_origin.z < self.center.z - self.size[i] / 2 or ray_origin.z > self.center.z + self.size[i] / 2:
                        return None
                else:
                    t1z = (self.center.z - self.size[i] / 2 - ray_origin.z) / ray_direction.z
                    t2z = (self.center.z + self.size[i] / 2 - ray_origin.z) / ray_direction.z
                    t_near = max(t_near, min(t1z, t2z))
                    t_far = min(t_far, max(t1z, t2z))

        if t_near <= t_far:
            hit_point = ray_origin + ray_direction * t_near
            return t_near, hit_point, self.color

        return None

    def normal(self, hit_point):
        # Calcule la différence entre le point d'intersection et le centre du cube
        diff = hit_point - self.center

        # half_size = Vector3D(self.size[0] / 2, self.size[1] / 2, self.size[2] / 2)

        if abs(diff.x) >= abs(diff.y) and abs(diff.x) >= abs(diff.z):
            if diff.x > 0:
                return Vector3D(1, 0, 0)
            else:
                return Vector3D(-1, 0, 0)
        elif abs(diff.y) >= abs(diff.x) and abs(diff.y) >= abs(diff.z):
            if diff.y > 0:
                return Vector3D(0, 1, 0)
            else:
                return Vector3D(0, -1, 0)
        else:
            if diff.z > 0:
                return Vector3D(0, 0, 1)
            else:
                return Vector3D(0, 0, -1)
