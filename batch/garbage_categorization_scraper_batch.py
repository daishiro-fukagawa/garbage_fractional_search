import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.city.shinjuku.lg.jp/seikatsu/seiso01_001025.html"
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "greenTable2"})

header1 = ["name", "type"]
header2 = ["type", "method"]

tbody = table.find("tbody")
rows1 = []
rows2 = []
for tr in tbody.find_all("tr"):
    row = [td.get_text(strip=True) for td in tr.find_all("td")]
    rows1.append(row[:2])  # name, type
    rows2.append(row[1:])  # type, ,method

with open("../public/data/garbage_names.csv", "w", encoding="utf-8", newline="") as f1:
    writer1 = csv.writer(f1)
    writer1.writerow(header1)
    writer1.writerows(rows1)

with open("../public/data/garbage_types.csv", "w", encoding="utf-8", newline="") as f2:
    writer2 = csv.writer(f2)
    writer2.writerow(header2)
    writer2.writerows(rows2)

print("CSVファイルにデータが書き込まれました。")