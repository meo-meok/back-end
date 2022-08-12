import os
def makeDB() : 
    dpath = "DB"
    flist = os.listdir(dpath)

    total_data = list()
    # category number
    # 1 : 한식/분식  2 : 돈까스/회/일식  3 : 중식  4 : 양식  5 : 아시안  6: 고기/구이  7 : 닭/치킨  8 : 찜/탕/찌개  9 : 패스트푸드  10 : 카페/디저트  11 : 호프/주류
    catelist = ['한식/분식', '돈까스/회/일식', '중식', '양식', '아시안', '고기/구이', '닭/치킨', '찜/탕/찌개', '패스트푸드', '카페/디저트', '호프/주류']

    for files in flist :
        fpath = dpath + "/" + files

        with open(fpath, 'r') as f :
            infolist = f.readlines()[:3]

            tmpdic = dict()

            name = files[:-4]
            tmpdic['name'] = name

            cate = infolist[0].rstrip().split(" : ")
            tmpdic['category'] = catelist.index(cate[1]) + 1       

            address = infolist[1].rstrip().split(" : ")
            tmpdic['address'] = address[1]

            number = infolist[2].rstrip().split(" : ")
            tmpdic['number'] = number[1]

            total_data.append(tmpdic)
    
    return total_data
