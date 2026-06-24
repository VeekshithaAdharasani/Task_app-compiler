import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from schemas.design_schema import SystemDesign

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def design_system(intent):

    prompt = f"""
You are a software architect.

Given this application intent:

{intent.model_dump_json(indent=2)}

Return ONLY valid JSON.

Format:

{{
    "entities": [],
    "pages": [],
    "roles": []
}}

Rules:
- Generate business entities.
- Generate application pages.
- Preserve roles.
- Keep names concise.
"""

    try:

        response = model.generate_content(
            prompt
        )

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

        return SystemDesign(**data)
    
    except Exception:
        entities = ["User"]
        pages = []
        feature_text = " ".join(
            intent.features
        ).lower()
        
        if (
            "login" in feature_text
            or "authentication" in feature_text
        ):
            pages.append("Login")
        
        if "dashboard" in feature_text:
            pages.append("Dashboard")
        
        if "contact" in feature_text:
            pages.append("Contacts")
            entities.append("Contact")
        
        if (
            "payment" in feature_text
            or "subscription" in feature_text
            or "premium" in feature_text
        ):
            entities.append("Subscription")
            
        if "analytics" in feature_text:
            pages.append("Analytics")
        
        return SystemDesign(
            entities=list(set(entities)),
            pages=pages,
            roles=intent.roles
            )