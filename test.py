import numpy as np
from pystackreg import StackReg
from skimage import io 

# Load the multi-page TIFF file. 
# This automatically creates a 3D NumPy array (100, Height, Width).
try:
    img_stack = io.imread('C:\\Users\\anupam-chaudhary\\Desktop\\test_chip\G_Chip\\1021_2.2.tif')
except FileNotFoundError:
    print("Error: TIFF file not found. Check the path.")
    # Handle the error, maybe exit or use dummy data for demonstration
    # return 

# Verify the shape: It should be (100, H, W)
print(f"Loaded image stack shape: {img_stack.shape}")