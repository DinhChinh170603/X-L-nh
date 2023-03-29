import cv2
import numpy as np
import random

###Lv3:


# Đọc bức ảnh
img = cv2.imread('room.jpg')


# Chuyển đổi sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc Gaussian để giảm nhiễu
blur = cv2.GaussianBlur(gray, (3,3), 0)

# Sử dụng Canny Edge Detection để tìm biên ảnh
edges = cv2.Canny(blur, 50, 150)

# Tìm các đường viền của vật thể
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tìm contour có diện tích lớn nhất
# max_area = 0
# best_cnt = None
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     if area > max_area:
#         max_area = area
#         best_cnt = cnt

#chosen_cnt = contours[random.randint(0, len(contours) - 1)]

# Tìm contour có diện tích mong muốn
chosen_cnt = None
while chosen_cnt is None:
    # Chọn một contour ngẫu nhiên từ danh sách contours
    contour_idx = random.randint(0, len(contours)-1)
    # Lấy diện tích của contour được chọn
    area = cv2.contourArea(contours[contour_idx])
    # Nếu diện tích lớn hơn hoặc bằng k pixel, gán contour này cho chosen
    if area > 200 and area < 300:
        chosen_cnt = contours[contour_idx]


#Tô random
cv2.drawContours(img, [chosen_cnt], -1, (0, 200, 155), -1)

# Tạo mask
mask = cv2.rectangle(np.zeros_like(img), (450, 255), (560, 355), (255, 255, 255), -1)

# Sao chép ảnh gốc để tránh thay đổi ảnh gốc
noisy_img = img.copy()

# Làm nhiễu vùng trong noisy_img
noisy_img[mask == 255] = cv2.randn(noisy_img[mask == 255], 0, 25)

# Hiển thị ảnh gốc và ảnh bị làm nhiễu
alpha = 0.5
beta = 1.0 - alpha
overlay = noisy_img.copy()
cv2.rectangle(overlay, (450, 255), (560, 355), (0, 0, 0), 2)
last = cv2.addWeighted(img, alpha, overlay, beta, 0)

# Hiển thị ảnh
cv2.imshow('object', last)
cv2.waitKey(0)
cv2.destroyAllWindows()