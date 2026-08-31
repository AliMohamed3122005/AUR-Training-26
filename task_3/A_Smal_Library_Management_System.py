from abc import ABC,abstractmethod
from enum import Enum


class Database:
    def __init__(self, filename):
        self.filename = filename
    def save(self,items):
        with open(self.filename,"w") as file:
            for item in items:
                item_type = item.__class__.__name__
                line = f"type={item_type}|title={item.title}"
                if item_type == "Book":
                    line += f"|author={item.author}|isbn={item.isbn}"
                elif item_type == "DVD":
                    line += f"|director={item.director}"

                elif item_type == "Magazine":
                    line += f"|issue={item.issue}"
                file.write(line + "\n")
    def load(self):
        items = []

        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                data = {}

                parts = line.split("|")

                for part in parts:
                    key, value = part.split("=")
                    data[key] = value

                item = LibraryItem.from_dict(data)
                items.append(item)

        return items


class ItemStatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"

class Library:
    def __init__(self):
        self.items = []
    def add_items(self,item):
        self.items.append(item)
    def checkout(self,title):
        for item in self.items:
            if item.title == title:
                item.checkout()
                return
        raise ValueError("Not found")
    def return_item(self, title):
        for item in self.items:
            if item.title == title:
                item.return_item()
                return
        raise ValueError("Not found")
    def find_by_title(self, title):
        for item in self.items:
            if item.title == title:
                return item
        return None
    def list_available(self):
        return [items for items in self.items if items.status == ItemStatus.AVAILABLE]







class LibraryItem(ABC):
    def __init__(self,title):
        self.title=title
        self._status = ItemStatus.AVAILABLE
    @abstractmethod
    def loan_period(self):
        ...
    def checkout(self):
        if self._status != ItemStatus.AVAILABLE:
            raise ValueError("Item is not available")
        else:
            self._status=ItemStatus.CHECKED_OUT
    def return_item(self):
        if self._status != ItemStatus.CHECKED_OUT:
            raise ValueError("Item is already here or lost")
        else:
            self._status=ItemStatus.AVAILABLE
    def mark_lost(self):
        if self._status==ItemStatus.LOST:
            raise ValueError("Item is already Lost!")
        else:
            self._status=ItemStatus.LOST
    @property
    def status(self):
        return self._status
    def __str__(self):
        return f"{self.title}({self.__class__.__name__})-{self.status.value}"
    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}')"
    def __lt__(self,other):
        return self.title < other.title
    @classmethod
    def from_dict(cls,data):
        items_types = {
            "Book":Book,
            "DVD":DVD,
            "Magazine":Magazine
        }
        items_class = items_types[data["type"]]
        return items_class.from_dict(data)


class Book(LibraryItem):
    def __init__(self, title,author,isbn):
        super().__init__(title)
        self.author=author
        self.isbn=isbn
    def loan_period(self):
        return 21
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"]
        )
    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) != 13:
            return False
        if not isbn.isdigit():
            return False

class DVD(LibraryItem):
    def __init__(self, title,director):
        super().__init__(title)       
        self.director = director 
    def loan_period(self):
        return 5
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["title"],
            data["director"]
        )

class Magazine(LibraryItem):
    def __init__(self, title,issue):
        super().__init__(title)     
        self.issue = issue 
    def loan_period(self):
        return 14
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["title"],
            data["issue"]
        )


db = Database("database.txt")

book = Book("Dune", "Frank Herbert", "9780441013593")
##dvd = DVD()
##magazine = Magazine()

print(book.loan_period())
print(book.title)
print(book.status)
book.checkout()
print(book.status)
book.return_item()
print(book.status)
book.mark_lost()
print(book.status)
print(book)
print([book])
book1 = Book("Dune", "Frank Herbert", "9780441013593")
book2 = Book("Inception", "Someone", "123456789")
book3 = Book("Atomic Habits", "James Clear", "123456789")
items =[ book1,book2,book3]
print(sorted(items))
data = {
    "title": "Dune",
    "author": "Frank Herbert",
    "isbn": "9780441013593"
}




print("\n TEST CASES ARE FROM CHATGPT TO MAKE IT EASIER FOR YOU TO TEST MY CODE (ALI) ")

