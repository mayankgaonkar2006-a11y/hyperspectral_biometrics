
import numpy as np
from src.pipeline import HyperspectralPipeline
from unittest.mock import patch

@patch("src.loader.HyperspectralLoader.load_cube")
def test_pipeline_execution(mock_load):
    """Test that the pipeline successfully integrates loading and normalization."""
    mock_load.return_value = np.array([[[10.0, 50.0], [30.0, 100.0]]])
    
    result = HyperspectralPipeline.process_file("dummy_path.hdr")
    
    assert result.shape == (1, 2, 2)
    assert np.min(result) == 0.0
    assert np.max(result) == 1.0

