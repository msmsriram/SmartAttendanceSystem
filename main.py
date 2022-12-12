import cv2
import numpy as np
import face_recognition

#import the images from the directory
#converting the images BGR into RGB
# imgElon = face_recognition.load_image_file('imagebasic/Elon Musk.jpg')
# imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgsurya = face_recognition.load_image_file('attendence/suriya.jpg')
imgsurya = cv2.cvtColor(imgsurya,cv2.COLOR_BGR2RGB)


# imgtest = face_recognition.load_image_file('imagebasic/Bill gates.jpg')
# imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

imgtest = face_recognition.load_image_file('attendence/Vijay.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

# faceloc = face_recognition.face_locations(imgElon)[0]
# encodeElon =face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

faceloc = face_recognition.face_locations(imgsurya)[0]
encodesurya = face_recognition.face_encodings(imgsurya)[0]
cv2.rectangle(imgsurya,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

# facelocTest = face_recognition.face_locations(imgtest)[0]
# encodetest =face_recognition.face_encodings(imgtest)[0]
# cv2.rectangle(imgtest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)

facelocTest = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)


# results = face_recognition.compare_faces([encodeElon],encodetest)
# facedis = face_recognition.face_distance([encodeElon],encodetest)
# print(results,facedis)

results = face_recognition.compare_faces([encodesurya],encodetest)
facedis = face_recognition.face_distance([encodesurya],encodesurya)
print(results,facedis)

# cv2.putText(imgtest,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.putText(imgtest,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


#opencv
# cv2.imshow('Elon Musk',imgElon)
# cv2.imshow('Elon test',imgtest)
# cv2.waitKey(0)

cv2.imshow('suriya',imgsurya)
cv2.imshow('Vijay',imgtest)
cv2.waitKey(0)



cv2.waitKey(0)
