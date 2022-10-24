import requests
import pandas as pd

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

req = requests.get(url="https://rsp.chemk.org/1korp/tomorrow.htm")
df = pd.concat(pd.read_html(req.content))
df.to_excel("1chemk.xlsx")
print(df)