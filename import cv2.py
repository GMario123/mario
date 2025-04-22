"""from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image_path = "image.jpg"  # Change this to your image path
img = Image.open(image_path)

# a) Display the image
img.show()

# b) Plot the image in console window
plt.imshow(img)
plt.axis("off")
plt.show()

# c) Display the image size (width and height)
width, height = img.size
print(f"Original Image Size: Width={width}, Height={height}")

# d) Reduce the Image size to its half
img_half = img.resize((width // 2, height // 2))
img_half.show()
print(f"Half Image Size: Width={width // 2}, Height={height // 2}")

# e) Rotate the image 145 degrees
img_rotated = img.rotate(145, expand=True)
img_rotated.show()

# f) Resize the image with 50 units in x and 70 units in y direction
img_resized = img.resize((width + 50, height + 70))
img_resized.show()
print(f"Resized Image Size: Width={width + 50}, Height={height + 70}")

# g) Flip the image (Left to Right, Top to Bottom)
img_flip_lr = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flip_tb = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flip_lr.show()
img_flip_tb.show()

# h) Crop the image (cropping to center portion)
crop_box = (50, 50, width - 50, height - 50)  # Adjust cropping box
img_cropped = img.crop(crop_box)
img_cropped.show()
print(f"Cropped Image Size: Width={crop_box[2] - crop_box[0]}, Height={crop_box[3] - crop_box[1]}")

# i) Convert the image to GrayScale and Black & White
gray_img = img.convert("L")
bw_img = img.convert("1")
gray_img.show()
bw_img.show()

# j) Apply blur effect on the image
img_blur = img.filter(ImageFilter.BLUR)
img_blur.show()

print("Image processing operations completed successfully!")"""
pip install pillow matplotlib numpy opencv-python


