# Alex Webber
#Done in collaboration with Nic Chiolerio and Collin Pounds

import requests
import json
import matplotlib.pyplot as plt

url = "https://covidapi.info/api/v1/country/USA"

payload = {}
headers = {}
response = requests.request("GET", url, headers = headers, data = payload)

data = json.loads(response.text.encode('utf8'))

deaths_plot_data = []

for date in data['result']:
    deaths_plot_data.append(data['result'][date]['deaths'])

plt.plot(deaths_plot_data)
plt.ylabel('Deaths from Coronavirus in US')
plt.xlabel('Days since first case (Jan 21)')
plt.show()
