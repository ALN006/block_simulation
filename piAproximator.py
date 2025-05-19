from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
class block(object):

    ''' assumes blocks are objects that have a mass and x-axis velocity
    models blocks for thier behaviours (collisions) '''


    def __init__(self: "block", mass: float, velocity: float) -> None:

        self.mass = mass
        self.velocity = velocity


    def collide(self: "block", other: "block") -> None:

        '''changes the velocities of each block in occurdance with physics'''
        
        m1, v1 = self.mass, self.velocity
        m2, v2 = other.mass, other.velocity

        self.velocity = ((m1 - m2)*v1 + 2*m2*v2) / (m1 + m2)
        other.velocity = ((m2 - m1)*v2 + 2*m1*v1) / (m1 + m2)


    def get_velocity(self: "block") -> float:

        return self.velocity
    

    def get_mass(self: "block") -> float:

        return self.mass
    

    def set_velocity(self: "block", velocity: float) -> None:

        self.velocity = velocity



def collision_simulation(mass_factor: float) -> tuple[int, list, list]:

    L1 = []
    L2 = []
    b1 = block(mass_factor, -1.0)
    b2 = block(1.0, 0.0)
    collision_count = 0

    while not (b1.get_velocity() >= 0 and b2.get_velocity() >= 0 and b1.get_velocity() >= b2.get_velocity()):

        L1.append(b1.get_velocity())
        L2.append(b2.get_velocity())

        if collision_count%2 == 0:
            b1.collide(b2)
        else:
            b2.set_velocity(-b2.get_velocity())

        collision_count += 1

    L1.append(b1.get_velocity())
    L2.append(b2.get_velocity())

    return collision_count, L1, L2

def plot_VelocityVsVelocity(mass_factor):
    collision_count, L1, L2 = collision_simulation(mass_factor)
    plt.plot(L1, L2, label = f"collisions = {collision_count}")

def plot_VelocityVsCollision(mass_factor):

    collision_count, L1, _ = collision_simulation(mass_factor)

    y_vals = np.array([L1[i] for i in range(len(L1)) if i%2 == 0])
    x_vals = np.array([i for i in range(len(L1)) if i%2 == 0])
    
    def model_f(x, a, b, c, d):
        return a*x**3 + b*x**2 + c*x**1 + d
    
    constants, _ = curve_fit(model_f, x_vals, y_vals)
    a, b, c, d = constants
    estimates = a*x_vals**3 + b*x_vals**2 + c*x_vals**1 + d

    plt.scatter(x_vals, y_vals, label = f"collisions = {collision_count}", s= 10)
    plt.plot(x_vals, estimates, label = "3 degree fit", c = "red")

def plot(title: str, x_label: str, y_label: str, f: "function", \
         mass_factor: float) -> None:
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    f(mass_factor)

    plt.legend()
    plt.savefig(title)

plot("velocity_plot1", "block1", "block2", plot_VelocityVsVelocity, 1)
plot("velocity_plot2", "block1", "block2", plot_VelocityVsVelocity, 10**2)
plot("velocity_plot3", "block1", "block2", plot_VelocityVsVelocity, 10**4)
plot("velocity_plot4", "block1", "block2", plot_VelocityVsVelocity, 10**6)

plot("VelocityVsCollision2", "block1", "block2", plot_VelocityVsCollision, 10**2)
plot("VelocityVsCollision3", "block1", "block2", plot_VelocityVsCollision, 10**4)
plot("VelocityVsCollision4", "block1", "block2", plot_VelocityVsCollision, 10**6)