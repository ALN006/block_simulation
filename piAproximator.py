from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


class block(object):
    """assumes blocks are objects that have a mass and x-axis velocity
    models blocks for their behaviours (collisions)"""

    def __init__(self: "block", mass: float | int, velocity: float | int) -> None:
        self.mass = mass
        self.velocity = velocity

    def collide(self: "block", other: "block") -> None:
        """changes the velocities of each block in accordance with physics"""

        m1, v1 = self.mass, self.velocity
        m2, v2 = other.mass, other.velocity

        self.velocity = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        other.velocity = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

    def get_velocity(self: "block") -> float:
        return self.velocity

    def get_mass(self: "block") -> float:
        return self.mass

    def set_velocity(self: "block", velocity: float) -> None:
        self.velocity = velocity


# a simulation of the pi collisions scenario
def collision_simulation(
    mass_factor: float | int,
) -> tuple[int, list[float], list[float]]:
    """assumes 1 block is mass_factor times as massive as a secondstationary block and is initially
    incumbant on said block with unit negative velocity

    simulates linear elastic collision between 2 blocks and a wall as seen in the pi collisions scenario
    the simulation does not factor, measure or utilize time

    returns the number of collisions that occur and a list of velocities in each collision"""

    L1, L2 = [], []
    b1 = block(mass_factor, -1.0)
    b2 = block(1.0, 0.0)
    collision_count = 0

    while not (
        b1.get_velocity() >= 0
        and b2.get_velocity() >= 0
        and b1.get_velocity() >= b2.get_velocity()
    ):
        L1.append(b1.get_velocity())
        L2.append(b2.get_velocity())

        if collision_count % 2 == 0:
            b1.collide(b2)
        else:
            b2.set_velocity(-b2.get_velocity())

        collision_count += 1

    L1.append(b1.get_velocity())
    L2.append(b2.get_velocity())

    return collision_count, L1, L2


def plot_VelocityVsVelocity(mass_factor: float | int, model_f=None) -> None:
    """plots velocity of one block versus another which is mass_factor times as massive
    and incumbant with unit negative velocity on a set up as described by the pi collisions scenario"""

    collision_count, L1, L2 = collision_simulation(mass_factor)
    plt.plot(np.array(L1)*mass_factor**0.5,L2, label=f"collisions = {collision_count}")
    if model_f:
        poly_fit(np.array(L1), L2, model_f)


def plot_VelocityVsCollision(mass_factor: float | int, model_f=None) -> None:
    """plots velocity of the more massive block (as described in the pi collisions scenario)
    at even numbered collisions versus the collision number at fits a 3 degree polynomial onto the curve"""

    collision_count, L1, _ = collision_simulation(mass_factor)

    y_vals = np.array([L1[i] for i in range(len(L1)) if i % 2 == 0])
    x_vals = np.array([i for i in range(len(L1)) if i % 2 == 0])

    plt.scatter(x_vals, y_vals, label=f"collisions = {collision_count}", s=10)
    if model_f:
        poly_fit(x_vals, y_vals, model_f)


def plot(
    title: str,
    x_label: str,
    y_label: str,
    plotting_function,
    mass_factor: float,
    model_f=None,
) -> None:
    """assigns titles and saves a figure"""

    plt.figure(figsize=(7,7))
    plt.title(title + f" (mass factor {mass_factor})")
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plotting_function(mass_factor, model_f)

    plt.legend()
    plt.savefig(title)


def poly_fit(x_vals: np.array, y_vals: np.array, model_f) -> None:
    """fits a polinomial onto the given 2 dimensional data"""
    constants, _ = curve_fit(model_f, x_vals, y_vals)
    pow = len(constants) - 1
    estimates = np.array([0.0] * len(x_vals))
    for i in constants:
        estimates += i * x_vals**pow
        pow -= 1
    plt.plot(x_vals, estimates, label=f"{len(constants) - 1} degree fit", c="red")


def cubic(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x**1 + d


def quadratic(x, a, b, c):
    return a * x**2 + b * x**1 + c


def linear(x, a, b):
    return a * x + b
