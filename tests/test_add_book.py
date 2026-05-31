import sys
   sys.path.append('src')
   from book import add_book, Book

   def test_add_book():
       b = Book(1, 'Python入门', '张三')
       add_book(b)
       assert len(book_list) == 1