from coordi.models import Mcasual, Mcampus, Mminimal, Mstreet, Mtravel, Msports, Mformal, Mdandy, Wsports, Wcasual, Wformal, Wromantic, Wgirlish, Wstreet, Wfeminine, Wtravel

from coordi.serializers import McasualSerializer   ## 각각 style별로 바꿔주면됨 넣을때 마다

import json

with open("./result_fi.json", "r") as json_file:
        json_data = json.load(json_file)

num = len(json_data)
def run():
    for i in range(num):
        insert_check = CoordiSerializer(data=json_data[i])    ### 이 친구도 마찬가지
        if insert_check.is_valid():
            insert_check.save()
