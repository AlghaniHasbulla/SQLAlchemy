# lib/models/author.py

from lib.db.connection import get_connection


class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self._name = name  # underscore indicates internal use only

    @property
    def name(self):
        """Ensure name is retrieved from DB if not set (e.g., loaded author)"""
        if not self._name and self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM authors WHERE id = ?", (self.id,))
            result = cursor.fetchone()
            if result:
                self._name = result["name"]
        return self._name

    @name.setter
    def name(self, value):
        """Validates name assignment"""
        if hasattr(self, '_name') and self._name is not None:
            raise Exception("Author name cannot be changed after creation.")
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = value

    def save(self):
        """Saves author to the database and assigns ID."""
        if not self._name:
            raise ValueError("Author name must be set before saving.")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self.id:
                # Update existing author
                cursor.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self.name, self.id)
                )
            else:
                # Insert new author
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?)",
                    (self.name,)
                )
                self.id = cursor.lastrowid  # Set the generated ID
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, author_id):
        """Finds an author by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row["id"], name=row["name"])
        return None

    @classmethod
    def find_by_name(cls, name):
        """Finds an author by name."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row["id"], name=row["name"])
        return None

    def articles(self):
        """Returns all articles written by this author."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def magazines(self):
        """Returns all unique magazines this author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def add_article(self, magazine, title):
        """
        Creates and saves a new article for this author and given magazine.
        Returns the Article object.
        """
        from lib.models.article import Article

        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    def topic_areas(self):
        """Returns list of unique categories of magazines the author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [row["category"] for row in rows] if rows else None