
import requests
import json
r = requests.get("https://www.thebluealliance.com/api/v3/events/2019/simple?X-TBA-Auth-Key=kbxvOnS2csBH6fzQ8zijLw2f1k135fWp8NgTEfPRg1n8hYqh7SSUo9VJ3JEBlnIg")
if r.status_code == 200:
  data_dict = json.loads(r.content)
  for e in data_dict:
    print("city:"+e["city"])
    print("country"+e["country"])
    print("date"+e["start_date"])
