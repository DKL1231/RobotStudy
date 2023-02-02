import cv2 as cv
import numpy as np

def mouse_callback(event, x, y, flags, param):
    if event == 1:
        print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
        print('=================================')


Path = 'Data/'
Name = 'rabong.jpg'
FullName = Path + Name

# 이미지 읽기
img = cv.imread(FullName)


new_img = img.copy()
result = [0, 0, 0, 0]
for i in range(512):
    for j in range(512):
        tmp = img[i][j]
        if 200 <= sum(tmp)-tmp[0]:
            new_img[i][j] = 0, 0, 255
        if i < 256:
            if j < 256:
                if new_img[i][j][0] == 0 and new_img[i][j][1] == 0 and new_img[i][j][2] == 255:
                    result[1] += 1
            else:
                if new_img[i][j][0] == 0 and new_img[i][j][1] == 0 and new_img[i][j][2] == 255:
                    result[0] += 1
        else:
            if j < 256:
                if new_img[i][j][0] == 0 and new_img[i][j][1] == 0 and new_img[i][j][2] == 255:
                    result[2] += 1
            else:
                if new_img[i][j][0] == 0 and new_img[i][j][1] == 0 and new_img[i][j][2] == 255:
                    result[3] += 1


print(f'위치 : 제{result.index(max(result))+1}사분면')
print(f'크기 : {new_img.shape}')
# 이미지 출력
cv.imshow('img', img)
cv.imshow('result', new_img)
# cv.imshow('gray1', gray1)
# cv.imshow('gray', gray)
# cv.imshow('blur', blur)


while cv.waitKey(33) <= 0:
    cv.setMouseCallback('img', mouse_callback, img)

cv.waitKey(0)
