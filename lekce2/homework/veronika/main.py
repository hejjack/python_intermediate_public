from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Function to search books
def search_books():
    query = search_entry.get().strip().lower()
    filter_by = filter_option.get()
    clear_table()
    filtered_books = [book for book in books if query in str(book[filter_by]).lower()]  # Filter books
    for book in filtered_books:
        book_table.insert("", "end", values=(book["title"], book["author"], book["type"], book["year"], book["genre"], book["ISBN"], book["copies_available"]))

# Function to clear the table
def clear_table():
    for item in book_table.get_children():
        book_table.delete(item)

# Hlavní seznam knih: název, autor, typ, rok vydání, žánr, počet dostupných kopií....

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "type": "Hardcover", "year": 1960, "genre": "Classic Fiction", "ISBN": "9780061120084", "copies_available": 4},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "type": "Audiobook", "year": 2006, "genre": "Classic Fiction","ISBN": "780061808128", "copies_available": 10},
    {"title": "1984", "author": "George Orwell", "type": "Paperback", "year": 1949, "genre": "Dystopian Fiction","ISBN": "9780451524935", "copies_available": 7},
    {"title": "1984", "author": "George Orwell", "type": "eBook", "year": 2013, "genre": "Dystopian Fiction","ISBN": "9780547249643", "copies_available": 15},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "type": "Hardcover", "year": 1813, "genre": "Classic Romance","ISBN": "9780141439518", "copies_available": 3},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "type": "eBook", "year": 2012, "genre": "Classic Romance","ISBN": "9781619491063", "copies_available": 20},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "type": "Paperback", "year": 1925, "genre": "Classic Fiction","ISBN": "9780743273565", "copies_available": 6},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "type": "Audiobook", "year": 2005, "genre": "Classic Fiction","ISBN": "9780743598247", "copies_available": 5},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "type": "Paperback", "year": 1951, "genre": "Classic Fiction","ISBN": "9780316769488", "copies_available": 2},
    {"title": "Moby-Dick", "author": "Herman Melville", "type": "Hardcover", "year": 1851, "genre": "Adventure Fiction","ISBN": "9780142437247","copies_available": 5},
    {"title": "Moby-Dick", "author": "Herman Melville", "type":"eBook", "year": 2009, "genre": "Adventure Fiction","ISBN": "9781593080181", "copies_available": 8},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "type": "Paperback", "year": 1937, "genre": "Fantasy","ISBN": "9780547928227", "copies_available": 8},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "type": "Audiobook", "year": 2001, "genre": "Fantasy","ISBN": "9780618346240", "copies_available": 3},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "type": "Hardcover", "year": 1997, "genre": "Fantasy","ISBN": "9780590353427", "copies_available": 12},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "type": "eBook", "year": 2015, "genre": "Fantasy","ISBN": "9781781102459", "copies_available": 30},
    {"title": "Brave New World", "author": "Aldous Huxley", "type": "Paperback", "year": 1932, "genre": "Dystopian Fiction","ISBN": "9780060850524", "copies_available": 4},
    {"title": "Brave New World", "author": "Aldous Huxley", "type": "Paperback", "year": 1925, "genre": "Dystopian Fiction","ISBN": "9780060850524", "copies_available": 7},
    {"title": "War and Peace", "author": "Leo Tolstoy", "type": "Hardcover", "year": 1869, "genre": "Historical Fiction","ISBN": "9780199232765", "copies_available": 1},
    {"title": "War and Peace", "author": "Leo Tolstoy", "type": "eBook", "year": 2009, "genre": "Historical Fiction","ISBN": "9780553213835", "copies_available": 12},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "type": "Paperback", "year": 1866, "genre": "Classic Fiction","ISBN": "9780143058144", "copies_available": 6},
    {"title": "The Odyssey", "author": "Homer", "type": "Hardcover", "year": -700, "genre": "Epic Poetry","ISBN": "9780140268867", "copies_available": 3},
    {"title": "The Odyssey", "author": "Homer", "type": "Audiobook", "year": 2007, "genre": "Epic Poetry","ISBN": "9780143059264", "copies_available": 5},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "type": "Paperback", "year": 1847, "genre": "Classic Romance","ISBN": "9780141441146", "copies_available": 4},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "type": "eBook", "year": 2015, "genre": "Classic Romance","ISBN": "9781509827794", "copies_available": 9},
    {"title": "Frankenstein", "author": "Mary Shelley", "type": "Paperback", "year": 1818, "genre": "Science Fiction","ISBN": "9780141439471", "copies_available": 5},
    {"title": "Frankenstein", "author": "Mary Shelley", "type": "Audiobook", "year": 2005, "genre": "Science Fiction","ISBN": "9780142429172", "copies_available": 2},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "type": "Hardcover", "year": 1954, "genre": "Fantasy","ISBN": "9780618640157", "copies_available": 2},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "type": "Audiobook", "year": 1990, "genre": "Fantasy","ISBN": "9780261102316", "copies_available": 4},
    {"title": "Dracula", "author": "Bram Stoker", "type": "Paperback", "year": 1897, "genre": "Horror","ISBN": "9781627936668", "copies_available": 12},
    {"title": "Dracula", "author": "Bram Stoker", "type": "eBook", "year": 2013, "genre": "Horror","ISBN": "9780385121675", "copies_available": 4},
    {"title": "The Shining", "author": "Stephen King", "type": "Hardcover", "year": 1977, "genre": "Classic Fiction","ISBN": "9780385121675", "copies_available": 4},
    {"title": "The Shining", "author": "Stephen King", "type": "eBook", "year": 2012, "genre": "Classic Fiction","ISBN": "9780385121675", "copies_available": 8},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "type": "Paperback", "year": 1988, "genre": "Science","ISBN": "9780553380163", "copies_available": 5},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "type": "Audiobook", "year": 2018, "genre": "Science","ISBN": "9781982109417", "copies_available": 10},
    {"title":"Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "type": "Paperback", "year": 2011, "genre": "Anthropology","ISBN": "9780062316097", "copies_available": 6},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "type": "eBook", "year": 2014, "genre": "Anthropology","ISBN": "9780062316097", "copies_available": 18},
    {"title": "The Road", "author": "Cormac McCarthy", "type": "Paperback", "year": 2006, "genre": "Post-Apocalyptic","ISBN": "9780307387899", "copies_available": 3},
    {"title": "The Road", "author": "Cormac McCarthy", "type": "Audiobook", "year": 2007, "genre": "Post-Apocalyptic","ISBN": "9780739343245", "copies_available": 5},
    {"title": "Becoming", "author": "Michelle Obama", "type": "Hardcover", "year": 2018, "genre": "Memoir","ISBN": "9781524763138", "copies_available": 12},
    {"title": "Becoming", "author": "Michelle Obama", "type": "eBook", "year": 2018, "genre": "Memoir","ISBN": "9781524763138", "copies_available": 25},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "type": "Paperback", "year": 2019, "genre": "Thriller","ISBN": "9781250301697", "copies_available": 8},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "type": "Audiobook", "year": 2019, "genre": "Thriller","ISBN": "9781250317544", "copies_available": 4},
]


