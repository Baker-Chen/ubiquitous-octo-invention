import cv2
import time
import os
import HandTrackingModule as htm
from handRecog import handrecongnition
from collections import deque
import requests

# 電梯樓層最多 HEIGHT 位數
HEIGHT = 1

# 網頁電梯模擬伺服器IP
IP = '36.228.196.251:5000'

# 手勢緩衝暫存長度
FIFO_LENGTH = 11

def gestureRecogFloor():
    
    wCam, hCam = 640, 480
    
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    
    startTime = time.time()
    # used to calculate frame rate
    fpsTime = 0

    # Gesture recognition will last for 15 sec 
    # then switch to idle state 
    idleTime = 15

    # hand pose recognizer
    detector = htm.handDetector(detectionCon=0.75)
    tipIds = [4, 8, 12, 16, 20]

    # 手勢暫存器
    gesturenow = 'x'
    gesturepre = 'x'

    # 樓層暫存器
    floorCount = 0
    floor = ['x']*HEIGHT

    # 手勢緩衝暫存器
    gestureFifo = deque(['x']*FIFO_LENGTH)
    
    while True:
        print('Time: ' + '%.2f'%(time.time()-startTime) + 's')
        
        # 取得辨識結果 
        ret, img = cap.read()
        img = cv2.flip(img,1)
        img,multih = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        # 確認手指是否伸直 
        if len(lmList) != 0:
            leftOright = multih[0].classification[0].label
            fingers = []
    
            # Thumb 
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                if leftOright == 'Left':
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if leftOright == 'Left':
                    fingers.append(0)
                else:
                    fingers.append(1)
    
            # 4 Fingers 
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 根據各手指是否伸直辨認當下的手勢 
            gesture = handrecongnition(fingers)
            totalFingers = fingers.count(1)
        else:
            gesture = 'x'
    
        # 將手勢放進暫存器 
        if len(gestureFifo) >= FIFO_LENGTH:
            gestureFifo.pop()
        gestureFifo.appendleft(gesture)

        # 將樓層傳給伺服器 
        if floorCount >= HEIGHT:
            test = 0
            for i,j in enumerate(floor):
                test += int(j) * 10**(HEIGHT-i-1)
            print(test)
            x = requests.post('http://'+str(IP)+'/change', data= {"text":str(test)})
            
            floor = ['x']*HEIGHT
            floorCount = 0
            return False


        gesturenow = max(sorted(set(gestureFifo)),key=gestureFifo.count)
        gesturepre = gesturenow

        # 將非功能型手勢輸入放入樓層暫存器
        if gesturenow == 'open':
            print('Time: ' + '%.2f'%(time.time()-startTime) + 's' + " open")
            x = requests.post('http://'+str(IP)+'/door', data= {"text":"o"})
            
        elif gesturenow == 'close':
            print('Time: ' + '%.2f'%(time.time()-startTime) + 's' + " close")
            x = requests.post('http://'+str(IP)+'/door', data= {"text":"c"})
            
        elif gesturenow == 'ok' and (gesturepre != 'ok' and gesturepre != 'x' and gesturepre != 'open' and gesturepre != 'close'):

            print(gesturepre,' ',gesturenow)
            floor[floorCount] = gesturepre
            floorCount+=1

        # 計算frame rate
        cTime = time.time()
        fps = (1 / (cTime - pTime)) if (cTime - fpsTime)>0 else 100
        fpsTime = cTime

        # 渲染畫面
        cv2.putText(img, gesturenow, (45, hCam-50), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 20)
        for i,j in enumerate(floor):
            cv2.putText(img, j, (45+100*i, hCam-180), cv2.FONT_HERSHEY_PLAIN,
                        10, (0, 0, 255), 20)
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 6)
    
        cv2.imshow("Image", img)

        # Idle over idleTime seconds
        if time.time()-startTime >= idleTime:
            cap.release()
            return False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False

if __name__ == "__main__":
    while True:
        gestureRecogFloor()
