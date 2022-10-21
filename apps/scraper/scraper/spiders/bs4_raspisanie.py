from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from fake_useragent import UserAgent
import csv

url = "https://rsp.chemk.org/1korp/tomorrow.htm"

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.chrome}

html_content = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_content, "lxml")


# print(soup.prettify())

table = soup.find("table", attrs={"class": "MsoNormalTable"})
print("Number of rows on table: ", len(table))
body = table.find_all("tr")
head = body[0]
body_rows = body[2:]
# print(head)

headings = []
for item in head.contents:
    item = (item.text).rstrip("\n",)
    headings.append(item)

# print("OUTPUT\n", headings)

all_rows = []
for row_num in range(len(body_rows)):
    row = []
    for row_item in body_rows[row_num].find_all("td"):
        aa = re.sub("(\xa0)|(\n)|(\s)", "", row_item.text)
        row.append(aa)
    all_rows.append(row)

print("\n",all_rows)

# with open("chemk.csv", "r", newline='') as csvfile:
#     spamreader = csv.writer(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# df = pd.DataFrame({'data':all_rows, 'columns':headings})
# df.head()