import cv2
import numpy as np

def sharp_image(image):
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(image, 0, sharpen_kernel)
    return sharpen
