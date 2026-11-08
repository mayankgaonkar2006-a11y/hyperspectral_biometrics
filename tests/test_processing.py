import numpy as np
from src.processing import HyperspectralProcessor

def test_normalize_cube():
    """Test that HyperspectralProcessor normalizes data between 0 and 1."""
    dummy_cube = np.array([[[10.0, 20.0], [30.0, 40.0]]])
    normalized = HyperspectralProcessor.normalize_cube(dummy_cube)
    
    assert np.min(normalized) == 0.0
    assert np.max(normalized) == 1.0
