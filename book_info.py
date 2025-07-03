import string



class Book:
    def __init__(self, title, firstName, lastName, publicationDate, pageCount):
        self.title = title
        self.authorFName = firstName
        self.authorLName = lastName
        self.publicationDate = publicationDate
        self.pageCount = pageCount

    def newBook(self):
        print("add a new book!")
        temp_new_book = input("Title: ")

    def full_name(self):
        print(f'{self.firstName} {self.lastName}')
    def updateBookInfo(self):
        print("updating book info")
        #will be able to work/manipulate table entries in the db

    title = input("Title: ")
    firstName = input("Author first name: ")
    lastName = input("Author last name: ")
    pageCount = input("Pages: ")
    publicationDate = input("Publication Date: ")

    print("Thank you we have received the book information!")
    print(f'{title}')
    print(f'{full_name()}')
    print(f'{pageCount}')
    print(f'{publicationDate}')





