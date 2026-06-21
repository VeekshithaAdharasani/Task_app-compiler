from schemas.ui_schema import UISchema, Page
from schemas.api_schema import APISchema, Endpoint
from schemas.db_schema import DBSchema, Table
from schemas.auth_schema import AuthSchema


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

        db_tables.append(
            Table(
                name=table_name,
                columns=["id", "name"]
            )
        )

        api_endpoints.append(
            Endpoint(
                path=f"/api/{table_name}",
                method="GET"
            )
        )

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