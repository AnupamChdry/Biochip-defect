import numpy as np
from pystackreg import StackReg
from skimage import io 
import os 

# --- CONFIGURATION ---
input_path = 'C:\\Users\\anupam-chaudhary\\Desktop\\test_chip\\G_Chip\\1021_2.2.tif'
# Choose your desired reference mode: 'first', 'median', or 'mean'
# 'first' is often best for standardizing to a specific ideal chip orientation.
reference_mode = 'first' 
transformation_type = StackReg.RIGID_BODY # Corrects for rotation and translation
# ---------------------

try:
    # 1. Load the multi-page TIFF file.
    img_stack = io.imread(input_path)
    
    # Define output paths
    base_dir = os.path.dirname(input_path)
    output_filename = f'1021_2.2_aligned_{reference_mode}.tif'
    output_path = os.path.join(base_dir, output_filename)

except FileNotFoundError:
    print(f"❌ Error: TIFF file not found at {input_path}. Please check the path.")
    exit() 

# 2. Verify the shape (Should be around 100 images)
print(f"Loaded image stack shape: {img_stack.shape}")
num_images = img_stack.shape[0]
print(f"Found {num_images} images in the stack.")
print("-" * 30)

## 3. Initialize and Perform Registration

# Initialize StackReg with the chosen transformation type
sr = StackReg(transformation_type)

print(f"Aligning {num_images} images to the '{reference_mode}' image using RIGID_BODY transformation...")

# This step calculates the transformation matrix for each image (i > 0) 
# and applies it to align it to the specified reference image (i = reference).
corrected_stack = sr.register_stack(img_stack, reference=reference_mode)

print("✅ Registration complete.")
print("-" * 30)

## 4. Save the Corrected Stack

try:
    # Save the resulting 3D NumPy array back into a multi-page TIFF file.
    # We use .astype(img_stack.dtype) to maintain the original image data type (e.g., uint16).
    io.imsave(output_path, corrected_stack.astype(img_stack.dtype), plugin='tifffile', check_contrast=False)
    print(f"💾 Successfully saved the aligned stack to: {output_path}")

except Exception as e:
    print(f"❌ Error saving the output file: {e}")