import cv2

# 1. Read the original color image
img = cv2.imread('image.jpg')

# 2. Convert from BGR (OpenCV's default color format) to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Alternative shortcut: Read directly as grayscale
# gray_img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# 3. Display the result in a window
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)          # Waits until you press any key
cv2.destroyAllWindows() # Closes the image window

# 4. Save the grayscale image
cv2.imwrite('grayscale_output.jpg', gray_img)