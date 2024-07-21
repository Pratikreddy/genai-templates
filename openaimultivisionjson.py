import base64
import requests

# OpenAI API Key
api_key = ""

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Paths to your images
image_paths = [
    "/Users/p/Desktop/work/ayotta/KTP - Muhammad Saefulloh.jpeg",
    "/Users/p/Desktop/work/ayotta/NPWP IRFAN AWALUDIN.jpg"
]

# Getting the base64 strings
base64_images = [encode_image(image_path) for image_path in image_paths]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Creating image content
image_contents = [
    {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
        }
    }
    for base64_image in base64_images
]

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What's in these images? Is there any difference between them? extract theyre data in jsons"
        },
        *image_contents
      ]
    }
  ],
  "max_tokens": 300,
  "temperature": 0.7,
  "response_format": {
    "type": "json_object"
  }
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
