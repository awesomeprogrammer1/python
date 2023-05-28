'''
Create a class that describes a book review.
Add a field to the book class - a list of reviews.
Do so that when the book is displayed on the screen
using the print function, reviews of it will also be displayed.
'''

class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
    
    def book_reviews(self)

