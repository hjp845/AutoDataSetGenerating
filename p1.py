import cv2
import numpy as np
import random

def hjp(n):
    for i in range(n):        
        
        background_num = random.randrange(3) # write your background files count in parameter

        img1 = cv2.imread('background/bg%d.jpg' % (background_num))
        img2 = cv2.imread('images/cross.png')

        rows1, cols1, channels1 = img1.shape
        rows2, cols2, channels2 = img2.shape

        #print(rows1, cols1, channels1)
        #print(rows2, cols2, channels2)

        y = random.randrange(200, 800)
        x = (y * 2 )// 3

        vpos = random.randrange(0, rows1 - y)
        hpos = random.randrange(0, cols1 - x)

        

        #print(vpos, hpos, x, y)
        
        img2 = cv2.resize(img2, dsize=(x, y), interpolation=cv2.INTER_AREA)
        
        
        
        roi = img1[vpos:vpos+y, hpos:hpos+x]
        
        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)


        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        
        
        img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
        
        dst = cv2.add(img1_bg, img2_fg)
        img1[vpos:vpos+y, hpos:hpos+x] = dst

        cv2.imwrite('save/test%d.jpg' % (i),img1)


        #vpos: 왼쪽 위
        #vpos + y: 왼쪽 아래
        #hpos: 오른쪽 위
        #hpos + x: 오른쪽 아래
        f = open("save/test%d.txt" % (i), 'w')
        f.write('%d %.6f %.6f %.6f %.6f' % (0, (hpos + x/2) / rows1, (vpos + y/2) / cols1, x / rows1, y / cols1))
        # 클래스번호, 왼쪽으로부터 사진 중심, 위쪽으로부터 사진 중심, 사진 가로, 사진 세로 (비율)
        f.close()
        #cv2.imshow('result', img1)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
#you can modify count
hjp(10)
