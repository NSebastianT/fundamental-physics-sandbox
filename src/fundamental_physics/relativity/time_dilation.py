from math import sqrt

C = 299_792_458

def lorentz_factor(beta):
    if beta < 0 or beta >= 1:
        raise ValueError("beta must be between 0 and 1")
    return 1 / sqrt(1 - beta**2)

def traveler_time(observer_time_years, beta):
    return observer_time_years / lorentz_factor(beta)

def observer_time(traveler_time_years, beta):
    return traveler_time_years * lorentz_factor(beta)
