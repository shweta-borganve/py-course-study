# Problem 8: Nested Data Structure - Library System

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard

## Problem Description

Create a library management system using **nested dictionaries and lists**:

```python
library = {
    "fiction": [
        {"title": "1984", "author": "George Orwell", "copies": 3},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2}
    ],
    "science": [
        {"title": "A Brief History of Time", "author": "Stephen Hawking", "copies": 1}
    ]
}
```

The program should:
1. **Search** for a book by title
2. **Search** for books by author
3. **Search** for books by category
4. **Checkout** a book (decrease copies by 1)
5. **Return** a book (increase copies by 1)
6. **Show** all books in a category
7. Show books with **no copies** available

## Learning Goals
- Work with nested structures (dicts inside lists inside dicts)
- Loop through complex data
- Search and filter data
- Modify nested data structures

## Hints to Get Started
1. Define a dictionary with categories as keys
2. Each category has a list of book dictionaries
3. Each book has: title, author, copies
4. Loop through categories: `for category, books in library.items():`
5. Loop through books in each category: `for book in books:`
6. To find a book, loop and check if `book["title"] == search_title`
7. To checkout: find the book and do `book["copies"] -= 1` (if copies > 0)
8. To return: find the book and do `book["copies"] += 1`

## Example

**Search by Title:**
```
Input: Search for "1984"
Output: 
Found: "1984" by George Orwell (Category: fiction)
Available copies: 3
```

**Checkout a Book:**
```
Input: Checkout "The Great Gatsby"
Output:
You checked out "The Great Gatsby"
Remaining copies: 1
```

**Find Books with No Copies:**
```
Input: Show unavailable books
Output:
Unavailable books:
- "The Hobbit" by J.R.R. Tolkien (fiction)
```

**List Books by Category:**
```
Input: Show all books in "science"
Output:
Books in science:
1. "A Brief History of Time" by Stephen Hawking - 1 copy available
```

## Tips
- Use nested loops to access all data
- Remember `dict.items()` gives you both key and value
- Check `if book["copies"] > 0` before allowing checkout
- Use `.lower()` when searching to make it case-insensitive
- Print nicely formatted output

## Challenge (Optional)
1. Add a due date system - when you checkout, store when it's due back
2. Add a penalty system - if returned late, show a fine
3. Add an "Add Book" feature where users can add new books to the library
4. Track who checked out which book (keep a user list)
