#! /usr/bin/env python3

import os
import requests
import json
import re
from pathlib import Path

def description_converter():
    home = str(Path.home())
    os.chdir(home + "/supplier-data/descriptions")
    cwd = os.getcwd()
    files = os.listdir(cwd)
    categories_list = []
    txt_search_list = []
    headers = ["name", "weight", "description"]
    for file in files:
        regex = r"(\d+).(txt)"
        txt_search = re.search(regex, file)
        if txt_search is None:
            continue
        txt_search = txt_search.groups()
        if txt_search[1] == "txt":
            txt_search_list.append(txt_search[0])
            count = 0
            categories_dict = {}
            with open(file, "r") as fruit_file:
                for line in fruit_file:
                    categories_dict[headers[count]] = line.strip()
                    if count < len(headers) - 1:
                        count += 1
                if categories_dict["weight"].endswith("lbs") == True:
                    regex2 = r"(\d+)"
                    int_weight = re.search(regex2, categories_dict["weight"])
                    int_weight = int_weight.groups()
                    categories_dict["weight"] = int(int_weight[0])
                else:
                    categories_dict["weight"] = int(categories_dict["weight"])
                categories_dict["image_name"] = txt_search[0] + ".jpeg"
                p = categories_dict
                requests.post("http://<your ip here>/fruits/", json = p)
        categories_list.append(categories_dict)
    for i in range(len(categories_list)):
        with open("{}.json".format(txt_search_list[i]), "w") as fruit_json:
            json.dump(categories_list[i], fruit_json, indent = 2)

description_converter()
