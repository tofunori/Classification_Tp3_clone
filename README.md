# Classification_Tp3

This repository contains a Jupyter notebook for performing NDVI (Normalized Difference Vegetation Index) classification on satellite imagery. The notebook is part of TP3 (Travail Pratique 3) for a remote sensing course.

## Contents

- `NDVI_Classification.ipynb`: Jupyter notebook containing Python code for analyzing and classifying satellite imagery using NDVI values.

## Technical Details

The notebook uses the following libraries:
- numpy
- rasterio
- sklearn (for KMeans clustering)
- matplotlib

The analysis is performed on a multi-band TIF file with 18 bands, including various Sentinel-2 bands and derived products like NDVI.

## Usage

1. Clone this repository
2. Install the required dependencies (numpy, rasterio, sklearn, matplotlib)
3. Open the Jupyter notebook and modify the input file path to point to your TIF file
4. Run the notebook cells to perform NDVI classification on your data

## Note

This is a clone of the original repository by tofunori.