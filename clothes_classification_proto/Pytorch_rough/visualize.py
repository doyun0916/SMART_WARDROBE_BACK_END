import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from model.check import Classify

width=5
height=5
rows = 2
cols = 3
axes=[]
fig=plt.figure()
# if c == 1:
#                 return {0: "cardigan", 1: "coat", 2: "coat fur", 3: "blazer", 4: "bomber", 5: "denim", 6: "leather", 7: "parka", 8: "trench coat"}[predic]
#             if c == 2:
#                 return {0: "short blouse", 1: "short shirt", 2: "short tee"}[predic]
#             if c == 3:
#                 return {0: "long tee", 1: "long blouse", 2: "long shirt", 3: "long tee", 4: "sweater", 5: "turtleneck"}[predic]
#             if c == 4:
#                 return {0: "denim shorts", 1: "romper", 2: "shorts"}[predic]
#             if c == 5:
#                 return {0: "chinos", 1: "jean", 2: "jumpsuit", 3: "leggings", 4: "sweatpants"}[predic]
#             if c == 6:
#                 return {0: "long skirt", 1: "short skirt"}[predic]
#             if c == 7:
#                 return {0: "long shirt", 1: "long tee"}[predic]

for a in range(rows*cols):
    img = "./test_sample/outer/" + str(a) + ".jpg"
    b = Image.open(img)
    predict = Classify("../mrcnn/models/outer/outer_new2.pt")
    prediction = predict.predict(img)
    k = fig.add_subplot(rows, cols, a+1)
    axes.append(k)
    subplot_title=({0: "cardigan", 1: "coat", 2: "coat fur", 3: "blazer", 4: "bomber", 5: "denim", 6: "leather", 7: "parka", 8: "trench coat"}[prediction])
    axes[-1].set_title(subplot_title)
    k.axis('off')
    plt.imshow(b)
fig.tight_layout()
plt.show()
