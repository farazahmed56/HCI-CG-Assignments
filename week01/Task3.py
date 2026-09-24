import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load image
image = Image.open("sample.jpg").convert("RGB")
img = np.array(image)

# Extract Red, Green and Blue channels
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

# Create Red-only image
red_only = np.zeros_like(img)
red_only[:, :, 0] = red

# Create Green-only image
green_only = np.zeros_like(img)
green_only[:, :, 1] = green

# Create Blue-only image
blue_only = np.zeros_like(img)
blue_only[:, :, 2] = blue

# Print summary
print("--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape :", img.shape)
print("Red Channel 2D Shape :", red.shape, "| Mean Intensity:", round(red.mean(), 2))
print("Green Channel 2D Shape:", green.shape, "| Mean Intensity:", round(green.mean(), 2))
print("Blue Channel 2D Shape :", blue.shape, "| Mean Intensity:", round(blue.mean(), 2))

# Display 2 x 3 layout
plt.figure(figsize=(12, 7))

plt.subplot(2, 3, 1)
plt.imshow(red_only)
plt.title("Red-Only")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(green_only)
plt.title("Green-Only")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blue_only)
plt.title("Blue-Only")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(red, cmap="gray")
plt.title("Red Intensity")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(green, cmap="gray")
plt.title("Green Intensity")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(blue, cmap="gray")
plt.title("Blue Intensity")
plt.axis("off")

plt.tight_layout()
plt.show()