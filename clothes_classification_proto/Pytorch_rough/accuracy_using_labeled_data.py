import csv
import numpy as np
import pandas as pd

f = open('./test_data_prediction.csv', 'r', encoding='utf-8')               # label에 format맞춰서 각각 비교후 결과계산!
rdr = csv.reader(f)
predict = list(rdr)
# for line in rdr:
#     print(line)
f.close()

f2 = open('./test_data_label.csv', 'r', encoding='utf-8')
rdr2 = csv.reader(f2)
target = list(rdr2)
# for line in rdr:
#     print(line)
f2.close()

result = []
temp = []
per = 0
cen = 0
average = 0
predict[0].insert(0, 'Num')
predict[0].append('accuracy')
result.append(predict[0])
for i in range(len(predict)-1):
    temp.append(i+1)
    temp.append(predict[i+1][0])
    for j in range(8):
        if predict[i+1][j+1] == target[i+1][j+1]:
            temp.append(1)
            per += 1
        #elif target[i+1][j+1] == "":
        #    temp.append(1)
        #    per += 1
        else:
            temp.append(0)
    cen += 8
    result.append(temp)
    temp = []
final = (per/cen)
dataframe2 = pd.DataFrame(result)
dataframe2.to_csv("./test_data_results(without null).csv", header=True, index=False)
print(np.array(result))
print("\n")
print( 'Average accuracy=', final)



#print(target[0])
#
# a = 0
# b = "a"
# fi = []
# result = []
# result.append(a)
# result.append(b)
# fi.append(result)
# print(fi)

# print(result)
#print(3.2510e-02 + 1.0384e-02 + 3.8575e-03 + 3.3311e-01 + 1.0805e-01 + 1.3653e-02 + 4.8909e-01 + 2.3686e-05 + 9.3299e-03)
