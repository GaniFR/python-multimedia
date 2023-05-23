import cv2
import os
import numpy as np

from pynput.keyboard import Key, Listener

# Image path, change accordingly 
image_path = r'E:\Teknik Informatika\Semester 6\Sistem Multimedia\ImageUTS\img\bf.jpg'
  
# Image directory, where image will be saved
directory = r'E:\Teknik Informatika\Semester 6\Sistem Multimedia\ImageUTS\img'

img = cv2.imread(image_path, -1)
# -1 = color, 0 = grayscale, 1 = unchanged

print('-------------------------')
try:
    modifier = float(input('* Edit your image? (yes=1): '))
except ValueError:
    print('Error, not a number')

#Editing Image
if (modifier == 1):
    selection = float(input('* Combine the modification or separate it? (1=combine or 2=seperate): '))

    #Combined modif
    if (selection==1):
        #Resize Image
        img_sz = float(input('* Enter size value (ex: 0.4 or 1): '))
        new_img = cv2.resize(img, (0,0), fx=img_sz, fy=img_sz)

        #Adding text
        text = (input('* Enter text (press enter to skip): '))
        cv2.putText(new_img,text,(100,200), cv2.FONT_HERSHEY_COMPLEX, 3,(255,255,255),2,cv2.LINE_AA)      

        kernel = np.ones((5,5),np.uint8)
        final = cv2.morphologyEx(new_img, cv2.MORPH_OPEN, kernel)

        #Naming image
        filename = (input('* Enter filename: '))
        print('-------------------------')

        cv2.imshow('Before', img)
        cv2.imshow('After', final)
        
        os.chdir(directory)
        cv2.imwrite("edited_"+filename+".jpg", final)

    #Separate modif
    elif (selection==2):
        #Resize Image
        img_sz = float(input('* Enter size value (ex: 0.4 or 1): '))
        resize = cv2.resize(img, (0,0), fx=img_sz, fy=img_sz)

        #Morph open image
        kernel = np.ones((5,5),np.uint8)
        morph = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        #Adding text
        text = (input('* Enter text (press enter to skip): '))
        texted = cv2.putText(img,text,(100,200), cv2.FONT_HERSHEY_COMPLEX, 3,(255,255,255),2,cv2.LINE_AA)           

        #Naming image
        filename = (input('* Enter filename: '))
        print('-------------------------')

        cv2.imshow('Resize', resize)
        cv2.imshow('Adding Text', texted)
        cv2.imshow('Morph Open', morph)
        
        os.chdir(directory)
        cv2.imwrite("resize_"+filename+".jpg", resize)
        cv2.imwrite("text_"+filename+".jpg", texted)
        cv2.imwrite("morphopen_"+filename+".jpg", morph)

#No edit
else:
    cv2.imshow('Original', img)

cv2.waitKey(0) # 0 = duration in second
cv2.destroyAllWindows()