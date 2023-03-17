import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.city.shinjuku.lg.jp/seikatsu/seiso01_001025.html"
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "greenTable2"})

header = ["name", "type", "method"]

rows = []
for tr in table.find_all("tr")[1:]:
    row = [td.get_text(strip=True) for td in tr.find_all("td")]
    rows.append(row)

with open("../public/data/garbage_data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("CSVファイルにデータが書き込まれました。")