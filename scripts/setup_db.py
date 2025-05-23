import sys
import os
from lib.db.connection import get_connection
from lib.db.seed import seed

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    with open(os.path.join(project_root, 'lib/db/schema.sql'), 'r') as schema_file:
        cursor.executescript(schema_file.read())
    conn.commit()
    seed(conn)
    conn.close()

if __name__ == "__main__":
    setup_db()