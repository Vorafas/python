import re
import requests

url = "http://cbr.ru/statistics/pr/"

session = requests.Session()
response = session.get(url)

htmlText = response.text
session.close()

data = re.findall("<td>(\d{1,2})</td>.+?<td>([А-Яа-я]{3,8})</td>.+?<td>([А-Яа-я]{3,8})</td>.+?<td>([^\<]{1,})</td>", htmlText, flags=re.DOTALL)

for num, start, finish, description in data:
    print(f"№ п.п: {num}")
    print(f"Дата начала: {start}")
    print(f"Дата окончания: {finish}")
    print(f"Наименование обследования: {description}")

