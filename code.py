import cv2
import numpy as np
import os

def writecsv(color,shape):
    filep = open('results1A_745.csv','a')
    datastr = "," + color + "-" + shape
    filep.write(datastr)
def main(path):

    class ShapeDetector:
        def initial(self):
            pass
        def detect_shape(self, contour):
            ss="shape not identified"
            l=cv2.arcLength(contour, True)
            ww=cv2.approxPolyDP(contour,0.04*l,True)
            if len(ww) == 3:
                ss = "triangle"
            elif len(ww) == 4:
                (m,n,o,q) = cv2.boundingRect(ww)
                po =o/ float(q)
                ss="square" if po >= 0.95 and po <= 1.05 else "rectangle"
            elif len(ww)==5:
                ss="pentagon"
            else:
                ss="circle"
            return ss
    print path
    img=cv2.imread("test"+str(path[8])+".png")
    img2=img
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,150,255,0)
    m2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,
                                                       cv2.CHAIN_APPROX_SIMPLE)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)       
    sd = ShapeDetector()
    lower=np.array([110,50,50])
    upper=np.array([130,255,255])
    result=cv2.inRange(hsv,lower,upper)
    ret1,thresh1 = cv2.threshold(result,150,255,0)
    im,c2,h2 = cv2.findContours(thresh1,cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)
    k=len(c2)
    ll=[]
    o=0
    for kk in range(k):
        m=cv2.moments(c2[kk])
        cx=int(m['m10']/m['m00']) 
        cy=int(m['m01']/m['m00'])
        color="blue"
        cv2.putText(img2, color, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 0, 0), 1)
        cv2.drawContours(img,c2,kk,(0,0,0),2)
        shape = sd.detect_shape(c2[kk])
        cv2.putText(img2, shape, (cx+45,cy), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 0), 1)
        s=color+"-"+shape
        writecsv(color,shape)
        ll.insert(o,str(s))
        o+=1
    lower=np.array([0,100,100])
    upper=np.array([20,255,255])
    result=cv2.inRange(hsv,lower,upper)
    ret1,thresh1 = cv2.threshold(result,150,255,0)
    im,c2,h2 = cv2.findContours(thresh1,cv2.RETR_TREE,
                                                       cv2.CHAIN_APPROX_SIMPLE)
    k=len(c2)
    for kk in range(k):
        m=cv2.moments(c2[kk])
        cx=int(m['m10']/m['m00'])
        cy=int(m['m01']/m['m00'])
        color="red"
        cv2.putText(img2, color, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 0, 0), 1)
        cv2.drawContours(img,c2,kk,(0,0,0),2)
        shape = sd.detect_shape(c2[kk])
        cv2.putText(img2, shape, (cx+45,cy), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 0, 0), 1)
        s=color+"-"+shape
        writecsv(color,shape)
        ll.insert(o,str(s))
        o+=1
    lower=np.array([40,100,100])
    upper=np.array([100,255,255])
    result=cv2.inRange(hsv,lower,upper)
    ret1,thresh1 = cv2.threshold(result,150,255,0)
    im,c2,h2 = cv2.findContours(thresh1,cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    k=len(c2)
    for kk in range(k):
        m=cv2.moments(c2[kk])
        cx=int(m['m10']/m['m00'])
        cy=int(m['m01']/m['m00'])
        color="green"
        cv2.putText(img2, color, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 0, 0), 1)
        cv2.drawContours(img,c2,kk,(0,0,0),2)
        shape = sd.detect_shape(c2[kk])
        cv2.putText(img2, shape, (cx+45,cy), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 0), 1)
        s=color+"-"+shape
        writecsv(color,shape)
        ll.insert(o,str(s))
        o+=1
    
    v="output"
    cv2.imwrite(v+str(path[8])+".png",img)
 
    return(ll)

if __name__ == "__main__":
    mypath = '.'
    onlyfiles = [mypath.join(f) for f in os.listdir(mypath) if f.endswith(".png")]
    for fp in onlyfiles:
        filep = open('results1A_745.csv','a')
        filep.write(fp)
        filep.close()
        data = main(fp)
        print data
        filep = open('results1A_745.csv','a')
        filep.write('\n')
        filep.close()
