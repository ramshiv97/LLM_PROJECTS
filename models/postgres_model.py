import psycopg2

# PostgreSQL Database Connection
def fetch_postgres_data(query):
    conn = psycopg2.connect(
        dbname="hybrid_db", user="username", password="password", host="localhost", port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    # Convert result to dictionary
    return [dict(zip([col[0] for col in cursor.description], row)) for row in rows]
