import cv2
import numpy

path =  './wing.jpg'

img = cv2.imread(path, 0)
resize = cv2.resize(img, (127, 127))


center = (-127 // 2) // 100
print(center)

def getAdd(x, y):
    global resize
    global center
    return resize[center + y][center + x]

def setAdd(x, y, rgb):
    global resize
    resize[y][x] = rgb

arr = []
count = 0
for x in range(127):
    for y in range(127):
        if getAdd(x, y) < 200:
            count += 1
            if count == 2:
                arr.append([round((x), 1 ), round((y), 1)])
                count = 0
                setAdd(round((x), 1 ), round((y ), 1), 255)

data = ''

for i in range(len(arr)):
    data += str(arr[i]) + '\n'

print(data.replace('\n', ',\n'))
cv2.imshow('show img', resize)

    
