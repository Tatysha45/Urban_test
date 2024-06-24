import cv2
import numpy as np

image = np.zeros((500,500, 3), dtype=np.uint8)

cv2.circle(image, (250, 250), 230, (255, 255, 255), thickness=5)


cv2.line(image, (100, 150), (200, 150), (0, 0, 255), thickness=5)
cv2.line(image, (300, 150), (400, 150), (0, 0, 255), thickness=5)
cv2.line(image, (100, 150), (100, 320), (255, 0, 0), thickness=5)
cv2.line(image, (200, 150), (200, 320), (255, 0, 0), thickness=5)
cv2.line(image, (300, 150), (300, 320), (255, 0, 0), thickness=5)
cv2.line(image, (400, 150), (400, 320), (255, 0, 0), thickness=5)
cv2.ellipse(image, (250, 320), (150, 150), 0, 180, 0, (0, 255, 0), thickness=5)
cv2.ellipse(image, (250, 320), (50, 50), 0, 180, 0, (0, 255, 0), thickness=5)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


def add_gradient_background(image1, start_color, end_color):
    height, width, _ = image1.shape
    gradient = np.linspace(start_color, end_color, height)
    for i in range(height):
        for j in range(width):
            image[i, j] = tuple(np.clip(gradient[i], 0, 255).astype(int))


add_gradient_background(image, (255, 0, 0), (0, 0, 255))

cv2.circle(image, (250, 250), 230, (255, 255, 255), thickness=5)

cv2.line(image, (100, 150), (200, 150), (0, 0, 255), thickness=5)
cv2.line(image, (300, 150), (400, 150), (0, 0, 255), thickness=5)
cv2.line(image, (100, 150), (100, 320), (255, 0, 0), thickness=5)
cv2.line(image, (200, 150), (200, 320), (255, 0, 0), thickness=5)
cv2.line(image, (300, 150), (300, 320), (255, 0, 0), thickness=5)
cv2.line(image, (400, 150), (400, 320), (255, 0, 0), thickness=5)
cv2.ellipse(image, (250, 320), (150, 150), 0, 180, 0, (0, 255, 0), thickness=5)
cv2.ellipse(image, (250, 320), (50, 50), 0, 180, 0, (0, 255, 0), thickness=5)

cv2.imshow('Logo with Gradient Background', image)
cv2.waitKey(0)
cv2.destroyAllWindows()