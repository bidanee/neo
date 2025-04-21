from fastapi import FastAPI
import requests, json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath('./'))
secret_file = os.path.join(BASE_DIR, "secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        return f"Set the {setting} environment variable."

@app.get("/exchange_rate")
def get_exchange_rate():
    serviceKey = get_secret("ECOS_apiKey")

    url = (
        "https://ecos.bok.or.kr/api/StatisticSearch/"
        + serviceKey +
        "/json/kr/1/1000/731Y004/M/202301/202403/0000001"
    )

    response = requests.get(url)
    contents = response.text
    dict_data = json.loads(contents)
    items = dict_data['StatisticSearch']['row']

    item = ['ITEM_NAME1','DATA_VALUE']
    validItem = {}

    for i in items:
        if i['ITEM_NAME2'] == '평균자료':
            key = i['TIME']
            filtered = {k: i[k] for k in item}
            validItem[key] = filtered

    return validItem 
