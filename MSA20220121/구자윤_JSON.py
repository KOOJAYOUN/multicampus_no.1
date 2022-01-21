# 디버깅-jsonlab06.py -> with => try ~ exception ?
# 파일열기 - json 파일 읽기: 경로명 꼭 주의
# 파일쓰기 - json파일쓰기

import json


try:
    fileName = open("datalab\\mydata.json", "rb") as jsonFile:
    tempData = json.load("datalab\\mydata.json")
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
except:
    print("오류")
else:
    fileName.close()

jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }


with open("datalab\\mydata2.json", "w") as writeFile:
    json.dump(jsonData1, writeFile)

with open("datalab\\mydata3.json", "w", encoding="utf-8") as writeFile:
    json.dump(jsonData1, writeFile, ensure_ascii=False) 

with open("datalab\\mydata4.json", "w") as writeFile:
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)   


with open("datalab\\mydata5.json", "w", encoding="utf-8") as writeFile:
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)


temp =0
