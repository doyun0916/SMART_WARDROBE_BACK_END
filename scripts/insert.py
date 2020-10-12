from coordi.models import Mancasual, Mancampus, Manminimal, Manstreet, Mantravel, Mansports, Manformal, Mandandy, Wosports, Wocasual, Woformal, Woromantic, Wogirlish, Wostreet, Wofeminine, Wotravel

from coordi.serializers import CoordiSerializer

import json

with open("./result_fi.json", "r") as json_file:
        json_data = json.load(json_file)

num = len(json_data)
def run():
    for i in range(num):
        insert_check = CoordiSerializer(data=json_data[i])
        if insert_check.is_valid():
            insert_check.save()
