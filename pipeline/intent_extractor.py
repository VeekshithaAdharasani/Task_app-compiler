import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from schemas.app_schema import AppIntent

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_intent(user_prompt: str):

    prompt = f"""
Extract application requirements from the user request.

Return ONLY valid JSON.

Format:

{{
    "app_type": "",
    "features": [],
    "roles": []
}}

Rules:
- Identify the application type.
- Extract major features.
- Extract user roles.
- If roles are not specified, infer reasonable roles.

User Request:
{user_prompt}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    data = json.loads(text)

    return AppIntent(**data)