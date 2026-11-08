import os
from spectral import open_image

class HyperspectralLoader:
    def __init__(self, header_file_path: str):
        self.header_file_path = header_file_path

    def load_cube(self):
        """Loads a hyperspectral image cube from an ENVI header file."""
        if not os.path.exists(self.header_file_path):
            raise FileNotFoundError(f"Header file not found: {self.header_file_path}")
        
        try:
            img = open_image(self.header_file_path)
            cube = img.load()
            return cube
        except Exception as e:
            raise RuntimeError(f"Failed to load hyperspectral image: {e}")
