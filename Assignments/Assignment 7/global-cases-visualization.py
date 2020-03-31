# Alex Webber
#Done in collaboration with Nic Chiolerio and Collin Pounds

import requests
import json
import matplotlib.pyplot as plt

url = "https://covidapi.info/api/v1/global"

payload = {}
headers = {}
response = requests.request("GET", url, headers = headers, data = payload)

data = json.loads(response.text.encode('utf8'))

width = 0.35
deaths = data["result"]["deaths"]
recovered = data["result"]["recovered"]
confirmed = data["result"]["confirmed"] - deaths - recovered
                           
plt.bar("---", recovered, width, label="recovered")
plt.bar("---", deaths, width, label="deaths", bottom=recovered)
plt.bar("---", confirmed, width, label="cases", bottom=(deaths+recovered))

plt.legend()
plt.xlabel("Total Global Cases on " + data["date"])

plt.show()
