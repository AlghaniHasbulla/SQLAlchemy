# This script seeds the database with initial data for testing purposes.
def seed(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO authors (name) VALUES ('John Doe')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Magazine', 'Technology')")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Test Article', 1, 1)")
    conn.commit()