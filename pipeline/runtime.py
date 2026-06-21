import sqlite3


def execute_db_schema(db_schema):

    conn = sqlite3.connect("generated_app.db")

    cursor = conn.cursor()

    created_tables = []

    for table in db_schema.tables:

        query = f"""
        CREATE TABLE IF NOT EXISTS {table.name} (
            id INTEGER PRIMARY KEY,
            name TEXT
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