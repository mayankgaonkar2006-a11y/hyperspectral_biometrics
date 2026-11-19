import numpy as np
import spectral.io.envi as envi
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class HyperspectralClassifier:
    @staticmethod
    def load_cube(hdr_path: str, img_path: str = None) -> np.ndarray:
        """Loads an ENVI hyperspectral cube into a 3D NumPy array."""
        img = envi.open(hdr_path, img_path)
        return np.array(img.load(), dtype=float)

    @staticmethod
    def run_kmeans_segmentation(data_cube: np.ndarray, n_clusters: int = 7, max_iter: int = 30) -> np.ndarray:
        """Flattens 3D cube to 2D pixel vectors, runs K-Means, and reconstructs 2D map."""
        height, width, bands = data_cube.shape
        pixel_tokens = data_cube.reshape(-1, bands)
        
        kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, random_state=42, n_init=10)
        labels = kmeans.fit_predict(pixel_tokens)
        
        return labels.reshape(height, width)

    @staticmethod
    def save_visual_map(segmented_map: np.ndarray, output_path: str = "output_segmentation.png"):
        """Generates a color-mapped visual image for the UI and PPT presentation."""
        plt.figure(figsize=(8, 6))
        plt.imshow(segmented_map, cmap="nipy_spectral")
        plt.colorbar(label="Material Cluster ID")
        plt.title("Hyperspectral Unsupervised Material Segmentation")
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()