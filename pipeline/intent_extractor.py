from schemas.app_schema import AppIntent

def extract_intent(prompt: str):

    prompt = prompt.lower()

    features = []

    keywords = [
        "login",
        "dashboard",
        "contacts",
        "payments",
        "analytics"
    ]

    for keyword in keywords:
        if keyword in prompt:
            features.append(keyword)

    roles = ["user"]

    if "admin" in prompt:
        roles.append("admin")

    return AppIntent(
        app_type="CRM",
        features=features,
        roles=roles
    )