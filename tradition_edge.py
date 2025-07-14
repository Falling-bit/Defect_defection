import cv2
import matplotlib.pyplot as plt

img_path = f"pics\cut1.bmp"
img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5),0)

edges = cv2.Canny(blurred, 50, 150)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilated = cv2.dilate(edges, kernel, iterations=1)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1);plt.title("Original");plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
plt.subplot(1, 3, 2); plt.title("Gray+Blur"); plt.imshow(blurred, cmap='gray')
plt.subplot(1, 3, 3); plt.title("Edges (Canny)"); plt.imshow(dilated, cmap='gray')
plt.tight_layout(); plt.show()