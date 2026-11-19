import matplotlib.pyplot as plt
import spectral.io.envi as envi

# Load the Seurat_BEFORE ENVI cube
img = envi.open("data/Seurat_BEFORE.hdr", "data/Seurat_BEFORE.img")
cube = img.load()

# Pick a sample pixel and squeeze extra dimensions to 1D
r, c = cube.shape[0] // 2, cube.shape[1] // 2
spectrum = cube[r, c, :].squeeze()

plt.figure(figsize=(6, 4))
plt.plot(spectrum, color="#008080", linewidth=2)
plt.title(f"Spectral Signature at Pixel ({r}, {c}) — Seurat_BEFORE")
plt.xlabel("Band Index")
plt.ylabel("Reflectance / Intensity")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("seurat_spectrum.png", dpi=300)
plt.show()