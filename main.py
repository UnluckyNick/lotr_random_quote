import requests
import config

headers = {"Authorization": f"Bearer {config.api_key}"}

response = requests.get("https://the-one-api.dev/v2/quote", headers=headers)

print(response.json())