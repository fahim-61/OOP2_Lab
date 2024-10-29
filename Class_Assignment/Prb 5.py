# Initial data: books tuple and tags set
books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)

tags = {"classic", "dystopian", "novel", "literature"}

# Access the second book's author and print it
second_book_author = books[1][1]
print(f"Author of the second book: {second_book_author}")

# Add a new record for the book "Brave New World" by Aldous Huxley, published in 1932
# Tuples are immutable, so we create a new tuple by concatenating the old one with the new book
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print(f"Updated books tuple: {books}")

# Unpack the details of the third book and print them
title, author, year = books[2]
print(f"Third book details:\nTitle: {title}, Author: {author}, Year: {year}")

# Loop through the books tuple and print each book's title
print("Book Titles:")
for book in books:
    print(book[0])

# Add a new tag "sci-fi" to the tags set and print the updated set
tags.add("sci-fi")
print(f"Updated tags set: {tags}")

# Remove the tag "novel" from the tags set and print the updated set
tags.remove("novel")  # Use remove() as per task description
print(f"Tags set after removing 'novel': {tags}")
