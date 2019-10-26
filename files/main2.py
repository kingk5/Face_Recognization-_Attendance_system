    import cv2
import face_recog_func as ff
import pandas as pd
import os
import shutil
import database as db

persons = {0:'Prince Khatri',1:'Pratiksha Dubey',2:'Prince'}

def recognize():
    #take the image
    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("test")
    
    img_counter = 0
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "img{}.png".format(img_counter)
            
            
            face_detected,gray_img = ff.face_detection(frame)
            #for face in faces:
             #   (x,y,w,h) = face
              #  frame = frame[y:y+h,x:x+w]
            
            
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            
            
            faces, faceID = ff.datapreprocessing()
            
            #faces1 = ff.test_img_preprocessing(img_name)
           
            
            #face_recogniser = ff.model_train(faces, faceID)
            #face_recogniser.save('trainningData.yml')
            face_recogniser = cv2.face.LBPHFaceRecognizer_create();
            face_recogniser.read('trainningData.yml');
            for face in face_detected:
                (x,y,w,h) = face
                roi_gray = gray_img[y:y+h,x:x+w]
                label,confidence = face_recogniser.predict(roi_gray)
                name= persons[label]
                print("label")
                print(label)
                print(name)
                print(confidence)
                namelist = name.split()
                first = namelist[0]
                last = namelist[-1]
                
                #db.attendance(first, last)
            
            #for i in label:
             #   label = i
           
            try: 
                os.remove(img_name)
            except: pass
            break
    cam.release()
    cv2.destroyAllWindows()
        
def register(entry):
    name= entry
    print(name)
    folders = 0
    for _, dirnames, filenames in os.walk('H:/work/opencv/another/Training'):
        folders += len(dirnames)
    persons[folders] = name
    print("take 100 images")
    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("test")
    
    img_counter = 0
    
    root = 'H:/work/opencv/another/Training/'
    root += str(folders);
    print(root)
    os.mkdir(root)
       # i = i+1
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            if img_counter <= 30:
                del persons[folders]
                #os.rmdir(root)
                shutil.rmtree(root)
            break
        else:
            # SPACE pressed
            img_name = "img{}.png".format(img_counter)
            img_location = root + '/' + img_name
            faces,_ = ff.face_detection(frame)
            for face in faces:
                (x,y,w,h) = face
                frame = frame[y:y+h,x:x+w]
            cv2.imwrite(img_location, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        if img_counter >= 100:
            break
    
    cam.release()
    
    cv2.destroyAllWindows()
    faces, faceID = ff.datapreprocessing()
    face_recogniser = ff.model_train(faces, faceID)
    face_recogniser.write('trainningData.yml')