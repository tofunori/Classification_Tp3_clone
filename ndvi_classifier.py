#!/usr/bin/env python3
"""
NDVI Classification Script

This script performs K-means clustering on satellite imagery using NDVI values.
It loads a multi-band TIF file, extracts the NDVI band, and applies K-means clustering
to classify the image based on NDVI values.

Usage:
    python ndvi_classifier.py --input <input_tif> --output <output_tif> --clusters <num_clusters>

Arguments:
    --input: Path to the input TIF file
    --output: Path to save the output classification TIF file
    --clusters: Number of clusters for K-means (default: 5)
    --ndvi_band: Index of the NDVI band in the TIF file (default: 13)
    --display: Display the classification results (default: False)
"""

import os
import argparse
import numpy as np
import rasterio
from rasterio.plot import show
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='NDVI Classification Script')
    parser.add_argument('--input', '-i', required=True, help='Input TIF file')
    parser.add_argument('--output', '-o', required=True, help='Output TIF file')
    parser.add_argument('--clusters', '-c', type=int, default=5, help='Number of clusters for K-means')
    parser.add_argument('--ndvi_band', '-n', type=int, default=13, help='Index of the NDVI band in the TIF file')
    parser.add_argument('--display', '-d', action='store_true', help='Display the classification results')
    return parser.parse_args()


def display_image_info(src):
    """Display image information."""
    print(f"Informations sur l'image {os.path.basename(src.name)}:")
    print(f"Dimensions: {src.width} x {src.height} pixels")
    print(f"Nombre total de bandes: {src.count}")
    print(f"Type de données: {src.dtypes[0]}")
    if src.crs:
        print(f"Système de coordonnées: {src.crs.to_string()}")

    print("\nBandes disponibles:")
    for i in range(1, src.count + 1):
        desc = src.descriptions[i-1] if src.descriptions and i-1 < len(src.descriptions) else "Non spécifiée"
        print(f"  Bande {i}: {desc}")


def perform_kmeans_clustering(ndvi_data, n_clusters):
    """Perform K-means clustering on NDVI data."""
    # Reshape data for clustering
    data_for_clustering = ndvi_data.reshape(-1, 1)
    
    # Remove invalid values (NaN, Infinity)
    valid_mask = np.isfinite(data_for_clustering).all(axis=1)
    valid_data = data_for_clustering[valid_mask]
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(valid_data)
    
    # Create classification map
    classification = np.zeros(data_for_clustering.shape[0], dtype=np.int16)
    classification[valid_mask] = kmeans.predict(valid_data) + 1  # Start labels from 1 instead of 0
    
    # Reshape back to original dimensions
    classification_map = classification.reshape(ndvi_data.shape)
    
    return classification_map, kmeans.cluster_centers_


def main():
    """Main function."""
    args = parse_args()
    
    # Open the input file
    with rasterio.open(args.input) as src:
        # Display image information
        display_image_info(src)
        
        # Read NDVI band
        ndvi_band_index = args.ndvi_band
        if ndvi_band_index > src.count:
            print(f"Error: NDVI band index {ndvi_band_index} exceeds the number of bands {src.count}")
            return
        
        ndvi_data = src.read(ndvi_band_index)
        
        # Perform K-means clustering
        classification_map, cluster_centers = perform_kmeans_clustering(ndvi_data, args.clusters)
        
        # Write the classification map to a new raster file
        profile = src.profile.copy()
        profile.update({
            'dtype': rasterio.int16,
            'count': 1,
            'nodata': 0
        })
        
        with rasterio.open(args.output, 'w', **profile) as dst:
            dst.write(classification_map.astype(rasterio.int16), 1)
            # Update band description
            dst.set_band_description(1, f"NDVI K-means classification ({args.clusters} clusters)")
        
        # Print cluster centers information
        flat_centers = cluster_centers.flatten()
        sorted_indices = np.argsort(flat_centers)
        
        print("\nCluster centers (NDVI values):")
        for i, idx in enumerate(sorted_indices):
            print(f"  Class {i+1}: {flat_centers[idx]:.4f}")
        
        # Display results if requested
        if args.display:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
            
            # Display NDVI
            img1 = ax1.imshow(ndvi_data, cmap='RdYlGn')
            ax1.set_title("NDVI")
            plt.colorbar(img1, ax=ax1, shrink=0.5)
            
            # Display classification
            img2 = ax2.imshow(classification_map, cmap='viridis')
            ax2.set_title(f"K-means Classification ({args.clusters} clusters)")
            plt.colorbar(img2, ax=ax2, shrink=0.5)
            
            plt.tight_layout()
            plt.show()
    
    print(f"\nClassification saved to: {args.output}")


if __name__ == "__main__":
    main()
