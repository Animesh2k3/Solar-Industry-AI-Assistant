import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_image_with_openrouter(image_path):
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Read and encode image as base64
    with open(image_path, "rb") as img:
        image_data = img.read()

    encoded_image = base64.b64encode(image_data).decode()

    # Construct prompt for OpenRouter
    prompt = {
        "model": "qwen/qwen2.5-vl-32b-instruct:free",
        "messages": [
            {
                "role": "system",
                "content": "You're an expert in solar panel installation and analysis."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyze this rooftop image for solar panel installation. Return: 1) Solar potential (low/medium/high), 2) Estimated kW capacity, 3) Recommended panel type, 4) Estimated ROI years."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(api_url, headers=headers, json=prompt)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed: {response.status_code} - {response.text}")
