class Book:asldfkjlskdjflkajdf;lkjsdlfksjdflkjsdfj
    def __init__(self,id,name,author,edition):
        self.name=name
        self.author=author
        self.id=id
        self.edition=edition

    def getName(self):
        return self.name

    def getId(self):
        return self.id
    def getAuthor(self):
        return self.author
    def getEdition(self):
        return self.edition

book=Book("01","Romeo & Juliet","William Shakespear","3rd")
print("id is {} name is {} author is {} edition is {}".format(book.getId(),book.getName(),book.getAuthor(),book.getEdition()))

