
import numpy as np

class HyperspectralProcessor:
    @staticmethod
    def normalize_cube(cube: np.ndarray) -> np.ndarray:
        """Normalizes hyperspectral data cube values between 0 and 1."""
        min_val = np.min(cube)
        max_val = np.max(cube)
        if max_val - min_val == 0:
            return np.zeros_like(cube, dtype=float)
        return (cube - min_val) / (max_val - min_val)

