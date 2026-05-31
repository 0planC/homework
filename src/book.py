class Book:
       def __init__(self, id, title, author):
           self.id = id
           self.title = title
           self.author = author

   book_list = []

   def add_book(book):
       book_list.append(book)
       print(f'图书《{book.title}》已添加')