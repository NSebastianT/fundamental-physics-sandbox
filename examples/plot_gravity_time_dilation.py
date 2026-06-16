from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fundamental_physics.relativity.gravity_time_dilation import (
    SOLAR_MASS,
    schwarzschild_radius,
    gravitational_time_factor,
)

mass = 10 * SOLAR_MASS
rs = schwarzschild_radius(mass)

multipliers = [1.01 + i * 0.02 for i in range(1000)]
factors = [gravitational_time_factor(mass, m * rs) for m in multipliers]

output_dir = ROOT / "outputs"
output_dir.mkdir(exist_ok=True)

plt.figure()
plt.plot(multipliers, factors)
plt.xlabel("Distance from center in Schwarzschild radii")
plt.ylabel("Local time factor")
plt.title("Gravitational time dilation near a black hole")
plt.grid(True)
plt.savefig(output_dir / "gravitational_time_dilation_curve.png", dpi=200)
plt.show()
