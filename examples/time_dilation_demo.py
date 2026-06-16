from src.fundamental_physics.relativity.time_dilation import lorentz_factor, traveler_time

age = 22
speeds = [0.1, 0.5, 0.9, 0.99, 0.999]

print("Time dilation examples")
print("----------------------")

for beta in speeds:
    gamma = lorentz_factor(beta)
    time = traveler_time(age, beta)
    print(f"At {beta}c: gamma = {gamma:.4f}, traveler time = {time:.4f} years")
