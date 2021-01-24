class BookStorage:
    def __init__(self, data=[]):
        self.data = data

    def add(self, book):
        self.data.append(book)
        return True

    def searchById(self, id):
        return self.data[id]

    def giveAll(self):
        return self.data