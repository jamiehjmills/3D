from ursina import *

class Planet():
    def __init__(self):
        self.entities = {}

    def create_entity(self, name, radius, distance, color):
         entity = Entity(model='sphere', color=color, scale=(radius, radius, radius), position=(distance, 0, 0))
         self.entities[name] = entity
         return entity
