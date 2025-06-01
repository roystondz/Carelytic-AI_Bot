import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

import base64
image_path = "acne.jpg"
image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
image_file.close()

from groq import Groq
client = Groq()
model="meta-llama/llama-4-scout-17b-16e-instruct"
query = "IS THERE SOMETHING WRONG WITH ME"
messages=[
    {
        "role": "user",
        "content":[
            {
                "type":"text",
                "text":query
            },{
                "type":"image_url",
                "image_url":{
                    "url":f"data:image/jpeg;base64,{encoded_image}"
                },
            },
        ]
    }
]

chat_completeion = client.chat.completions.create(
    messages=messages,
    model=model,
)

print(chat_completeion)