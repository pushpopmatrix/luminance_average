# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
import cv2

#初期化
cap = cv2.VideoCapture(0)
x = []
y = []
i = 0
j = 0
plt.ion()

plt.title('luminance of frame') #グラフタイトル
plt.xlabel('time') #x軸ラベル
plt.ylabel('luminance') #y軸ラベル
plt.xlim(0,200) #x軸範囲固定
plt.grid() #グリッド線

while True:
    #VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()
    #ウェブカメラからの画像を表示
    frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
    cv2.imshow('HeartBeat', frame)
    
    #輝度値の平均を保存
    j = frame[:, :, :].flatten().mean()
    i += 1
    x.append(i)
    y.append(j)
    plt.plot(x,y,color='r')
    plt.draw()

    #iがある値になったら終了
    if i == 200:
        break
    #待機時間
    plt.pause(0.1)

#plt.close()
cap.release()
#終了したらウィンドウを全て閉じる
#cv2.destroyAllWindows()
