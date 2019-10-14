import cv2
import numpy as np
# read origin img
lena = cv2.imread("/Users/i/Pycharm/opencv-learn/lena512color.tiff", 0)
w, h = lena.shape
mask = np.zeros((w, h), dtype=np.uint8)
mask[220:400, 250:350] = 1
front_mask = mask * 255
back_mask = (1-mask) * 255

key = np.random.randint(0, 256, size=[w, h], dtype=np.uint8)
# ==================captcha face image=========
lenaXorKey = cv2.bitwise_xor(lena, key)
encryptFace = cv2.bitwise_and(lenaXorKey, front_mask)
lenaBackEnd = cv2.bitwise_and(lena, back_mask)
maskFace = encryptFace + lenaBackEnd
# ==================decaptcha face image=======
extractOriginal = cv2.bitwise_xor(maskFace, key)
extractFace = cv2.bitwise_and(extractOriginal, front_mask)
decaptcha_img = lenaBackEnd + extractFace
cv2.imshow("lena", lena)
cv2.imshow("key", key)
cv2.imshow("encryption", lenaXorKey)
cv2.imshow("encrypFace", maskFace)
cv2.imshow("decryptFace", decaptcha_img)
cv2.waitKey()
cv2.destroyAllWindows()