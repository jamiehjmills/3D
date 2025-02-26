from ursina import *

app=Ursina()

x=0
speed=1

def update():
    # cube.rotation_x += 1
    # cube.rotation_z += 1
    # cube.rotation_y += 1
    global x, speed
    x += time.dt*speed

    if abs(x) > 3:
        speed *= -1

    camera.position=(x, 0, -20)

cube=Entity(model="cube", color=color.yellow, position=(1,0,10))

app.run()