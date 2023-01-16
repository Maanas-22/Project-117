import os
import cv2
path="C:/Users/user/Downloads/Python/Projects/Project 117/Images/"
Images=[]
for file in os.listdir(path):
    name, ext=os.path.splitext(file)
    if ext in ['.png', '.gif', '.jfif', '.jpeg', '.jpg']:
        file_name=path+file
        #print(file_name)
        Images.append(file_name)
count=len(Images)
frame = cv2.imread(Images[0])
width, height, channels=frame.shape
size=(width,height)
#print(size)
out=cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0, count-1):
    cv2.imread()
    out.write()
    
    if cv2.waitKey(25):
        break
print("Done")


