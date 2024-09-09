from PIL import Image
from matplotlib import pyplot as plt

# Load Image
img = Image.open("C:\\Users\\Acer\\Desktop\\Project 15\\lsd.png")

# Rotate image by 45 degrees
rotated_img = img.rotate(45)

# Define crop box
crop_box = (100,100,400,400)

# Crop the rotated image 
cropped_img = rotated_img.crop(crop_box)

# Save the cropped and rotated image 
cropped_img.save("C:\\Users\\Acer\\Desktop\\Project 15\\cropped_lsd.png")

# Display all images side by side
plt.figure(figsize=(20,10))

# Show original image
plt.subplot(1,3,1)
plt.imshow(img)
plt.axis('off')
plt.title("Original Image")

# Show rotated image
plt.subplot(1,3,2)
plt.imshow(rotated_img)
plt.axis('off')
plt.title("Rotated Image by 45 degree")

# Show cropped image
plt.subplot(1,3,3)
plt.imshow(cropped_img)
plt.axis('off')
plt.title("Rotated and Cropped Image")

# Display all images
plt.show()