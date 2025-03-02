from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

# press a to go left and d to go right
player=PlatformerController2d(model= 'sphere', y=1, scale_y=1)
ground=Entity(model='quad', y=-2, scale_x=10, collider='box', color=color.yellow)
wall=Entity(model='quad', x=5, scale_y=5, collider='box', color=color.yellow)
level=Entity(model='quad',x=3, scale_x=2, collider='box', color=color.red)

app.run()