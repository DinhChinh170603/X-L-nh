import cv2
import numpy as np

### Lv2:

# Load ảnh
img = cv2.imread('room.jpg')

# Vùng tọa độ xử lý
x1, y1 = 450, 250
x2, y2 = 560, 360
x3, y3 = 43, 448
x4, y4 = 70, 493
x5, y5 = 279, 531
x6, y6 = 294, 553


roi1 = img[y1:y2, x1:x2]
roi2 = img[y3:y4, x3:x4]
roi3 = img[y5:y6, x5:x6]

# Góc xoay(nếu dùng)
angle = 90

# Lấy kích thước ảnh
rows1, cols1, _ = roi1.shape
rows2, cols2, _ = roi2.shape
rows3, cols3, _ = roi3.shape

# Define the rotation matrix
M = cv2.getRotationMatrix2D((cols1/2,rows1/2), angle, 1)
N = cv2.getRotationMatrix2D((cols2/2,rows2/2), angle, 0)
P = cv2.getRotationMatrix2D((cols3/2,rows3/2), angle, 0)

# Apply the rotation to the region of interest
rotated_roi1 = cv2.warpAffine(roi1, M, (cols1, rows1))
rotated_roi2 = cv2.warpAffine(roi2, N, (cols2, rows2))
rotated_roi3 = cv2.warpAffine(roi3, P, (cols3, rows3))

# Replace the original region of interest with the rotated region
img[y1:y2, x1:x2] = rotated_roi1
img[y3:y4, x3:x4] = rotated_roi2
img[y5:y6, x5:x6] = rotated_roi3

# Hiển thị ảnh
cv2.imshow('Rotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()