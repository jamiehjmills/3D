from ursina import *

import PIL.Image

app=Ursina()


# Set the window size
window.size = (3000, 1280)  # Width, Height
window.title = 'Solar System Simulation'  # Set the window title

x=0
speed=1

cube=Entity(model="cube", color=color.yellow, position=(5,3,-1))

cube2=Entity(model="cube", color=color.blue, position=(5,-1,1))

def update():
    cube.rotation_x += 1
    cube2.rotation_x += 1
    # cube.rotation_z += 1
    # cube.rotation_y += 1
    global x, speed
    x += time.dt*speed

    # if abs(x) > 1:
    #     speed *= -1

    # camera.position=(0, 0, x)

app.run()