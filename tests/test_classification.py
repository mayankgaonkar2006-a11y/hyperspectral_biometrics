import numpy as np
from src.classification import HyperspectralClassifier

def test_kmeans_segmentation_shape():
    """Validates that K-Means correctly reshapes pixel tokens back to the 2D spatial map dimensions."""
    # Create a small synthetic 3D hyperspectral cube (height=10, width=10, bands=5)
    synthetic_cube = np.random.rand(10, 10, 5)
    
    # Run segmentation with K=3 clusters
    seg_map = HyperspectralClassifier.run_kmeans_segmentation(synthetic_cube, n_clusters=3, max_iter=10)
    
    # Assertions to prove correctness
    assert isinstance(seg_map, np.ndarray)
    assert seg_map.shape == (10, 10)  # Must match original height and width
    assert np.all(seg_map >= 0) and np.all(seg_map < 3)  # Cluster IDs must be within range