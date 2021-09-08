#set of functions can be added
#class;defined patturn
#object;real world entity
#reference;operations#self instance keywordd method
class Book:
    library="nit library"
    def setval(self,bookname,author,pages):
        self.bookname=bookname
        self.author=author
        self.pages=pages
    def prints(self):
        print(self.bookname,self.author,self.pages)
        print(Book.library)
b=Book()
b.setval("benyamin","abg",67)
b.prints()