print("\n========== TEST 1: Create Items ==========")

book = Book("Dune", "Frank Herbert", "9780441013593")
dvd = DVD("Inception", "Christopher Nolan")
magazine = Magazine("National Geographic", "2026-08")

print(book)
print(dvd)
print(magazine)


print("\n========== TEST 2: Loan Period ==========")

print("Book:", book.loan_period())
print("DVD:", dvd.loan_period())
print("Magazine:", magazine.loan_period())


print("\n========== TEST 3: Initial Status ==========")

print(book.status)
print(dvd.status)
print(magazine.status)


print("\n========== TEST 4: Checkout ==========")

book = Book("Dune", "Frank Herbert", "9780441013593")

print("Before:", book.status)

book.checkout()

print("After:", book.status)

try:
    book.checkout()
except ValueError as e:
    print("Error caught:", e)


print("\n========== TEST 5: Return Item ==========")

book = Book("Dune", "Frank Herbert", "9780441013593")

book.checkout()
print("After checkout:", book.status)

book.return_item()
print("After return:", book.status)

try:
    book.return_item()
except ValueError as e:
    print("Error caught:", e)


print("\n========== TEST 6: Mark Lost ==========")

book = Book("Dune", "Frank Herbert", "9780441013593")

print("Before:", book.status)

book.mark_lost()

print("After:", book.status)

try:
    book.mark_lost()
except ValueError as e:
    print("Error caught:", e)


print("\n========== TEST 7: __str__ ==========")

book = Book("Dune", "Frank Herbert", "9780441013593")

print(book)


print("\n========== TEST 8: __repr__ ==========")

book = Book("Dune", "Frank Herbert", "9780441013593")

print(repr(book))
print([book])


print("\n========== TEST 9: __lt__ / Sorting ==========")

book1 = Book("Dune", "Frank Herbert", "9780441013593")
book2 = Book("Inception", "Christopher Nolan", "123456789")
book3 = Book("Atomic Habits", "James Clear", "987654321")

items = [book1, book2, book3]

print("Before:")
print(items)

print("After:")
print(sorted(items))


print("\n========== TEST 10: Book.from_dict ==========")

data = {
    "title": "Dune",
    "author": "Frank Herbert",
    "isbn": "9780441013593"
}

book = Book.from_dict(data)

print(book)
print(book.title)
print(book.author)
print(book.isbn)


print("\n========== TEST 11: DVD.from_dict ==========")

data = {
    "title": "Inception",
    "director": "Christopher Nolan"
}

dvd = DVD.from_dict(data)

print(dvd)
print(dvd.title)
print(dvd.director)


print("\n========== TEST 12: Magazine.from_dict ==========")

data = {
    "title": "National Geographic",
    "issue": "2026-08"
}

magazine = Magazine.from_dict(data)

print(magazine)
print(magazine.title)
print(magazine.issue)


print("\n========== TEST 13: Library.add_items ==========")

library = Library()

book = Book("Dune", "Frank Herbert", "9780441013593")
dvd = DVD("Inception", "Christopher Nolan")
magazine = Magazine("National Geographic", "2026-08")

library.add_items(book)
library.add_items(dvd)
library.add_items(magazine)

print(library.items)


print("\n========== TEST 14: Library.find_by_title ==========")

print(library.find_by_title("Dune"))
print(library.find_by_title("Nothing"))


print("\n========== TEST 15: Library.checkout ==========")

book = library.find_by_title("Dune")

print("Before:", book.status)

library.checkout("Dune")

print("After:", book.status)


print("\n========== TEST 16: Library.return_item ==========")

library.return_item("Dune")

print("After return:", book.status)


print("\n========== TEST 17: Library.list_available ==========")

print(library.list_available())


print("\n========== TEST 18: Database.save ==========")

db = Database("database.txt")

db.save(library.items)

print("Saved successfully.")


print("\n========== TEST 19: Database.load ==========")

loaded_items = db.load()

print(loaded_items)


print("\n========== TEST 20: Loaded Items ==========")

for item in loaded_items:
    print(item)


print("\n========== ALL TESTS FINISHED ==========")