books = ["Harry Potter", "Matilda", "The Jungle Book", "Charlotte's Web", "Wonder"]

print("Library Book List:", "Wonder")

print("Total Books:", len (books))
print("First Book:", books[0])
print("Last Book", books[-1])
print("First Three Books:", books[:3])

books.append("Diary of Wimpy Kid")
print("After Adding a Book:", books)

books.remove("The Jungle Book")
print("After removing Jungle Book:", books)

books.sort()
print("Bookks Sorted Alphabetically:", books)

books.reverse()
print("books in Reverse order:", books)

librarian = {"name": "Ms Priya", "section":"Children's books","experience":5}

print("Librarian Profile:", librarian)

print("Librarian name:", librarian["name"])
print("Library section:", librarian["section"])
print("Experience:", librarian["experience"])

librarian["experience"]=6
print("Updated Experience:", librarian)

librarian["email"] = "priya@schoollibrary.com"
print("After adding Email:", librarian)

librarian.pop("section")
print("After Removing a Section:", librarian)

book_ids = [101, 102, 103, 104, 105]
book_names = ["Matilda", "Wonder", "Harry Potter", "Charlotte's Web", "Diary of a Wimpy kid"]

book_directory = dict(zip(book_ids, book_names))

print("Book Directory: book_directory")




