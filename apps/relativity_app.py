from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fundamental_physics.relativity.time_dilation import lorentz_factor, traveler_time
from fundamental_physics.relativity.gravity_time_dilation import (
    SOLAR_MASS,
    schwarzschild_radius,
    gravitational_time_factor,
)

st.title("Fundamental Physics Sandbox")

st.header("Special relativity")

observer_years = st.slider("Observer time in years", 1.0, 100.0, 22.0)
beta = st.slider("Speed as fraction of light speed", 0.0, 0.999, 0.9)

gamma = lorentz_factor(beta)
traveler_years = traveler_time(observer_years, beta)

st.write(f"Lorentz factor: {gamma:.6f}")
st.write(f"Traveler time: {traveler_years:.6f} years")

st.header("Gravitational time dilation")

black_hole_mass = st.slider("Black hole mass in solar masses", 1.0, 100.0, 10.0)
distance_rs = st.slider("Distance in Schwarzschild radii", 1.01, 20.0, 5.0)

mass = black_hole_mass * SOLAR_MASS
rs = schwarzschild_radius(mass)
radius = distance_rs * rs
factor = gravitational_time_factor(mass, radius)

st.write(f"Schwarzschild radius: {rs:.2f} m")
st.write(f"Local time factor: {factor:.6f}")
st.write(f"Local time for 1 distant year: {factor:.6f} years")
