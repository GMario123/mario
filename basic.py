#print("welcome to python")
#a=2
#b=6
#if (a<b):
 #   print("true")
#x=5
#print(x)
#x='mario'
#print(x)
"""hii"""#mutliline comments
#a=str(3)
#c=int(3)
#x=float(3)
#print(a,c,x)
#x=5
#y='joy'
#print(type(x))
#print(type(y))
"""a=3
A=4
print(A,a)
a,s,d='red','blue','white'
print(a,s,d)
a=s=d="girl"
print(a,s,d)"""
#strings as arrays
a="samritha"
#print (a[4])
#print(a[:3])
#a=('mario shilshi raj is the kindest,smartest and gorgeous girl😎')
#print(len(a))
"""for x in "sam":
    print(x)"""
#tkwinter
import cv2
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from ascii_magic import from_image

def load_image(image_path):
    return cv2.imread(image_path)

def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plot_image_console(image_path):
    output = from_image(image_path, columns=100, mode='@')
    print(output)

def image_size(image):
    height, width = image.shape[:2]
    print(f"Image Width: {width}, Image Height: {height}")

def reduce_image_size(image):
    height, width = image.shape[:2]
    return cv2.resize(image, (width // 2, height // 2))

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

def resize_image(image, x, y):
    return cv2.resize(image, (x, y))

def flip_image(image):
    flip_lr = cv2.flip(image, 1)
    flip_tb = cv2.flip(image, 0)
    return flip_lr, flip_tb

def crop_image(image, x_start, y_start, width, height):
    return image[y_start:y_start+height, x_start:x_start+width]

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def convert_to_black_white(image):
    gray = convert_to_grayscale(image)
    _, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return bw

def apply_blur(image, ksize=(5,5)):
    return cv2.GaussianBlur(image, ksize, 0)

# Main Execution
image_path = "image.jpg"  # Change to your image file
image = load_image(image_path)

# a) Display the image
display_image("Original Image", image)

# b) Plot the image in console window
plot_image_console(image_path)

# c) Display the image size
image_size(image)

# d) Reduce the image size
small_image = reduce_image_size(image)
display_image("Reduced Size Image", small_image)

# e) Rotate the image
rotated_image = rotate_image(image, 145)
display_image("Rotated Image", rotated_image)

# f) Resize the image
resized_image = resize_image(image, 50, 70)
display_image("Resized Image", resized_image)

# g) Flip the image
flipped_lr, flipped_tb = flip_image(image)
display_image("Flipped Left-Right", flipped_lr)
display_image("Flipped Top-Bottom", flipped_tb)

# h) Crop the image
cropped_image = crop_image(image, 50, 50, 100, 100)
display_image("Cropped Image", cropped_image)

# i) Convert to Grayscale and Black & White
gray_image = convert_to_grayscale(image)
bw_image = convert_to_black_white(image)
display_image("Grayscale Image", gray_image)
display_image("Black and White Image", bw_image)

# j) Apply Blur Effect
blurred_image = apply_blur(image)
display_image("Blurred Image", blurred_image)

