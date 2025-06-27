

class book:
    def __init__(self, title, firstName, lastName, publicationDate, pageCount):
        self.title: title
        self.authorFName: firstName
        self.authorLName: lastName
        self.publicationDate: publicationDate
        self.pageCount: pageCount

    def newBook(self):
        print("add a new book!")

    def updateBookInfo(self):
        print("updating book info")
        #will be able to work/manipulate table entries in the db
