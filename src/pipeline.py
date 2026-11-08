
import numpy as np
from src.loader import HyperspectralLoader
from src.processing import HyperspectralProcessor

class HyperspectralPipeline:
    @staticmethod
    def process_file(file_path: str) -> np.ndarray:
        """Loads a hyperspectral data cube and applies normalization pipeline."""
        cube = HyperspectralLoader.load_cube(file_path)
        normalized_cube = HyperspectralProcessor.normalize_cube(cube)
        return normalized_cube

