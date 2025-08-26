class Book:

    def __str__(self):
        return "The main Book class"

    def __init__(self, title: str, author: str, year: int, is_available: bool):
        self._title = title
        self._author = author
        self._year = year
        self._is_available = is_available

    @property
    def title(self):
        return self._title.capitalize()

    @title.setter
    def title(self, new_title: str):
        if not new_title.isalnum():
            raise TypeError("The title must be a valid string")
        self._title = new_title


book1 = Book("title1", "author1", 2000, True)
book1.title = "newTitle"
print(book1.title)
