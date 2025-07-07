import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧪 Double-Slit Interference Simulation")
st.write("Simulates the interference pattern of particles like electrons in a quantum double-slit experiment.")
wavelength = st.sidebar.slider("Wavelength (arbitrary units)", 1.0, 20.0, 5.0, step=0.5)
slit_separation = st.sidebar.slider("Slit Separation", 10, 100, 20, step=1)
screen_distance = st.sidebar.slider("Screen Distance", 50, 300, 100, step=10)
slit_width = st.sidebar.slider("Slit Width", 1, 10, 4)
width = 400 
x = np.linspace(-width//2, width//2, width)
intensity = np.zeros_like(x)
k = 2 * np.pi / wavelength
for xi in range(width):
    r1 = np.sqrt(screen_distance**2 + (x[xi] - slit_separation/2)**2)
    r2 = np.sqrt(screen_distance**2 + (x[xi] + slit_separation/2)**2)

    wave1 = np.sin(k * r1) / r1
    wave2 = np.sin(k * r2) / r2

    intensity[xi] = (wave1 + wave2)**2
intensity /= intensity.max()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, intensity, color='blue')
ax.set_title("Interference Pattern on Screen")
ax.set_xlabel("Position on Screen")
ax.set_ylabel("Normalized Intensity")
ax.grid(True)
st.pyplot(fig)
st.caption("Based on Wilson–Sommerfeld wave quantization and classical interference principles.")
