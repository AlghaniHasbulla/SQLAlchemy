# tests/test_author.py

from lib.models.author import Author
from lib.models.article import Article
from lib.db.connection import get_connection  # ← Newly added import


def test_author_save():
    # Clean up any existing author with this name
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors WHERE name = ?", ("John Doe",))
    conn.commit()
    conn.close()

    author = Author(name="John Doe")
    author.save()

    assert author.id is not None


def test_author_articles():
    # Clean up and set up test data
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors WHERE name = ?", ("John Doe",))
    cursor.execute("INSERT OR IGNORE INTO magazines (id, name, category) VALUES (1, 'Tech Weekly', 'Technology')")
    conn.commit()

    author = Author(name="John Doe")
    author.save()

    article = Article(title="Test Article", author_id=author.id, magazine_id=1)
    article.save()

    assert len(author.articles()) > 0