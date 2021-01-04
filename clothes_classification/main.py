import os
import json
from MaskRCNN.model import Model
from resnet.model import Classify
from k_means.model_new import image_color_cluster, image_color_cluster_jean
import pandas as pd

# First: Install requirements
## pip install -r requirements.txt

# Second: Install detectron2
## python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
## (add --user if you don't have permission)

if __name__ == "__main__":
    # params : model weights path
    # weights.pth can download https://drive.google.com/file/d/1R2XdqES4WXVJCVSdUgPh-xjX2xVxu0H-/view?usp=sharing
    mrcnn_model = Model("./weights.pth", threshold=0.7)
    # params :
    # image_path : image path
    # download : download masking image ("./output.jpg")
    path_rest = '/woman/street'                                                    # change img directory
    path_dir = '/mnt/c/Users/doyun/PycharmProjects/mrcnn/street_snap' + path_rest
    file_list = os.listdir(path_dir)

    def Classifi(c, model, image, crop, u=0):
        pre = Classify(model)
        if u==0:
            predic = pre.predict(image, crop, 0)
        else:
            predic = pre.predict(image, crop, 1)
        if predic == None:
            return None
        else:
            if c == 1:
                return {0: "cardigan", 1: "coat", 2: "coat fur", 3: "blazer", 4: "bomber", 5: "denim", 6: "leather", 7: "parka", 8: "trench coat"}[predic]
            if c == 2:
                return {0: "short blouse", 1: "short shirt", 2: "short tee"}[predic]
            if c == 3:
                return {0: "long tee", 1: "long blouse", 2: "long shirt", 3: "long tee", 4: "sweater", 5: "turtleneck"}[predic]
            if c == 4:
                return {0: "denim shorts", 1: "romper", 2: "shorts"}[predic]
            if c == 5:
                return {0: "chinos", 1: "jeans", 2: "jumpsuit", 3: "leggings", 4: "sweatpants"}[predic]
            if c == 6:
                return {0: "long skirt", 1: "short skirt"}[predic]
            if c == 7:
                return {0: "long shirt", 1: "long tee"}[predic]
    
    result = []
    for j in range(len(file_list)):
        img = "./street_snap" + path_rest + "/" + file_list[j] # for loop for the file amount
        predictions = mrcnn_model.predict_from_image(img, download=False)
        temp = predictions["result"]["objects"]
        num = len(temp)
        obj = {}
        #obj['file'] = file_list[j]
        for i in range(num):
            classnum = temp[i]["classId"]
            if classnum == 3:
                classi_temp = Classifi(1, "./models/outer/outer_new2.pt", img, temp[i], 0)
                if classi_temp != None:
                    obj["outer"] = classi_temp
                    if classi_temp == "denim":
                        obj["outercol"] = image_color_cluster_jean(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                    else:
                        obj["outercol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                temp2 = Classifi(3, "./models/top/top_long_new2.pt", img, temp[i], 0)
                if temp2 != None:
                    if temp2 == "long tee" or temp2 == "long shirt":
                        temp4 = Classifi(7, "./models/top/tee_shirt3.pt", img, temp[i], 1)
                        if temp4 != None:
                            obj["top"] = temp4
                            temp4 = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 1)[0]
                            if temp4 == 1:
                                del obj["top"]
                            else:
                                obj["topcol"] = temp4
                    else:
                        obj["top"] = temp2
                        temp3 = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 1)[0]
                        if temp3 == 1:
                            del obj["top"]
                        else:
                            obj["topcol"] = temp3
            elif classnum == 0 or classnum == 2:
                classi_temp = Classifi(2, "./models/top/top_short.pt", img, temp[i], 0)
                if classi_temp != None:
                    obj["top"] = classi_temp
                    obj["topcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
            elif classnum == 1:
                temp2 = Classifi(3, "./models/top/top_long_new2.pt", img, temp[i], 0)
                if temp2 != None:
                    if temp2 == "long tee" or temp2 == "long shirt":
                        obj["top"] = Classifi(7, "./models/top/tee_shirt3.pt", img, temp[i], 1)
                    else:
                        obj["top"] = temp2
                    obj["topcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
            elif classnum == 6:
                stand2 = Classifi(4, "./models/bottom/bottom_short.pt", img, temp[i], 0)
                if stand2 != None:
                    if stand2 == 'romper':
                        obj['dress'] = stand2
                        obj['dresscol'] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                    else:
                        obj["bottom"] = stand2
                        if stand2 == "denim shorts":
                            obj["bottomcol"] = image_color_cluster_jean(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                        else:
                            obj["bottomcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
            elif classnum == 7:
                stand = Classifi(5, "./models/bottom/bottom_long_new.pt", img, temp[i], 0)
                if stand != None:
                    if stand == 'jumpsuit':
                        obj['dress'] = stand
                        obj['dresscol'] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                    else:
                        obj["bottom"] = stand
                        if stand == "jeans":
                            obj["bottomcol"] = image_color_cluster_jean(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                        else:
                            obj["bottomcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
            elif classnum == 8:
                classi_temp = Classifi(6, "./models/bottom/bottom_skirt.pt", img, temp[i], 0)
                if classi_temp != None:
                    obj["bottom"] = classi_temp
                    obj["bottomcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
            elif classnum == 4:    #vest
                obj["outer"] = temp[i]['class']
                obj["outercol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
                temp2 = Classifi(3, "./models/top/top_long_new2.pt", img, temp[i], 0)
                if temp2 != None:
                    if temp2 == "long tee" or temp2 == "long shirt":
                        obj["top"] = Classifi(7, "./models/top/tee_shirt3.pt", img, temp[i], 1)
                    else:
                        obj["top"] = temp2
                    temp3 = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 1)[0]
                    if temp3 == 1:
                        del obj["top"]
                    else:
                        obj["topcol"] = temp3
            elif classnum == 5:  #sling
                obj["top"] = temp[i]['class']
                obj["topcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
            else:     #dress
                obj["dress"] = temp[i]['class']
                obj["topcol"] = image_color_cluster(img, temp[i]["pred_masks"], temp[i], 1, 0)[0]
        obj["url"] = "https://smart-wardrobe-static.s3.amazonaws.com/street_snap" + path_rest + "/" + file_list[j]
        result.append(obj)
        print(result[j], "\n")
   
    #pree = []
    #img = "./mss" + path_rest + "/" + "13701.jpg" # for loop for the file amount
    #predictions = mrcnn_model.predict_from_image(img, download=False)
    #temp = predictions["result"]["objects"]
    #print(temp)

    #for i in range(len(temp)):
        #col = image_color_cluster(img, temp[i]["pred_masks"], 1)[0]
        #print(col)
    #pree.append(temp)
    
    #dataframe = pd.DataFrame(result)
    #dataframe.to_csv("./Vali_test_0.1lim_Clanum=1TeeShirt_Inner_only_mask", header=False, index=False)

    #dataframe2 = pd.DataFrame(result)
    #dataframe2.to_csv("./Vali_test_headerAdded_0.1lim_onlyTeeShirtMasked_jeanfixed.csv", header=True, index=False)
    
    with open("./street_snap_woman_street.json", 'w') as outfile:
            json.dump(result, outfile)                #prediction 대신에 result
