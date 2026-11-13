import json
import os
import requests

url = os.environ["COURSE_MODEL_URL"]
model = os.environ["COURSE_MODEL_ID"]
prompt = "What is an HTTP request?"
# prompt = input("You: ")

payload = {
    "model": model,
    "messages": [{"role": "user", "content": prompt}],
}
response = requests.post(url, json=payload, timeout=120)
print("HTTP status:", response.status_code)
print("Response headers:")
print(json.dumps(dict(response.headers), indent=2))
print("Response body:")
try:
    body = response.json()
except requests.exceptions.JSONDecodeError:
    print(response.text)
    raise
print(json.dumps(body, indent=2))
with open("response.json", "w", encoding="utf-8") as handle:
    json.dump(body, handle, indent=2)
    handle.write("\n")
response.raise_for_status()
# print(body["choices"][0]["message"]["content"])
