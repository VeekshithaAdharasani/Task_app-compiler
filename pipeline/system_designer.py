from schemas.design_schema import SystemDesign

def design_system(intent):

    entities = ["User"]

    pages = []

    if "login" in intent.features:
        pages.append("Login")

    if "dashboard" in intent.features:
        pages.append("Dashboard")

    if "contacts" in intent.features:
        pages.append("Contacts")
        entities.append("Contact")

    if "payments" in intent.features:
        entities.append("Subscription")

    if "analytics" in intent.features:
        pages.append("Analytics")

    return SystemDesign(
        entities=list(set(entities)),
        pages=pages,
        roles=intent.roles
    )