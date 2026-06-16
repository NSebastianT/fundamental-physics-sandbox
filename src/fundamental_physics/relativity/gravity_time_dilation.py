from math import sqrt

G = 6.67430e-11
C = 299_792_458

SOLAR_MASS = 1.98847e30
EARTH_MASS = 5.9722e24

def schwarzschild_radius(mass_kg):
    return 2 * G * mass_kg / C**2

def gravitational_time_factor(mass_kg, radius_m):
    rs = schwarzschild_radius(mass_kg)

    if radius_m <= rs:
        raise ValueError("radius must be outside the Schwarzschild radius")

    return sqrt(1 - rs / radius_m)

def local_time(distant_observer_time, mass_kg, radius_m):
    return distant_observer_time * gravitational_time_factor(mass_kg, radius_m)
