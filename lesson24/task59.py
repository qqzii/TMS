import json
import requests

response = requests.get(' https://www.nbrb.by/api/exrates/rates/dynamics/145?startDate=2021-6-18&endDate=2021-6-25')

data = json.loads(response.text)
print(data)

def average(data_):
    summa = 0
    days = 0
    for i in data_:
        summa += i['Cur_OfficialRate']
        days += 1
    return summa / days

print(average(data))
