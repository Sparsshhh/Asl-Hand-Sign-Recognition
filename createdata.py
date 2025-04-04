import cv2
import os


directory= 'SignImage48x48/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
    
for i in range(71,77):
    letter  = chr(i)
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')




import os
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             'g': len(os.listdir(directory+"/G")),
             'h': len(os.listdir(directory+"/H")),
             'i': len(os.listdir(directory+"/I")),
             'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/K")),
             'l': len(os.listdir(directory+"/L")),
                          }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(128,128))
    interrupt = cv2.waitKey(10)

    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory+'G/'+str(count['g']))+'.jpg',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory+'H/'+str(count['h']))+'.jpg',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory+'I/'+str(count['i']))+'.jpg',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory+'J/'+str(count['j']))+'.jpg',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory+'K/'+str(count['k']))+'.jpg',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory+'L/'+str(count['l']))+'.jpg',frame)
   

    
