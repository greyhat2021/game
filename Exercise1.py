import cv2
import numpy as np
import matplotlib.pyplot as plt
def create_rectangle_image():
 img = np.ones((400, 600, 3), dtype=np.uint8) * 255
 start_point = (100, 100)
 end_point = (500, 300)
 color = (0, 255, 0)
 thickness = -1
 img = cv2.rectangle(img, start_point, end_point, color, thickness)
 return img
def translate_image(image, tx, ty):
 rows, cols = image.shape[:2]
 M = np.float32([[1, 0, tx], [0, 1, ty]])
 translated = cv2.warpAffine(image, M, (cols, rows))
 return translated
def scale_image(image, sx, sy):
 rows, cols = image.shape[:2]
 M = np.float32([[sx, 0, 0], [0, sy, 0]])
 scaled = cv2.warpAffine(image, M, (int(cols * sx), int(rows * sy)))
 return scaled
def zoom_image(image, zoom_factor):
 rows, cols = image.shape[:2]
 M = np.float32([[zoom_factor, 0, 0], [0, zoom_factor, 0]])
 zoomed = cv2.warpAffine(image, M, (int(cols * zoom_factor), int(rows * zoom_factor)))
 return zoomed
def rotate_image(image, angle):
 rows, cols = image.shape[:2]
 center = (cols / 2, rows / 2)
 M = cv2.getRotationMatrix2D(center, angle, 1.0)
 rotated = cv2.warpAffine(image, M, (cols, rows))
 return rotated
def transform_image(image, tx, ty, sx, sy, angle):
 translated = translate_image(image, tx, ty)
 scaled = scale_image(translated, sx, sy)
 rotated = rotate_image(scaled, angle)
 return rotated
input_image = create_rectangle_image()
translation_x = 50
translation_y = 30
scaling_x = 1.2
scaling_y = 1.2
zoom_factor = 1.5
rotation_angle = 45
translated_image = translate_image(input_image, translation_x, translation_y)
scaled_image = scale_image(translated_image, scaling_x, scaling_y)
zoomed_image = zoom_image(input_image, zoom_factor)
rotated_image = rotate_image(input_image, rotation_angle)
transformed_image = transform_image(input_image, translation_x, translation_y, scaling_x, scaling_y, rotation_angle)
def display_image(title, img):
 plt.figure(figsize=(8, 6))
 plt.title(title)
 plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
 plt.axis('off')
 plt.show()
display_image('Original Image', input_image)
display_image('Translated Image', translated_image)
display_image('Scaled Image', scaled_image)
display_image('Zoomed Image', zoomed_image)
display_image('Rotated Image', rotated_image)
display_image('Transformed Image', transformed_image)
