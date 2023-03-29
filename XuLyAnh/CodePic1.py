import cv2
import numpy as np


### Lv1:


# Load bức ảnh
img = cv2.imread("room.jpg")

# Tạo các điểm tọa độ
pts = np.array([[280, 651], [304, 651], [298, 672], [265, 672]], np.int32)

# Đưa tọa độ các điểm vào một list (ở đây chỉ có một đường cong nên ta tạo list gồm một phần tử)
pts = [pts]

# Vẽ đường cong
cv2.drawContours(img, pts, 0, (200, 185, 112), 1)

# Tải ảnh background và ảnh overlay
picture = cv2.imread('Goldhourse.jpg')

# Tọa độ vị trí thêm ảnh overlay vào background
x_offset = 245
y_offset = 250

# Lấy chiều cao, chiều rộng và số kênh màu của ảnh overlay
picture_height, picture_width, picture_channels = picture.shape

# Đặt vị trí thêm ảnh overlay trong background
y1, y2 = y_offset, y_offset + picture_height
x1, x2 = x_offset, x_offset + picture_width

# Thêm ảnh overlay vào background
img[y1:y2, x1:x2] = picture

# Tọa độ và nội dung cần vẽ lên ảnh
text = "Bed"
org = (550, 620)
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX       # Font xịn
fontScale = 1
color = (200, 185, 112)
thickness = 1

# Vẽ chữ lên ảnh
cv2.putText(img, text, org, font, fontScale, color, thickness)



# Hiển thị ảnh
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
