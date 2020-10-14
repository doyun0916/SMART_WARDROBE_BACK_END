import numpy as np
import cv2
from sklearn.cluster import KMeans
import json

"""RGB"""
white = (255, 255, 255)
lightgray = (211, 211, 211)
darkgray = (169, 169, 169)
black = (0, 0, 0)
red = (255, 0, 0)
pink = (255, 0, 255)
orange = (255, 127, 0)
mustard = (240, 179, 37)
yellow = (255, 255, 0)
mint = (0, 255, 255)
green = (0, 255, 0)
olive = (128, 128, 0)
navy = (0, 102, 204)
blue = (0, 0, 255)
purple = (127, 0, 255)
beige = (232, 195, 129)
brown = (127, 64, 0)

colorset = (white, lightgray, darkgray, black, red, pink, orange, mustard, yellow, mint, green, olive, navy, blue, purple, beige, brown)
colorsname = {0: 'white', 1: 'lightgray', 2: 'darkgray', 3: 'black', 4: 'red', 5: 'pink', 6: 'orange',
              7: 'mustard', 8: 'yellow', 9: 'mint', 10: 'green', 11: 'olive', 12: 'navy', 13: 'blue', 14: 'purple', 15: 'beige', 16: 'brown'}


def calc_distance(a):  # 거리값을 계산하고 그 값을 저장하는 역할
    dis_list = list()
    for i in range(len(colorset)):
        dis = 0.0
        for j in range(len(a)):
            dis += (colorset[i][j] - a[j]) ** 2  # Euclidean distance 거리값을 계산
        dis_list.append(np.sqrt(dis))  # 배열형태로 거리값을 저장한다
    return dis_list.index(min(dis_list))


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



def image_color_cluster(image_path, json_path, k=3):  # k값은 몇개의 색깔 인지
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with open(json_path) as f:
        json_data = json.load(f)
        json_mask = np.array(json_data["result"]["objects"][0]["pred_masks"])
    n = image[json_mask]

    clt = KMeans(n_clusters=k)
    clt.fit(n)

    hist = centroid_histogram(clt)
    hist = np.sort(hist)[::-1]  # 색깔비율 내림차순 정렬
    print(find_color(clt.cluster_centers_[0]))

