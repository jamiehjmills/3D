from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

entities=[]

size=13
bg=Entity(model='quad', scale=(size,10), texture='assets/sky.jpg',z=1)

# press a to go left and d to go right
player=PlatformerController2d(model= 'quad', y=2, scale_y=1, texture='assets/guy.png', color=color.white)
ground=Entity(model='quad', y=-2, scale_x=10, collider='box', color=color.yellow)
# duplicate(ground, x=size)
# duplicate(ground, x=-size)

wall=Entity(model='quad', x=5, scale_y=5, collider='box', color=color.yellow)
# duplicate(wall, x=size)
# duplicate(wall, x=-size)

level=Entity(model='quad',x=3, scale_x=2, collider='box', color=color.red)
# duplicate(level, x=size)
# duplicate(level, x=-size)

entities.append(bg)
entities.append(player)
entities.append(ground)
entities.append(wall)
entities.append(level)

for entity in entities:
    if entity!=player:
        duplicate(entity, x=size)
        duplicate(entity, x=-size)



camera.add_script(SmoothFollow(target=player, offset=[0,1,-50], speed=4))

app.run()

#TODO: continue on https://www.youtube.com/watch?v=CBNyPralr3E&list=PLgQYnHnDxgtjILmQbQXQeUTHiLLSRkSuk&index=3
#INFORMATION: https://github.com/mk-codingspace/Python/blob/9dea9a3ce47704e96b928295f34975cc69323c7e/Ursina-Platformer-Intro/assets/guy.png