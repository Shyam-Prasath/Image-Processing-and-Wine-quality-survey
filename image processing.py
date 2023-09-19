import cv2
import numpy as np

# Load an image from file with the correct file path
image = cv2.imread("C:\\Users\\SHYAM PRASATH\\Desktop\\home.png")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Define the lower and upper bounds for the color you want to segment (e.g., blue)
lower_bound = np.array([90, 50, 50])  # Lower bound for blue color in HSV
upper_bound = np.array([130, 255, 255])  # Upper bound for blue color in HSV

# Convert the original image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a mask to extract the specified color range
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

# Apply the mask to the original image to extract the color of interest
color_segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image, grayscale image, blurred image, and color segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Color Segmented Image', color_segmented_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
