import numpy as np
import cv2
import math

val = input("Enter the watermark: ") 
#Read Image
gray=cv2.imread('boat.png',cv2.IMREAD_GRAYSCALE)
gray1=gray.copy()
#display image
cv2.imshow('Original Image',gray)

#Binary conversion of watermark
res=[]
for c in val:
    ascii_val = ord(c) 
    binary_val = bin(ascii_val)
    res.append(binary_val[2:]) 
n=len(res)
#Addition of watermark to image
for i in range(0,n):
    for j in range(0,7):
        if gray[i,j]%2==0 and res[i][j]=='1':
            gray[i,j]=gray[i,j]+1
        elif gray[i,j]%2!=0 and res[i][j]=='0':
            gray[i,j]=gray[i,j]-1
#Display watermarked Image       
cv2.imshow('Watermarked Image',gray) 

#Retrieval of watermark from the watermarked Image.
str=''
for i in range(0,n):
    t=''
    for j in range(0,7):
        z=bin(gray[i,j])
        t=t+(z[len(z)-1])
        
    str=str+chr(int(t,2))
#Printing Watermark   
print("Retrieved watermark:",str)

#Addition of random gaussian Noise to image
gauss = np.random.normal(0,1,gray.size)
gauss = gauss.reshape(gray.shape[0],gray.shape[1]).astype('uint8')
img_gauss = cv2.add(gray,gauss)
cv2.imshow('Noise Image',img_gauss)

#Calculation of PSNR value
error=np.mean((gray1-img_gauss)**2)
psnr=10*math.log10((255*255)/error)
print("PSNR value:",psnr)

cv2.waitKey(0)
cv2.destroyAllWindows()
