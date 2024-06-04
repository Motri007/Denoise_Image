import cv2
import numpy as np
from skimage import img_as_ubyte

image_original = cv2.imread("C:\\Users\\Motri\\Documents\\GitHub\\Denoise_Image\\original.jpg")
imageBW = cv2.imread("C:\\Users\\Motri\\Documents\\GitHub\\Denoise_Image\\original.jpg",0)
imageBW = imageBW/255

cv2.imshow("original", image_original)
cv2.imshow("original black white", imageBW)
cv2.waitKey(0)
cv2.destroyAllWindows()


x,y = imageBW.shape
a = np.zeros((x,y) , dtype= np.float32)

# salt and pepper
# nose 10% pepper=0.05
# nose 25% pepper=0.125
# nose 50% pepper=0.25
pepper = 0.05
salt = 1 - pepper

# sakht salt and pepper
for i in range(x):
    for j in range(y):
        rnd=np.random.random()
        if rnd < pepper:
            a[i][j] = 0
        elif rnd > salt:
            a[i][j] = 1
        else:
            a[i][j] = imageBW[i][j]


image_noisy = a
cv2.imshow('image noisy', image_noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ta inja tasvir vo noisy kardim ===========================================

## denoise image
# filter mean (average)
i = 5
j = 5
denoise_mean = cv2.blur(image_noisy, (i,j))

# filter median
image_noisy_median = np.clip(image_noisy, -1, 1) # range pixel
image_noisy_median = img_as_ubyte(image_noisy_median) # convert to uint8
denoise_median = cv2.medianBlur(image_noisy_median, 5)


cv2.imshow('Denoise Filter Mean', denoise_mean)
cv2.imshow('Denoise Filter Median', denoise_median)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save 
save_denoise_mean = "C:\\Users\\Motri\\Documents\\GitHub\\Denoise_Image\\Denoise Filter Mean.jpg"
save_denoise_median = "C:\\Users\\Motri\\Documents\\GitHub\\Denoise_Image\\Denoise Filter Median.jpg"
cv2.imwrite(save_denoise_mean, image_noisy)
cv2.imwrite(save_denoise_median, image_noisy)