from ursina import *
from planet import Planet

app = Ursina()
solar_system = Planet()

# Set the window size
window.size = (3000, 1280)  # Width, Height
window.title = 'Solar System Simulation'  # Set the window title

#orbit_radius=1
x=0
speed=1
angle=3
angle_mercury = 1
angle_venus = 1
angle_earth = 1
angle_mars = 1
angle_jupiter = 1
angle_saturn = 1
angle_uranus = 1
angle_neptune = 1

# Create a sphere entity
#sun = Entity(model='sphere', color=color.yellow, scale=1, position=(0, 0, 0))
#mercury = Entity(model='sphere', color=color.green, scale=0.04, position=(0, 0, 0))
sun = solar_system.create_entity('sun', 1, 0, color.yellow)
mercury = solar_system.create_entity('mercury', 0.04, 0, '#B7B8B9')
venus = solar_system.create_entity('venus', 0.09, 0, '#877882')
earth = solar_system.create_entity('earth', 0.09, 0, '#6b93d6')
mars = solar_system.create_entity('mars', 0.05, 0, '#c1440e')
jupiter = solar_system.create_entity('jupiter', 1.03, 0, '#c99039')
saturn = solar_system.create_entity('saturn', 0.87, 0, '#e3e0c0')
uranus = solar_system.create_entity('uranus', 0.37, 0, '#ACE5EE')
neptune = solar_system.create_entity('neptune', 0.36, 0, '#5b5ddf')

def update():
    # global x, speed
    # x += time.dt*speed
    global angle_mercury, angle_venus, angle_earth, angle_mars, angle_jupiter, angle_saturn, angle_uranus, angle_neptune
    #angle += time.dt * speed

    sun.rotation_y += 1  # Rotate the sphere around the y-axis

    # mercury
    angle_mercury += time.dt * speed
    mercury.x = 1.158 * math.cos(angle_mercury)
    mercury.z = 1.158 * math.sin(angle_mercury)
    mercury.rotation_z += 1

    # venus
    angle_venus += time.dt * speed
    venus.x = 2.164 * math.cos(angle_venus)
    venus.z = 2.164 * math.sin(angle_venus)

    # earth
    angle_earth += time.dt * speed
    earth.x = 2.992 * math.cos(angle_earth)
    earth.z = 2.992 * math.sin(angle_earth)

    # mars
    angle_mars += time.dt * speed
    mars.x = 4.558 * math.cos(angle_mars)
    mars.z = 4.558 * math.sin(angle_mars)

    # jupiter
    angle_jupiter += time.dt * speed
    jupiter.x = 5.572 * math.cos(angle_jupiter)
    jupiter.z = 5.572 * math.sin(angle_jupiter)

    # saturn
    angle_saturn += time.dt * speed
    saturn.x = 7.67 * math.cos(angle_saturn)
    saturn.z = 7.67 * math.sin(angle_saturn)

    # uranus
    angle_uranus += time.dt * speed
    uranus.x = 8.45 * math.cos(angle_uranus)
    uranus.z = 8.45 * math.sin(angle_uranus)

    # neptune
    angle_neptune += time.dt * speed
    neptune.x = 9.902 * math.cos(angle_neptune)
    neptune.z = 9.902 * math.sin(angle_neptune)

    #camera.position = (0, 0, 1)  # Example position
    # if abs(x) > 3:
    #     speed *= -1

app.run()

## TO DO: https://www.ursinaengine.org/entity_basics.html#Position <-- read documentation!!