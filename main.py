import requests
import config
import json

headers = {"Authorization": f"Bearer {config.api_key}"}

response = requests.get("https://the-one-api.dev/v2/quote", headers=headers)

the_one_list = response.json()

#for key in the_one_list:{
#    print(key,":", the_one_list['docs'])
#}

dialog = the_one_list['docs'][0]['dialog']
print(f"dialog: {dialog}")