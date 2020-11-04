from .. import models
import pytest


def test_object_created():
    bookObj = models.BookObject()
    assert bookObj.title == 'SomeObject'

def test_str_book_and_author():
    author=models.BookAuthor(title='NAME')
    book = models.BookObject(title='TEST', author=author)
    assert book.title == 'TEST'
    assert book.author.title == 'NAME'
    assert str(book) == 'TEST - NAME'
    assert str(author) == 'NAME'
