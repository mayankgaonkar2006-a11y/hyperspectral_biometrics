import pytest
from src.loader import HyperspectralLoader

def test_loader_file_not_found():
    """Test that HyperspectralLoader raises FileNotFoundError for a non-existent file."""
    loader = HyperspectralLoader("non_existent_file.hdr")
    with pytest.raises(FileNotFoundError):
        loader.load_cube()
