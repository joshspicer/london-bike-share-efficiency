import requests
import json



a = 51.52916347
b= -0.109970527
c=  51.53430039
d= -0.1680743
data = json.dumps({"start_latitude": a,"start_longitude": b,"end_latitude": c,"end_longitude": d})
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAG8AAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAkAAAABwAAAAEAAAAEAAAAJIegrQTIBc2hzy3Ul4tpulsAAAAwcr9KXTjlBm5KTwTlTf8FTXUuLj38h-0gEDFkFDXj5n0peqKIwXn1DRpgYqk2lTOx5whJxaDAAZf307ZKTP4i0yViYzB5OxE-9hXzVvPYu-v6ATl2xTC2nLOyBQ6s0Du_J6PPvDuJ7zwvM4YDAAAAKLGvY7-oT_0OOgzCCQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU'}
r = requests.post('https://api.uber.com/v1.2/requests/estimate', headers=headers, data=data)

print(r.json());
