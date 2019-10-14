import cv2
import numpy as np

lena = cv2.imread("/Users/i/Pycharm/opencv-learn/lena512color.tiff", 0)
cv2.imshow("lena", lena)
w, h = lena.shape
draw_array = np.zeros((w, h, 8), dtype=np.uint8)
for i in range(8):
    draw_array[:, :, i] = 2**i
bit_pic = np.zeros(draw_array.shape, dtype=np.uint8)
for i in range(8):
    bit_pic[:, :, i] = cv2.bitwise_and(lena, draw_array[:, :, i])
    mask = bit_pic[:, :, i] > 0
    bit_pic[:, :, i][mask] = 255
    cv2.imshow(str(i), bit_pic[:, :, i])
cv2.waitKey()
cv2.destroyAllWindows()