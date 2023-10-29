import math
from render import InitRender, Render

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    """Returns the distance between two bodies"""
    mass,(x1,y1),(xv1,yv1) = body1
    mass,(x2,y2),(xv2,yv2) = body2

    distance = math.sqrt((x1-x2)**2 +(y1-y2)**2)

    return distance


def calculate_force(body1, body2):
    """Returns the force exerted on body1 by body2, in 2 dimensions as a tuple"""
    G = 6.67e-11

    m1,(x1,y1),(xv1,yv1) = body1
    m2,(x2,y2),(xv2,yv2) = body2

    dx = x2 - x1
    dy = y2 - y1

    # Calculate the distance between the two bodies (magnitude of the vector)
    r = math.sqrt(dx**2 + dy**2)

    # Calculate the gravitational force in each dimension
    Fx = (G * m1 * m2 / r**2) * (dx / r)
    Fy = (G * m1 * m2 / r**2) * (dy / r)

    # Return the force as a 2D vector (tuple)
    return (Fx, Fy)


body1 = (1, (0, 0), (0, 0))
body2 = (1, (1, 0), (0, 0))
print(calculate_force(body1,body2))


def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""

    net_force = (0, 0)

    for other_body in system:
        if other_body != body: 
            force = calculate_force(body, other_body)
            net_force = (net_force[0] + force[0], net_force[1] + force[1])

    return net_force



def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    #f = ma
    m, (x, y), (xv, yv) = body

    net_force = calculate_net_force_on(body, system)

    ax = net_force[0] / m
    ay = net_force[1] / m

    accel = (ax, ay)

    return accel
    


def update_velocity(system, dt):
    updated_system = []

    for body in system:
        m, (x, y), (vx, vy) = body
        accel = calculate_acceleration(body, system)

        new_vx = vx + accel[0] * dt
        new_vy = vy + accel[1] * dt

        new_body = (m, (x, y), (new_vx, new_vy))

        updated_system.append(new_body)

    return updated_system
   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    updated_system = []

    for body in system:
        m, (x, y), (vx, vy) = body

        accel = calculate_acceleration(body, system)
        new_vx = vx + accel[0] * dt
        new_vy = vy + accel[1] * dt

        new_x = x + new_vx*dt
        new_y = y + new_vy*dt

        new_body = m, (new_x,new_y), (new_vx,new_vy)

        updated_system.append(new_body)

    return updated_system



def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    updated_system = []

    for body in system:
        m, (x, y), (vx, vy) = body

        accel = calculate_acceleration(body, system)
        new_vx = vx + accel[0] * dt*num_steps
        new_vy = vy + accel[1] * dt*num_steps

        new_x = x + new_vx*dt
        new_y = y + new_vy*dt

        new_body = m, (new_x,new_y), (new_vx,new_vy)

        updated_system.append(new_body)

    return updated_system

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass





