import numpy as np
import matplotlib.pyplot as plt

# Create a 300 x 400 x 3 image array filled with zeros
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Top-left: Red
img[0:150, 0:200] = [255, 0, 0]

# Top-right: Green
img[0:150, 200:400] = [0, 255, 0]

# Bottom-left: Blue
img[150:300, 0:200] = [0, 0, 255]

# Bottom-right: White
img[150:300, 200:400] = [255, 255, 255]

# Print array information
print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) :", img.shape)
print("Data Type :", img.dtype)
print("Total Elements :", img.size, "values")
print("Memory Footprint :", img.nbytes, "bytes")

# Display the image
plt.imshow(img)
plt.axis("off")
plt.show()