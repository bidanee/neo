from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dateutil.relativedelta import relativedelta
import requests, json
import os
from datetime import datetime, timedelta

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
secret_file = os.path.join(BASE_DIR,"..", "secret.json")
country_file = os.path.join(BASE_DIR, "main_countries.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.1.19"],  # 허용할 주소 (자신의 주소)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


with open(country_file) as f:
    country_code = json.loads(f.read())
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
  try:
      return secrets[setting]
  except KeyError:
      return f"Set the {setting} environment variable."
serviceKey = get_secret("ECOS_apiKey")


current_rate = 0
@app.get("/current_exchange_rate")
def get_current_exchange_rate(country: str = Query(..., description="나라 이름")):
    today = datetime.today()
    yesterday = today - timedelta(days=1)

    start_date = yesterday.strftime("%Y%m%d")
    end_date = today.strftime("%Y%m%d")

    # 입력한 나라 이름으로 항목 찾기 (ITEM_CODE1, code)
    country_info = next((item for item in country_code["exchange"] if item["country"] == country), None)
    if not country_info:
        return {"error": f"'{country}'에 해당하는 데이터를 찾을 수 없습니다."}

    item_code = country_info["ITEM_CODE1"]
    currency_code = country_info.get("code", "")  # 빈 문자열이면 None 대신 "" 반환

    # API 호출
    url = f"https://ecos.bok.or.kr/api/StatisticSearch/{serviceKey}/json/kr/1/100/731Y001/D/{start_date}/{end_date}/{item_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        items = data.get("StatisticSearch", {}).get("row", [])
        current_item = items[0]["DATA_VALUE"]
        result = [
            {
                "날짜": item["TIME"],
                "국가": country,
                "통화코드": currency_code,
                "환율": item["DATA_VALUE"]
            }
            for item in items
        ]
        if len(result) == 2:
            result = result[1]

        return result if result else {"message": "해당 국가에 대한 환율 데이터가 없습니다."}

    except Exception as e:
        return {"error": str(e)}

@app.get("/exchange_rate")
def get_exchange_rate(country: str = Query(..., description="나라 이름")):
    country_info = next((item for item in country_code["exchange"] if item["country"] == country), None)

    if not country_info:
      print("country_info is none")
      return {"error": f"'{country}'에 해당하는 데이터를 찾을 수 없습니다."}

    item_code = country_info["ITEM_CODE1"]

    end_date = datetime.now().strftime('%Y%m%d')
    start_date = (datetime.now() - timedelta(days=100)).strftime('%Y%m%d')

    url = (
        f"https://ecos.bok.or.kr/api/StatisticSearch/"
        f"{serviceKey}/json/kr/1/1000/731Y001/D/{start_date}/{end_date}/{item_code}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        items = data.get('StatisticSearch', {}).get('row', [])
        
        validItem = {}
        item_keys = ['ITEM_NAME1', 'DATA_VALUE']

        for i in items:
                key = i['TIME']
                filtered = {k: i[k] for k in item_keys}
                validItem[key] = filtered

        if not validItem:
            return {"error": "자료가 존재하지 않습니다."}
        return {
          "labels": list(validItem.keys()),
          "datasets": [{
            "label": next(iter(validItem.values()))["ITEM_NAME1"],
            "data": [float(v["DATA_VALUE"]) for v in validItem.values()],
          "backgroundColor": "#ffffff",
          "borderColor": "#ff8686",
          "borderWidth": 2
          }],
          "current_rate": current_rate
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_current_exchange_all")
def get_exchange_rate():
    start_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
    end_date = datetime.now().strftime('%Y%m%d')
    url = (
        f"https://ecos.bok.or.kr/api/StatisticSearch/"
        f"{serviceKey}/json/kr/1/1000/731Y001/D/{start_date}/{end_date}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        items = data.get('StatisticSearch', {}).get('row', [])
        return items

    except Exception as e:
        return {"error": str(e)}