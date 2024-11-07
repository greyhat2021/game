import cv2
import numpy as np

image_path = 'virat.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image at {image_path}")
else:
    def translate(image, x, y):
        rows, cols = image.shape[:2]
        translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
        translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
        return translated_image

    def scale(image, fx, fy):
        scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
        return scaled_image

    def zoom(image, zoom_factor):
        centerX, centerY = image.shape[1] // 2, image.shape[0] // 2
        radiusX, radiusY = int(centerX / zoom_factor), int(centerY / zoom_factor)

        cropped_image = image[centerY - radiusY:centerY + radiusY, centerX - radiusX:centerX + radiusX]
        zoomed_image = cv2.resize(cropped_image, (image.shape[1], image.shape[0]))
        return zoomed_image

    def rotate(image, angle):
        rows, cols = image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
        return rotated_image

    translated = translate(image, 100, 50)
    scaled = scale(image, 1.5, 1.5)
    zoomed = zoom(image, 1.5)
    rotated = rotate(image, 45)

    cv2.imshow("Original", image)
    cv2.imshow("Translated", translated)
    cv2.imshow("Scaled", scaled)
    cv2.imshow("Zoomed", zoomed)
    cv2.imshow("Rotated", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()