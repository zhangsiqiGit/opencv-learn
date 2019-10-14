import cv2
import numpy as np
# read origin img
lena = cv2.imread("lena512color.tiff", 0)
# read watermark img
watermark = cv2.imread("/Users/i/Pycharm/opencv-learn/watermark.jpg", 0)
# binary convert
w = watermark[:, :] > 0
watermark[w] = 1
w, h = lena.shape
# ===============Insert process=========
draw_array = np.ones((w, h), dtype=np.uint8) * 254
lenaH7 = cv2.bitwise_and(lena, draw_array)
# insert watermark into lenaH7
lena_mark = cv2.bitwise_or(lenaH7, watermark)
# ===============Draw process===========
draw_arr = np.ones((w, h), dtype=np.uint8)
water_mark = cv2.bitwise_and(lena_mark, draw_arr)
mask = water_mark[:, :] > 0
water_mark[mask] = 255
cv2.imshow("lena", lena)
cv2.imshow("watermark", watermark*255)
cv2.imshow("lena_mark", lena_mark)
cv2.imshow("mask", water_mark)
cv2.waitKey()
cv2.destroyAllWindows()
