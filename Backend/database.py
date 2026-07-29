import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    """
    Creates and returns a new PostgreSQL connection.
    A new connection is created for each request,
    which avoids 'connection already closed' errors on Render/Neon.
    """
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )
    return conn