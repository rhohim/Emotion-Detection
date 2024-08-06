import cv2
img = cv2.imread('G:/CrevHim/Code/software/Emotion-detection-main/user.3.20.jpg',cv2.IMREAD_UNCHANGED)

cv2.putText(img, "rohim"[::-1], (30,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255),2,cv2.LINE_AA)
# img =cv2.flip(img,1)
#cv2.putText(img, "Bebed", (30,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)