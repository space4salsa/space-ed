import psycopg2
import os
from dotenv import load_dotenv

#load_dotenv()
# Replace with your actual Neon connection string
#DATABASE_URL = os.getenv("DBURL")
DATABASE_URL = "postgresql://neondb_owner:npg_gqi6LfQUST9A@ep-restless-haze-a4cirnj7-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Quick execute function
def run_sql(sql, params=None):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            if sql.strip().upper().startswith('SELECT'):
                return cur.fetchall()
            else:
                conn.commit()
                return cur.rowcount

# Examples:
if __name__ == "__main__":
    # Select data
    check_db_table = run_sql("SELECT * FROM celestial_objects;")
    print("Users:", check_db_table)
    
    count = run_sql("SELECT COUNT(*) FROM celestial_objects;")