# Create main application window
root = Tk()
root.title("Správa knihovny")
root.geometry("800x600")

# Load and display the background image
try:
    img = Image.open(r'C:\Users\pc\Pictures\Saved Pictures\Trinity-College-Library.jpg')
    img_resized = img.resize((800, 600))  # Resize image to cover the entire window
    bg_image = ImageTk.PhotoImage(img_resized)


    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the image to fill the entire window
except FileNotFoundError:
    bg_label = Label(root, text="Image not found!", font=("Arial", 30), fg="green")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)



# Add library name at the top
library_name = Label(root, text="Biblioteca", font=("Arial", 20, "bold"), bg="black", fg="white")
library_name.place(relx=0.5, y=5, anchor="n")  # Center horizontally



# Create search frame
search_frame = Frame(root, bg="green")
search_frame.place(x=50, y=100, width=700, height=50)



Label(search_frame, text="Hledat:", bg="green", fg="white").pack(side=LEFT, padx=5)
search_entry = Entry(search_frame)
search_entry.pack(side=LEFT, fill=X, expand=True, padx=5)



filter_option = StringVar(value="title")
filter_combo = ttk.Combobox(search_frame, textvariable=filter_option, values=["title", "author", "ISBN", "type", "year"], state="readonly")
filter_combo.pack(side=LEFT, padx=5)



Button(search_frame, text="Vyhledat", command=search_books).pack(side=LEFT, padx=5)


# Create table frame for displaying results
table_frame = Frame(root, bg="green")
table_frame.place(x=50, y=180, width=700, height=350)



columns = ("title", "author", "type", "year", "genre", "ISBN", "copies_available")
book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
book_table.pack(fill=BOTH, expand=True)




# Customize column headings
for col in columns:
    book_table.heading(col, text=col.upper() if col == "ISBN" else col.capitalize())
    book_table.column(col, width=100, anchor="center")  # Adjust column widths



# Start the application
root.mainloop()
