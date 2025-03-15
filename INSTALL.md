# Installation Instructions

This document provides instructions for setting up the environment needed to run the NDVI classification notebook and scripts in this repository.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation Steps

### 1. Clone or Download the Repository

```bash
git clone https://github.com/tofunori/Classification_Tp3_clone.git
cd Classification_Tp3_clone
```

Or download and extract the ZIP file from GitHub.

### 2. Create a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS and Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install numpy matplotlib rasterio scikit-learn jupyter
```

#### Common Issues with Rasterio Installation

Rasterio can sometimes be challenging to install due to its dependencies on GDAL. If you encounter issues:

**Windows Users:**
- Consider using pre-built wheels from Christoph Gohlke's website: https://www.lfd.uci.edu/~gohlke/pythonlibs/
- Download the appropriate rasterio and GDAL wheels for your Python version and architecture.
- Install them with pip:
  ```bash
  pip install path/to/downloaded/GDAL-wheel.whl
  pip install path/to/downloaded/rasterio-wheel.whl
  ```

**macOS Users:**
- Install GDAL first using Homebrew:
  ```bash
  brew install gdal
  pip install rasterio
  ```

**Linux Users:**
- Install GDAL development libraries:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install libgdal-dev
  pip install rasterio
  
  # Fedora/RHEL/CentOS
  sudo dnf install gdal-devel
  pip install rasterio
  ```

### 4. Running the Jupyter Notebook

```bash
jupyter notebook
```

Navigate to and open `NDVI_Classification.ipynb` in the Jupyter interface.

### 5. Running the Python Script

The repository includes a standalone Python script that can be run from the command line:

```bash
python ndvi_classifier.py --input /path/to/your/image.tif --output /path/to/save/classification.tif --clusters 5 --display
```

For help with the script's options:

```bash
python ndvi_classifier.py --help
```

## Test Data

The code expects a multi-band TIF file with an NDVI band (by default, it looks for the NDVI band at index 13).

If you don't have such data, consider:
- Using Sentinel-2 data, which can be downloaded from [Copernicus Open Access Hub](https://scihub.copernicus.eu/)
- Using sample data from resources like [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/catalog/sentinel-2)
- Creating a derived NDVI band from Red and NIR bands using tools like QGIS or GDAL

## Troubleshooting

If you encounter issues:
1. Ensure all dependencies are correctly installed
2. Check that your input TIF file has the expected bands
3. If using the script, try adjusting the `--ndvi_band` parameter to match your data
4. For rasterio-specific issues, consult the [rasterio documentation](https://rasterio.readthedocs.io/)