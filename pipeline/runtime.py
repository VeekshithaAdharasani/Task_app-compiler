import sqlite3


def execute_db_schema(db_schema):

    conn = sqlite3.connect("generated_app.db")

    cursor = conn.cursor()

    created_tables = []

    for table in db_schema.tables:

        columns_sql = []

        for column in table.columns:

            if column == "id":
                columns_sql.append(
                    "id INTEGER PRIMARY KEY"
                )
            else:
                columns_sql.append(
                    f"{column} TEXT"
                )

        query = f"""
        CREATE TABLE IF NOT EXISTS {table.name} (
            {', '.join(columns_sql)}
        )
        """

        cursor.execute(query)

        created_tables.append(table.name)

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    existing_tables = [
        row[0]
        for row in cursor.fetchall()
    ]

    conn.commit()
    conn.close()

    return {
        "created": created_tables,
        "verified": existing_tables
    }