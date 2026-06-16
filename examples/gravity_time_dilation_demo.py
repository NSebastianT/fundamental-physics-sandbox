from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fundamental_physics.relativity.gravity_time_dilation import (
    SOLAR_MASS,
    schwarzschild_radius,
    gravitational_time_factor,
    local_time,
)

mass = 10 * SOLAR_MASS
rs = schwarzschild_radius(mass)

print("Gravitational time dilation examples")
print("------------------------------------")
print(f"Black hole mass: 10 solar masses")
print(f"Schwarzschild radius: {rs:.2f} m")
print()

for multiplier in [10, 5, 3, 2, 1.5, 1.1]:
    radius = multiplier * rs
    factor = gravitational_time_factor(mass, radius)
    time = local_time(1, mass, radius)

    print(f"At {multiplier} Rs: time factor = {factor:.6f}, local time = {time:.6f} years")
