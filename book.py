# create a class called book that stores a title, an author, and the
# number of pages
# write a method called describe_book() that prints a formatted summary
# of the book
# write a method called update_pages() that updates the page count.
# it should add 10 pages by default.
# it should also accept a custom number of pages to add


class Book:
    """store a title, an author, and the number of pages."""
    
    def __init__(self, title, author, pages):
        """store title, author, pages as attributes."""
        self.title = title
        self.author = author
        self.pages = pages
    

    def describe_book(self):
        """print a formatted summary of the book."""
        print(f"Title: {self.title.title()} - Author: {self.author.title()} - Pages: {self.pages}")
    

    def update_pages(self, pages=10):
        """takes a default of 10 pages and also updates the page count."""
        self.pages = pages