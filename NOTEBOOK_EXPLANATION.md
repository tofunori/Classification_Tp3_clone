# NDVI Classification Notebook Explanation

This document provides a detailed explanation of the `NDVI_Classification.ipynb` notebook in this repository.

## Overview

The notebook performs image classification on satellite imagery (specifically, a Sentinel-2 image) with a focus on using the NDVI (Normalized Difference Vegetation Index) band for classifying vegetation and land cover types.

## Data Used

The input data is a multi-band TIF file with 18 bands:
- Bands 1-9: Various Sentinel-2 spectral bands (B02 through B12)
- Bands 10-11: Atmospheric data (AOT and WVP)
- Band 12: Scene Classification Layer (SCL)
- Band 13: NDVI (Normalized Difference Vegetation Index)
- Bands 14-18: Various unsupervised classification results

## Process

The notebook follows these steps:

1. **Data Loading and Visualization**: 
   - Loads the multi-band TIF file using rasterio
   - Explores the image properties (dimensions, coordinate system, band information)
   - Visualizes individual bands

2. **NDVI Analysis**:
   - Focuses on the NDVI band (band 13)
   - Performs histogram analysis of NDVI values
   - Visualizes the NDVI distribution

3. **Classification**:
   - Uses K-means clustering to classify the image based on NDVI values
   - Tests different numbers of clusters
   - Visualizes the classification results

4. **Result Analysis**:
   - Compares classification results
   - Analyzes the spectral signatures of different classes
   - Evaluates classification quality

## Technical Implementation

The notebook uses:
- rasterio for reading and manipulating geospatial raster data
- numpy for array operations
- sklearn.cluster.KMeans for unsupervised classification
- matplotlib for visualization

## Practical Applications

This type of analysis is useful for:
- Land cover classification
- Vegetation health monitoring
- Agricultural applications
- Environmental change detection
- Urban/rural area delineation