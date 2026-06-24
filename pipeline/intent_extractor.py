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

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

        elif text.startswith("```"):
            text = text.replace(
                "```",
                ""
            ).strip()

        data = json.loads(text)

        return AppIntent(**data)

    except Exception as e:
        print("FALLBACK ACTIVATED")
        print("Gemini Error:", e)
        print("Using Fallback Extractor")

        prompt_lower = user_prompt.lower()

        features = []

        if "login" in prompt_lower:
            features.append("login")

        if "dashboard" in prompt_lower:
            features.append("dashboard")

        if "contact" in prompt_lower:
            features.append("contacts")

        if "payment" in prompt_lower:
            features.append("payments")

        if "analytics" in prompt_lower:
            features.append("analytics")

        roles = ["user"]

        if "admin" in prompt_lower:
            roles.append("admin")

        return AppIntent(
            app_type="CRM",
            features=features,
            roles=roles
        )