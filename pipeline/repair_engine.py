from schemas.api_schema import Endpoint
from schemas.db_schema import Table


def repair_schemas(design, schemas, errors):

    api = schemas["api"]
    db = schemas["db"]
    auth = schemas["auth"]

    repairs = []

    for error in errors:

        if error["type"] == "MISSING_ENDPOINT":

            endpoint_path = error["endpoint"]

            api.endpoints.append(
                Endpoint(
                    path=endpoint_path,
                    method="GET"
                )
            )

            repairs.append(
                f"Added endpoint {endpoint_path}"
            )

        elif error["type"] == "MISSING_TABLE":

            table_name = error["table"]

            db.tables.append(
                Table(
                    name=table_name,
                    columns=["id", "name"]
                )
            )

            repairs.append(
                f"Added table {table_name}"
            )

        elif error["type"] == "MISSING_ROLE":

            role = error["role"]

            auth.roles[role] = ["read"]

            repairs.append(
                f"Added role {role}"
            )

    return schemas, repairs