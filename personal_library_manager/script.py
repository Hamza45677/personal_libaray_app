# import streamlit as st
# import json
# import os

# DATA_FILE = 'library.json'

# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, 'r') as f:
#             return json.load(f)
#     return []

# def save_data(books):
#     with open(DATA_FILE, 'w') as f:
#         json.dump(books, f, indent=4)

# def add_book():
#     print("\nAdd New Book")
#     book = {
#         'id': len(load_data()) + 1,
#         'title': input("Title: "),
#         'author': input("Author: "),
#         'year': input("Publication Year: "),
#         'genre': input("Genre: ")
#     }
#     books = load_data()
#     books.append(book)
#     save_data(books)
#     print("\nBook added successfully!")

# def list_books():
#     books = load_data()
#     print("\nBook List:")
#     print("-" * 50)
#     for book in books:
#         print(f"ID: {book['id']}")
#         print(f"Title: {book['title']}")
#         print(f"Author: {book['author']}")
#         print(f"Year: {book['year']}")
#         print(f"Genre: {book['genre']}")
#         print("-" * 50)

# def search_books():
#     print("\nSearch Books")
#     query = input("Search in title/author/genre: ").lower()
#     results = []
    
#     for book in load_data():
#         if (query in book['title'].lower() or 
#             query in book['author'].lower() or 
#             query in book['genre'].lower()):
#             results.append(book)
    
#     if results:
#         print(f"\nFound {len(results)} results:")
#         for book in results:
#             print(f"[{book['id']}] {book['title']} - {book['author']}")
#     else:
#         print("\nNo books found")

# def update_book():
#     book_id = int(input("\nEnter book ID to update: "))
#     books = load_data()
#     found = False
    
#     for book in books:
#         if book['id'] == book_id:
#             print("\nEnter new data (press Enter to keep current value):")
#             book['title'] = input(f"Title [{book['title']}]: ") or book['title']
#             book['author'] = input(f"Author [{book['author']}]: ") or book['author']
#             book['year'] = input(f"Year [{book['year']}]: ") or book['year']
#             book['genre'] = input(f"Genre [{book['genre']}]: ") or book['genre']
#             found = True
#             break
    
#     if found:
#         save_data(books)
#         print("\nBook updated successfully!")
#     else:
#         print("\nBook not found")

# def delete_book():
#     book_id = int(input("\nEnter book ID to delete: "))
#     books = load_data()
#     new_books = [book for book in books if book['id'] != book_id]
    
#     if len(new_books) != len(books):
#         save_data(new_books)
#         print("\nBook deleted successfully!")
#     else:
#         print("\nBook not found")

# def show_menu():
#     print("\n" + "="*30)
#     print("My Personal Library")
#     print("="*30)
#     print("1. View all books")
#     print("2. Add new book")
#     print("3. Search books")
#     print("4. Update book")
#     print("5. Delete book")
#     print("6. Exit")
#     print("="*30)

# def main():
#     while True:
#         show_menu()
#         choice = input("\nEnter your choice (1-6): ")
        
#         if choice == '1':
#             list_books()
#         elif choice == '2':
#             add_book()
#         elif choice == '3':
#             search_books()
#         elif choice == '4':
#             update_book()
#         elif choice == '5':
#             delete_book()
#         elif choice == '6':
#             print("\nThank you! Have a great day!")
#             break
#         else:
#             print("\nInvalid choice! Please choose 1-6")

#         input("\nPress Enter to continue...")

# if __name__ == "__main__":
#     main()

import streamlit as st
import json
import os

DATA_FILE = 'library.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def add_book():
    st.header("Add New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")

    if st.button("Add Book"):
        if title and author and year and genre:
            books = load_data()
            book = {
                'id': len(books) + 1,
                'title': title,
                'author': author,
                'year': year,
                'genre': genre
            }
            books.append(book)
            save_data(books)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields")

def list_books():
    books = load_data()
    st.header("Book List")
    if books:
        for book in books:
            st.subheader(f"ID: {book['id']} - {book['title']}")
            st.write(f"Author: {book['author']}")
            st.write(f"Year: {book['year']}")
            st.write(f"Genre: {book['genre']}")
            st.write("-" * 50)
    else:
        st.write("No books found")

def search_books():
    st.header("Search Books")
    query = st.text_input("Search in title/author/genre")
    
    if query:
        results = [book for book in load_data() if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query.lower() in book['genre'].lower()]
        
        if results:
            st.write(f"Found {len(results)} results:")
            for book in results:
                st.subheader(f"[{book['id']}] {book['title']} - {book['author']}")
        else:
            st.write("No books found")

def update_book():
    st.header("Update Book")
    book_id = st.number_input("Enter book ID to update", min_value=1)
    books = load_data()
    book = next((book for book in books if book['id'] == book_id), None)

    if book:
        title = st.text_input("Title", value=book['title'])
        author = st.text_input("Author", value=book['author'])
        year = st.text_input("Year", value=book['year'])
        genre = st.text_input("Genre", value=book['genre'])
        
        if st.button("Update Book"):
            book['title'] = title
            book['author'] = author
            book['year'] = year
            book['genre'] = genre
            save_data(books)
            st.success("Book updated successfully!")
    else:
        st.error("Book not found")

def delete_book():
    st.header("Delete Book")
    book_id = st.number_input("Enter book ID to delete", min_value=1)
    books = load_data()
    book = next((book for book in books if book['id'] == book_id), None)

    if book:
        if st.button("Delete Book"):
            books = [b for b in books if b['id'] != book_id]
            save_data(books)
            st.success("Book deleted successfully!")
    else:
        st.error("Book not found")

def show_menu():
    st.title("My Personal Library")
    st.write("-" * 30)

    choice = st.selectbox("Choose an action", ("View all books", "Add new book", "Search books", "Update book", "Delete book", "Exit"))

    if choice == "View all books":
        list_books()
    elif choice == "Add new book":
        add_book()
    elif choice == "Search books":
        search_books()
    elif choice == "Update book":
        update_book()
    elif choice == "Delete book":
        delete_book()
    elif choice == "Exit":
        st.write("Thank you! Have a great day!")
        st.stop()

def main():
    show_menu()

if __name__ == "__main__":
    main()
