import cv2

# Read the image
image = cv2.imread("EXP9 Test.jpeg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Write the grayscale image to disk
cv2.imwrite("gray_image.jpg", gray_image)

# Rotate the image
rotated_image = cv2.rotate(gray_image, cv2.ROTATE_90_CLOCKWISE)

# Write the rotated image to disk
cv2.imwrite("rotated_image.jpg", rotated_image)
