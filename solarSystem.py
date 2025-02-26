from ursina import *

app = Ursina()

orbit_radius=3
x=0
speed=1
angle=0

# Create a sphere entity
sun = Entity(model='sphere', color=color.yellow, scale=(1, 1, 1), position=(0, 0, 0))
earth = Entity(model='sphere', color=color.green, scale=0.5, position=(3, 0, 0))

def update():
    # global x, speed
    # x += time.dt*speed
    global angle
    angle += time.dt * speed

    # if abs(x) > 3:
    #     speed *= -1

    # camera.position=(0, 0, -20)

    sun.rotation_y += 1  # Rotate the sphere around the y-axis
    earth.x = orbit_radius * math.cos(angle)
    #earth.y = orbit_radius * math.sin(angle)
    earth.z = orbit_radius * math.sin(angle)

app.run()

## TO DO: create the rest of the planets in the solar system!! (28 Feb 2024)