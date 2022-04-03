from PIL import Image
from PIL import ImageDraw,ImageFont
import cv2

def img_text():      # Function Created
 img = cv2.imread('C:/Users/Administrator/wf9.jpg', cv2.IMREAD_GRAYSCALE)  # Read the image
 font = cv2.FONT_HERSHEY_COMPLEX    # Set The Font
 cv2.putText(img,'What is Your name : _____________________',(200,250), font, .5,(0,0,0),1,cv2.LINE_AA)  # draw The Text
# initialize counter
 i = 0
 while True:
    cv2.imshow('a',img)   # Display the image
    cv2.imwrite('C:/Users/Administrator/wf_9.jpg',img)  # Save Image  
    myFont = cv2.FONT_HERSHEY_SIMPLEX
    k = cv2.waitKey(0)   # wait for keypress
    cv2.putText(img,chr(k),(390+i,245), myFont, .4,(0,0,0),1,cv2.LINE_AA)  # specify the font and draw the key using puttext
    i+=10
    if k == ord('q'):
        break
 cv2.destroyAllWindows()
print(img_text())         # Call Function