import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title(" Double-Slit Interference Simulation")
st.write("Simulates the interference pattern of particles like electrons in a quantum double-slit experiment.")
st.subheader(" Interference Equations")
st.latex(r"""
k = \frac{2\pi}{\lambda} \quad \text{(wave number)}
""")
st.latex(r"""
r_1 = \sqrt{D^2 + \left(x - \frac{d}{2}\right)^2}, \quad r_2 = \sqrt{D^2 + \left(x + \frac{d}{2}\right)^2}
""")
st.latex(r"""
\psi(x) = \frac{\sin(k r_1)}{r_1} + \frac{\sin(k r_2)}{r_2}
""")
st.latex(r"""
I(x) \propto \left| \psi(x) \right|^2
""")

wavelength_nm = st.sidebar.slider("Wavelength (nanometers)", 100.0, 1000.0, 500.0, step=10.0)
slit_separation_um = st.sidebar.slider("Slit Separation (micrometers)", 10.0, 200.0, 50.0, step=1.0)
screen_distance_cm = st.sidebar.slider("Screen Distance (cm)", 1.0, 100.0, 10.0, step=1.0)
slit_width_um = st.sidebar.slider("Slit Width (μm - not used yet)", 1.0, 20.0, 5.0, step=0.5)

# Convert units to meters
wavelength = wavelength_nm * 1e-9
slit_separation = slit_separation_um * 1e-6
screen_distance = screen_distance_cm * 1e-2

# Simulation grid
width = 400  # number of screen points
x = np.linspace(-1e-2, 1e-2, width)  # ±1 cm on screen
intensity = np.zeros_like(x)

# Wave number
k = 2 * np.pi / wavelength
for xi in range(width):
    r1 = np.sqrt(screen_distance**2 + (x[xi] - slit_separation/2)**2)
    r2 = np.sqrt(screen_distance**2 + (x[xi] + slit_separation/2)**2)

    wave1 = np.sin(k * r1) / r1
    wave2 = np.sin(k * r2) / r2

    intensity[xi] = (wave1 + wave2)**2

# Normalize
intensity /= intensity.max()

# Plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x * 1e3, intensity, color='blue')  # convert x to mm for display
ax.set_title("Interference Pattern on Screen")
ax.set_xlabel("Position on Screen (mm)")
ax.set_ylabel("Normalized Intensity")
ax.grid(True)
st.pyplot(fig)

st.caption("Simulation based on classical wave interference and quantum amplitude superposition.")
