import streamlit as st
import numpy as np
from src.classification import HyperspectralClassifier

st.set_page_config(page_title="Hyperspectral Biometrics & Segmentation", layout="centered")
st.title("Hyperspectral Material & Biometric Analysis")

st.sidebar.header("Model Parameters")
n_clusters = st.sidebar.slider("Number of Material Clusters (K)", min_value=2, max_value=12, value=7)
max_iter = st.sidebar.slider("Max Iterations", min_value=10, max_value=100, value=30)

st.write("### 1. Data Input")
use_sample = st.checkbox("Use Synthetic Demo Cube", value=False)

if use_sample:
    np.random.seed(42)
    cube = np.random.rand(100, 100, 15)
    cube[20:50, 20:50, :] += 1.5
    cube[60:85, 50:90, :] += 3.0
else:
    hdr_path = st.text_input("Path to .hdr file", "data/Seurat_BEFORE.hdr")
    img_path = st.text_input("Path to .img file", "data/Seurat_BEFORE.img")

if st.button("Run Hyperspectral Segmentation"):
    with st.spinner("Processing spectral bands (this takes ~10-20 seconds on the 413MB cube)..."):
        if not use_sample:
            cube = HyperspectralClassifier.load_cube(hdr_path, img_path)
        
        seg_map = HyperspectralClassifier.run_kmeans_segmentation(cube, n_clusters=n_clusters, max_iter=max_iter)
        HyperspectralClassifier.save_visual_map(seg_map, "output_segmentation.png")
        
        st.success("Classification Complete!")
        st.image("output_segmentation.png", caption="Segmented Spatial Map", use_container_width=True)