import requests, os
import pandas as pd
import numpy as np
import folium
from folium.plugins import MiniMap

def elec_location(region,page_num):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region,'page': page_num}
    headers = {"Authorization": "KakaoAK a56011af4a120fea91496b1b1bfcc909"}

    places = requests.get(url, params=params, headers=headers).json()['documents']
    # print(places)
    return places

def elec_info(places):
    result = []

    X = []
    Y = []
    stores = []
    road_address = []
    cate = []
    for place in places:
        X.append(float(place['x']))
        Y.append(float(place['y']))
        stores.append(place['place_name'])
        road_address.append(place['road_address_name'])
        cate.append(place['category_name'])

    result.append(X)
    result.append(Y)
    result.append(road_address)
    result.append(stores)

    result.append(cate)

    return result

def keywords(location_name):
    dlist = list()
    local_name = elec_location(location_name, 1)
    local_elec_info = elec_info(local_name)

    dlist.append(local_elec_info)

    return dlist

dirpath = "DB"
dirlist = os.listdir(dirpath)

totals = list()

for files in dirlist :
    tmplist = []
    filename = files[:-4]
    fname = dirpath + "/" + files
    try :
        with open(fname, 'r') as f :
            lines = f.readlines()
            address = " ".join(lines[1].rstrip().split(" : ")[1].split()[:5])
            if filename == "대패생각" :
                address = "경북 포항시 북구 양덕동 1914"
            elif filename == "오픈오프(OPENOFF)" :
                address = '경북 포항시 북구 양덕동 1243'

            df = keywords(address)
            check = False
            # print(df)
            
            for names in df[0][3] :
                if filename == names :
                    check = True 
            if check :
                for names in range(len(df[0][3])) :
                    if df[0][3][names] == filename :
                        # print("{} : {}".format(filename, names))
                        tmplist.append(df[0][3][names])
                        tmplist.append(df[0][0][names])
                        tmplist.append(df[0][1][names])
                        check = True
            else :
                tmplist.append(filename)
                tmplist.append(df[0][0][0])
                tmplist.append(df[0][1][0])
        with open("axis.txt", 'a') as f :
            f.write("{} : {}, {}\n".format(tmplist[0], tmplist[1], tmplist[2]))
            
    except :
        with open("axis.txt", 'a') as f :
            f.write("{} : 0, 0\n".format(tmplist[0]))
            print(tmplist[0])