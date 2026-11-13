import json
import os

import requests

FRUITS = {1: "apple", 2: "banana", 3: "cherry",
          4: "dragonfruit", 5: "elderberry"}

def get_fruit(number):
    return FRUITS.get(number, "unknown fruit")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_fruit",
            "description": "Look up the fruit assigned to an integer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {
                        "type": "integer"
                    }
                },
                "required": [
                    "number"
                ],
                "additionalProperties": false
            }
        }
    }
]


def dispatch(call):
    if call.get("type") != "function":
        return "Error: unsupported call type"
    function = call.get("function", {})
    if function.get("name") != "get_fruit":
        return "Error: unknown tool"
    try:
        args = json.loads(function.get("arguments", ""))
    except (json.JSONDecodeError, TypeError):
        return "Error: arguments must be JSON"
    if not isinstance(args, dict) or set(args) != {"number"}:
        return "Error: expected only number"
    if type(args["number"]) is not int:
        return "Error: number must be an integer"
    return get_fruit(args["number"])

url = os.environ["COURSE_MODEL_URL"]
model = os.environ["COURSE_MODEL_ID"]
messages = []

while True:
    prompt = input("You: ")
    if prompt.strip().lower() == "quit":
        break
    messages.append({"role": "user", "content": prompt})
    for _ in range(5):
        payload = {"model": model, "messages": messages}
        # TODO: Include TOOLS in the request.
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        message = response.json()["choices"][0]["message"]
        calls = message.get("tool_calls") or []
        if not calls:
            messages.append(message)
            print("AI:", message.get("content") or "")
            break
        # TODO: Validate call IDs, append the assistant message, then append
        # one correlated result per call using dispatch().
        raise NotImplementedError("Wire tool calls into the conversation")
    else:
        print("AI: This turn did not complete within five model requests.")
        break
