from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fundamental_physics.relativity.time_dilation import lorentz_factor

betas = [i / 1000 for i in range(0, 1000)]
gammas = [lorentz_factor(beta) for beta in betas]

output_dir = ROOT / "outputs"
output_dir.mkdir(exist_ok=True)

plt.figure()
plt.plot(betas, gammas)
plt.xlabel("Speed as fraction of light speed")
plt.ylabel("Lorentz factor")
plt.title("Time dilation vs speed")
plt.grid(True)
plt.savefig(output_dir / "time_dilation_curve.png", dpi=200)
plt.show()
