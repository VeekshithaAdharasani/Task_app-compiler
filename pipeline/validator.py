def validate_schemas(design, schemas):

    errors = []

    ui = schemas["ui"]
    api = schemas["api"]
    db = schemas["db"]
    auth = schemas["auth"]

    # -----------------------
    # Rule 1
    # Every role in design must exist in auth
    # -----------------------

    for role in design.roles:
        if role not in auth.roles:
            errors.append(
                {
                    "type": "MISSING_ROLE",
                    "role": role
                }
            )

    # -----------------------
    # Rule 2
    # Every entity must have DB table
    # -----------------------

    db_tables = {
        table.name
        for table in db.tables
    }

    for entity in design.entities:

        table_name = entity.lower()

        if table_name not in db_tables:

            errors.append(
                {
                    "type": "MISSING_TABLE",
                    "table": table_name
                }
            )

    # -----------------------
    # Rule 3
    # Every entity must have API endpoint
    # -----------------------

    api_paths = {
        endpoint.path
        for endpoint in api.endpoints
    }

    for entity in design.entities:

        expected = f"/api/{entity.lower()}"

        if expected not in api_paths:

            errors.append(
                {
                    "type": "MISSING_ENDPOINT",
                    "endpoint": expected
                }
            )

    return errors