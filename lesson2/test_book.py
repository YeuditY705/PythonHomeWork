# from lesson2.app.library import Library
# from lesson2.app.book import Book
import logging
import book
import library
import pytest
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

my_library = library.Library()

#בדיקה שהפונקציה מוסיפה ספר חדש לרשימת הספרים במערכת.
@pytest.mark.book
@pytest.mark.parametrize("title,author", [("רותי קפלר", "מסומן"), ("אסתר קוין", "תשע לפנות בוקר"),("","")])
def test_add_book(title, author):
    my_book = book.Book(title, author)
    assert my_library.add_book(my_book) == True

#בדיקה שהפונקציה מוסיפה משתמש חדש לרשימת המשתמשים.
@pytest.mark.user
def test_add_user():
    assert my_library.add_user("יהודית") == True


#בדיקה שהספר הושאל בהצלחה למשתמש רשום.
@pytest.mark.book
def test_check_out_book():
    my_book = book.Book("50 50", "דבורי רנד")
    my_library.add_user("אלישבע")
    my_library.check_out_book("אלישבע", my_book)
    assert my_book.is_checked_out == True


def test_return_book():
    my_book = book.Book("50 50", "דבורי רנד")
    my_library.add_book(my_book)
    my_library.add_user("אלישבע")
    my_library.check_out_book("אלישבע", my_book)
    my_library.return_book("אלישבע",my_book)
    assert my_book.is_checked_out == False

@pytest.mark.parametrize("title", ["bb", "b",  ""])
def test_search_book(title):
    my_book = book.Book("BB", "BB")
    my_book2 = book.Book("50 50", "AA")
    my_library.add_book(my_book)
    my_library.add_book(my_book2)
    assert my_library.search_books(title)
