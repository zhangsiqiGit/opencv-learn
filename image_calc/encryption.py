import cv2
import numpy as np
lena = cv2.imread("/Users/i/Pycharm/opencv-learn/lena512color.tiff", 0)
key = np.random.randint(0, 256, size=list(lena.shape), dtype=np.uint8)
encryption = cv2.bitwise_xor(lena, key)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imshow("encryption", encryption)
cv2.imshow("decrption", decryption)
cv2.waitKey()
cv2.destroyAllWindows()
