class BookService:
    def __init__(self, book_storage=None):
        self.book_storage = book_storage

    def addBook(self, book):
        return self.book_storage.add(book)

    def getAllBooks(self):
        return self.book_storage.giveAll()

    def searchForBook(self, id):
        if type(id) == int:
            if self.book_storage.searchById(id):
                return self.book_storage.searchById(id)
            else:
                return 'Not Found'
        else:
            return 'Wrong Id'

    def getAuthorSurname(self, id):
        if type(id) == int:
            if self.book_storage.searchById(id):
                foundBook = self.book_storage.searchById(id)
                return foundBook['author']['surname']
            else:
                return 'Not Found'
        else:
            return 'Wrong Id'

    def getTitle(self, id):
        if type(id) == int:
            if self.book_storage.searchById(id):
                foundBook = self.book_storage.searchById(id)
                return foundBook['title']
            else:
                return 'Not Found'
        else:
            return 'Wrong Id'