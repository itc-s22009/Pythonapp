import json
import pandas as pd

with open('rakuten_api_chikuCode_file.json') as f:
    res = json.load(f)

prefectures = res['areaClasses']['largeClasses'][0]['largeClass'][1]['middleClasses']

list_a = []#middleClassCode・middleClassNameを入れるリスト
list_b = []#smallClassCode・smallClassNameを入れるリスト
list_c = []#detailClassCode・detailClassNameを入れるリスト

for i in range(len(prefectures)):
    for j in range(len(prefectures[i]['middleClass'][1]['smallClasses'])):
        if len(prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass']) == 2:
            for k in range(len(prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][1]['detailClasses'])):
                list_a.append(prefectures[i]['middleClass'][0]['middleClassCode'] + ' ' + prefectures[i]['middleClass'][0]['middleClassName'])
                list_b.append(prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][0]['smallClassCode'] + ' ' + prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][0]['smallClassName'])
                list_c.append(prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][1]['detailClasses'][k]['detailClass']['detailClassCode'] + ' ' + prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][1]['detailClasses'][k]['detailClass']['detailClassName'])
        
        else:
            list_a.append(prefectures[i]['middleClass'][0]['middleClassCode'] + ' ' + prefectures[i]['middleClass'][0]['middleClassName'])
            list_b.append(prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][0]['smallClassCode'] + ' ' + prefectures[i]['middleClass'][1]['smallClasses'][j]['smallClass'][0]['smallClassName'])
            list_c.append('-')

df_a = pd.DataFrame(list_a, columns = ['largeClassCode'])
df_b = pd.DataFrame(list_b, columns = ['smallClassCode'])
df_c = pd.DataFrame(list_c, columns = ['detailClassCode'])

df_all = pd.concat([df_a, df_b, df_c], axis=1, ignore_index=False)

df_all.to_csv('rakuten_api_chikucode_ichiran.csv', index=False)