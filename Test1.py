import requests
import json

json_url = 'http://ebiz.heung-a.com/intra/sailing_web/cf_n_sch_qry.cfm?fm_port=KRPUS&to_port=HKHKG&yyyymm=201807'
json_string = requests.get(json_url).text
data_list = json.loads(json_string)
col_len = data_list['ROWCOUNT']

idx = 0
for idx in range(0, col_len - 1):
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    for col in data_list['DATA']:
        print(col, ":", data_list["DATA"][col][idx])

