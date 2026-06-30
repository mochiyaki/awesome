import requests

endpoint_id = "YOUR_ENDPOINT_ID"
api_key = "YOUR_API_KEY"

response = requests.post(
    f"https://api.runpod.ai/v2/{endpoint_id}/runsync",
    headers={
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}",
    },
    json={
        "input": {
            "prompt": "A futuristic city skyline at sunset",
        }
    },
)

print(response.json())