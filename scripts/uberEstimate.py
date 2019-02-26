import requests
import json



a = 51.52916347
b= -0.109970527
c=  51.53430039
d= -0.1680743
data = json.dumps({"start_latitude": a,"start_longitude": b,"end_latitude": c,"end_longitude": d})
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer <YOUR-TOKEN-HERE>'}
r = requests.post('https://api.uber.com/v1.2/requests/estimate', headers=headers, data=data)

print(r.json());
