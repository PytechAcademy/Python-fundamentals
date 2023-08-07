class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}"

# Creating instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book2 = Book("1984", "George Orwell", "Dystopian")

# Calling the method to display book information
info1 = book1.display_info()
info2 = book2.display_info()

# Displaying the book information
print("Book 1 Information:\n" + info1 + "\n")
print("Book 2 Information:\n" + info2)
