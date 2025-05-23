import pytest
from lib.models.author import Author

def test_author_save():
    author = Author(name="John Doe")
    author.save()
    assert Author.find_by_name("John Doe") is not None

def test_author_articles():
    author = Author.find_by_name("John Doe")
    article = Article(title="Test Article", author_id=author.id, magazine_id=1)
    article.save()
    assert len(author.articles()) > 0