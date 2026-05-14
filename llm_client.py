from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MY_API_KEY")
client = genai.Client(api_key=api_key)

def get_ai_response_stream(contents, config, model="gemini-3.1-flash-lite"):
    response_stream = client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=config
    )
    return response_stream