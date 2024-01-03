"""For the image given below (provided with the lab handout), apply the connected 
component labelling and count the total number of white objects. First threshold the 
images and then do connected component analysis. You can use the following code"""

import cv2
import numpy as np
# Load the image
image = cv2.imread('EXP10 Test.png', 0)  # Replace 'image.jpg' with the actual image file path

# Threshold the image
_, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Apply connected component analysis
num_labels, labels = cv2.connectedComponents(thresholded)

# Count the total number of white objects (excluding the background)
num_objects = num_labels - 1

print("Total number of white objects:", num_objects)
# Label the white objects in the image
colored_labels = cv2.applyColorMap(labels.astype(np.uint8), cv2.COLORMAP_JET)

# Save the labeled image to disk
cv2.imwrite("labeled_image.jpg", colored_labels)
