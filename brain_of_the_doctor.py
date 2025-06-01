import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

import base64

def encode_image_to_base64(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")
    image_file.close()

from groq import Groq



def analyze_image_with_query(model, query,encoded_image):
    client = Groq()
    model = model
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
    
    return chat_completeion.choices[0].message.content

