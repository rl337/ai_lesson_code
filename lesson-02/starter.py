import os
import requests

url = os.environ["COURSE_MODEL_URL"]
model = os.environ["COURSE_MODEL_ID"]

# Where should conversation history live?
while True:
    prompt = input("You: ")
    if prompt.strip().lower() == "quit":
        break
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    answer = response.json()["choices"][0]["message"]["content"]
    print("AI:", answer)
    # What should we retain from this exchange?
