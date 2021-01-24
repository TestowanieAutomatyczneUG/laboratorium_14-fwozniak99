from behave import *
from unittest.mock import *
import json
from src.sample.bookService import BookService
from src.sample.bookStorage import BookStorage


@step("że mamy atrapę bazy")
def step_impl(context):
    db = Mock( BookStorage() )

    db.searchById.return_value = {"title": "Ja, Ibra",
                                  "author": {"name": "Zlatan", "surname": "Ibrahimovic", "email": "abc123@onet.pl"},
                                  "ISBN": "3-221-3333-1332-0"}
    context.db = db
    context.books = BookService(context.db)


@step("podajemy id")
def step_impl(context):
    context.id = 0


@step("otrzymujemy książkę")
def step_impl(context):
    assert context.books.searchForBook(context.id) == {"title": "Ja, Ibra",
                                                       "author": {"name": "Zlatan", "surname": "Ibrahimovic",
                                                                  "email": "abc123@onet.pl"},
                                                       "ISBN": "3-221-3333-1332-0"}


@step("że mamy atrapę bazy zwracającą {book}")
def step_impl(context, book):
    db = Mock(BookStorage())
    db.searchById.return_value = json.loads(book)
    context.db = db
    context.books = BookService(context.db)


@step("podajemy {id}")
def step_impl(context, id):
    context.id = int(id)


@step("zwrócony tytuł książki powinien być {title}")
def step_impl(context, title):
    assert context.books.getTitle(context.id) == title


@step("we have a mocked database")
def step_impl(context):
    db = Mock(BookStorage())
    context.db = db
    context.books = BookService(context.db)


@step("books are to be retrieved")
def step_impl(context):
    context.db.giveAll.return_value = [
        {"title": "title1", "author": {"name": "name1", "email": "abc124@onet.pl", "surname": "wozniak"},
         "isbn": "1534554554"},
        {"title": "title2", "author": {"name": "name2", "email": "abc124@onet.pl", "surname": "hej"},
         "isbn": "1423423243"}]


@step("we can return all the books")
def step_impl(context):
    assert context.books.getAllBooks() == [
        {"title": "title1", "author": {"name": "name1", "email": "abc124@onet.pl", "surname": "wozniak"},
         "isbn": "1534554554"},
        {"title": "title2", "author": {"name": "name2", "email": "abc124@onet.pl", "surname": "hej"},
         "isbn": "1423423243"}
    ]


@step("we have a mocked db with mocked method returning {book}")
def step_impl(context, book):
    db = Mock(BookStorage())
    db.searchById.return_value = json.loads(book)
    context.db = db
    context.books = BookService(context.db)


@step("we have id equal to {id}")
def step_impl(context, id):
    context.id = int(id)


@step("returned second name should be equal to {surname}")
def step_impl(context, surname):
    assert context.books.getAuthorSurname(context.id) == surname
