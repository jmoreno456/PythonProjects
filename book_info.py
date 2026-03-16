# in your main program, continually ask the user to enter book
# information: tile, author, number of pages
# after creating each book object, ask the user if they want to update
# the page
# store all book objects in a list
# after the user is done entering books, print a summary of all books


from book import Book

books = []

while True:
    print("Please enter all book information")


    title = input("What is the title of your chosen book? ")
    author = input("Who is the author of the book? ")
    pages = int(input("What is the number of pages in the book? "))


    book = Book(title, author, pages)
    books.append(book)


    update_page = input("Would you like to update the page count? (y/n): ").lower()
    if update_page == 'y':
        page = input("Enter the number of pages or press Enter if not updating pages: ")

        if page:
            book.update_pages(int(page))
        else:
            book.update_pages()
    
    add_another = input("Would you like to add another book? (y/n): ").lower()
    if add_another != 'y':
        break


# print book summary
print("\n----- Book Summary -----")
for book in books:
    book.describe_book()