import random

with open("math_books.txt", "r") as f:
    books = list(f)
    length = len(books)
    random_book = random.randint(0, len(books))
    print(books[random_book])
