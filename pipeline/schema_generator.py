from schemas.ui_schema import UISchema, Page
from schemas.api_schema import APISchema, Endpoint
from schemas.db_schema import DBSchema, Table
from schemas.auth_schema import AuthSchema


ENTITY_COLUMNS = {
    "user": [
        "id",
        "name",
        "email"
    ],

    "doctor": [
        "id",
        "name",
        "specialization",
        "email"
    ],

    "patient": [
        "id",
        "name",
        "age",
        "phone"
    ],

    "appointment": [
        "id",
        "doctor_id",
        "patient_id",
        "appointment_date"
    ],

    "bill": [
        "id",
        "patient_id",
        "amount",
        "status"
    ],

    "service": [
        "id",
        "service_name",
        "price"
    ],

    "contact": [
        "id",
        "name",
        "email",
        "phone"
    ],

    "subscription": [
        "id",
        "plan_name",
        "price",
        "status"
    ]
}


def generate_schemas(design):

    ui = UISchema(
        pages=[
            Page(
                name=page,
                components=["Header", "Content"]
            )
            for page in design.pages
        ]
    )

    api_endpoints = []

    db_tables = []

    for entity in design.entities:

        table_name = entity.lower()

        columns = ENTITY_COLUMNS.get(
            table_name,
            ["id", "name"]
        )

        db_tables.append(
            Table(
                name=table_name,
                columns=columns
            )
        )

        api_endpoints.extend([
            Endpoint(
                path=f"/api/{table_name}",
                method="GET"
            ),
            Endpoint(
                path=f"/api/{table_name}",
                method="POST"
            ),
            Endpoint(
                path=f"/api/{table_name}/{{id}}",
                method="PUT"
            ),
            Endpoint(
                path=f"/api/{table_name}/{{id}}",
                method="DELETE"
            )
        ])

    api = APISchema(
        endpoints=api_endpoints
    )

    db = DBSchema(
        tables=db_tables
    )

    auth = AuthSchema(
        roles={
            role: ["read"]
            for role in design.roles
        }
    )

    return {
        "ui": ui,
        "api": api,
        "db": db,
        "auth": auth
    }