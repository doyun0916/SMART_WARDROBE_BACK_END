import numpy as np
import cv2
from sklearn.cluster import KMeans
import json

"""RGB"""
white = [(255, 255, 255)]
lightgray = [(192, 192, 192), (217, 214, 207), (201, 192, 187), (200, 200, 205)]
darkgray = [(96, 96, 96), (115, 106, 98), (139, 134, 128)]
black = [(0, 0, 0)]
red = [(255, 0, 0), (237, 10, 63), (195, 33, 72), (253, 14, 53), (198, 45, 66), (204, 71, 75), (204, 51, 54),
       (225, 44, 44), (217, 33, 33)]
pink = [(255, 0, 255), (252, 116, 253), (230, 103, 206), (226, 156, 210), (217, 108, 190), (246, 83, 166),
        (218, 50, 135), (255, 51, 153), (251, 174, 210), (247, 70, 138), (219, 80, 121), (252, 128, 165)]
orange = [(255, 127, 0), (255, 112, 52), (255, 104, 31), (255, 136, 100), (255, 185, 123), (236, 177, 118),
          (231, 114, 0)]
mustard = [(240, 179, 37)]
yellow = [(255, 255, 0), (242, 198, 73), (252, 214, 103), (252, 232, 131), (255, 235, 0), (250, 250, 55),
          (255, 255, 153)]
mint = [(0, 255, 255), (48, 191, 191), (0, 204, 204), (0, 128, 128)]
green = [(0, 255, 0), (175, 227, 19), (94, 140, 49), (123, 160, 91), (157, 224, 147), (99, 183, 108), (77, 140, 87),
         (58, 166, 85), (95, 167, 119), (41, 171, 135)]
olive = [(128, 128, 0)]
blue = [(143, 216, 216), (149, 224, 232), (108, 218, 231), (118, 215, 234), (126, 212, 230), (0, 149, 183),
        (0, 157, 196), (2, 164, 211), (71, 171, 204), (46, 180, 230), (51, 154, 204), (147, 204, 234), (40, 135, 200),
        (0, 70, 140), (0, 102, 204), (21, 96, 189), (69, 112, 230), (60, 105, 231), (71, 92, 119), (107, 129, 150)]
purple = [(127, 0, 255), (118, 110, 200), (100, 86, 183), (63, 38, 191), (139, 114, 190), (101, 45, 193),
          (107, 63, 160), (131, 89, 163), (143, 71, 179), (201, 160, 220), (191, 143, 204), (128, 55, 144),
          (115, 51, 128), (193, 84, 193), (115, 46, 108), (142, 49, 121), (200, 80, 155), (187, 51, 133),
          (166, 58, 121), (165, 11, 94)]
beige = [(232, 195, 129), (255, 203, 164), (253, 213, 177)]
brown = [(127, 64, 0), (233, 116, 81), (175, 89, 62), (158, 91, 64), (135, 66, 31), (222, 166, 129), (210, 125, 70),
         (102, 66, 40), (217, 154, 108), (128, 85, 51), (102, 82, 51), (168, 139, 129)]

colorset = (white, lightgray, darkgray, black, red, pink, orange, mustard, yellow, mint, green, olive, blue, purple, beige, brown)
colorsname = ['white', 'lightgray', 'darkgray', 'black', 'red', 'pink', 'orange', 'mustard', 'yellow', 'mint', 'green', 'olive', 'blue', 'purple', 'beige', 'brown']


def calc_distance(a):  # 거리값을 계산하고 그 값을 저장하는 역할
    dis_list = list()
    dis_list_total = list()
    for i in range(len(colorset)):
        for j in range(len(colorset[i])):
            dis = 0.0
            for k in range(len(a)):
                dis += (colorset[i][j][k] - a[k]) ** 2  # Euclidean distance 거리값을 계산한다.
            dis_list.append(np.sqrt(dis))  # 배열형태로 거리값을 저장한다.
        dis_list_total.append(min(dis_list))
        dis_list.clear()
    return dis_list_total.index(min(dis_list_total))


def find_color(a):
    b = calc_distance(a)
    return colorsname[b]


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist


def image_color_cluster(image_path, pred_mask, crop, k=3, inner=0):  # k값은 몇개의 색깔 인지
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                                         # 반대로 뒤집고 crop 따서 적용!

    try:
        if inner==1:
            #nsamples, nx, ny = crop_img.shape
            #crop_img2 = crop_img.reshape((nsamples*nx, ny))
            #print(crop_img2.shape, "inner")
            y1=int(crop["y1"])+int(crop["y1"]/9.5)
            y2=int(crop["y2"])-int(crop["y2"]/2)
            x1=int(crop["x1"])+int(crop["x1"]/2)
            x2=int(crop["x2"])-int(crop["x2"]/4)
            json_mask = np.array(pred_mask)
            json_mask2 = np.logical_not(json_mask)
            json_mask3 = json_mask2[y1:y2, x1:x2]
            #print(json_mask3.shape, "mask3 shape")
            image2=image[y1:y2, x1:x2]
            #print(image2.shape, "image2 shape")
            n = image2[json_mask3]
            #print(n.shape, "crop_masking")
        else:
            json_mask = np.array(pred_mask)
            n = image[json_mask]
            #print(n.shape, "masking")
        clt = KMeans(n_clusters=k)
        clt.fit(n)
    
    except:
        nul = []
        nul.append(1)
        return nul

    hist = centroid_histogram(clt)
    hist = np.sort(hist)[::-1]  # 색깔비율 내림차순 정렬
    result = []
    for i in range(k):
        temp = find_color(clt.cluster_centers_[i])
        result.append(temp)
    return result

