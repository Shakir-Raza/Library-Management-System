# import tkinter as tk
# from tkinter import messagebox
# from collections import deque
#
# # Library class
# class Library:
#     def __init__(self):
#         self.books = set()
#
#     def addbook(self, book):
#         self.books.add(book)
#
#     def deletebook(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             return True
#         return False
#
#     def displaybook(self):
#         return list(self.books)
#
#     def sorted_book(self):
#         return sorted(self.books)
#
#     def borrowbook(self, book):
#         return book in self.books
#
# # Queue class
# class Queue:
#     def __init__(self):
#         self.queue = deque()
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.popleft()
#         return None
#
#     def queue_display(self):
#         return list(self.queue)
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
# # TreeNode and BST class for future operations if needed (keeping them for completeness)
# class TreeNode:
#     def __init__(self, key):
#         self.right = None
#         self.left = None
#         self.val = key
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         if self.root is None:
#             self.root = TreeNode(key)
#         else:
#             self._insert(self.root, key)
#
#     def _insert(self, current, key):
#         if key < current.val:
#             if current.left is None:
#                 current.left = TreeNode(key)
#             else:
#                 self._insert(current.left, key)
#         elif key > current.val:
#             if current.right is None:
#                 current.right = TreeNode(key)
#             else:
#                 self._insert(current.right, key)
#
#     def searching(self, key):
#         return self._searching(self.root, key)
#
#     def _searching(self, current, key):
#         if current is None or current.val == key:
#             return current
#         elif key < current.val:
#             return self._searching(current.left, key)
#         else:
#             return self._searching(current.right, key)
#
#     def inorder_traversing(self):
#         return self._inorder_traversing(self.root, [])
#
#     def _inorder_traversing(self, current, result):
#         if current:
#             self._inorder_traversing(current.left, result)
#             result.append(current.val)
#             self._inorder_traversing(current.right, result)
#         return result
#
# # LibrarySystem class for operations
# class LibrarySystem:
#     def __init__(self):
#         self.library = Library()
#         self.waiting_users = Queue()
#         self.borrowed_books = []
#         self.users = {"Shakir": "123", "User": "User"}  # Hardcoded credentials for now
#
#         # Add initial books to library
#         for book in ["b1", "b2", "b3", "b4", "b5", "b6"]:
#             self.library.addbook(book)
#
#     # Function to validate login and load appropriate operations
#     def login(self, username, password):
#         if username in self.users and self.users[username] == password:
#             if username == "Shakir":
#                 return "librarian"
#             else:
#                 return "user"
#         else:
#             return None
#
#     def librarian_operations(self):
#         pass  # This will be linked to the librarian GUI operations
#
#     def user_operations(self):
#         pass  # This will be linked to the user GUI operations
#
# # GUI class to build the interface
# class LibraryGUI:
#     def __init__(self, root):
#         self.root = root
#         self.library_system = LibrarySystem()
#         self.root.title("Library Management System")
#         self.root.geometry("400x400")
#         self.login_screen()
#
#     # Clear the current window
#     def clear_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()
#
#     # Login screen
#     def login_screen(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Login", font=("Arial", 20)).pack(pady=10)
#
#         tk.Label(self.root, text="Username:").pack()
#         self.username_entry = tk.Entry(self.root)
#         self.username_entry.pack()
#
#         tk.Label(self.root, text="Password:").pack()
#         self.password_entry = tk.Entry(self.root, show="*")
#         self.password_entry.pack()
#
#         tk.Button(self.root, text="Login", command=self.validate_login).pack(pady=10)
#
#     # Validate login credentials
#     def validate_login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#
#         user_type = self.library_system.login(username, password)
#         if user_type == "librarian":
#             self.librarian_menu()
#         elif user_type == "user":
#             self.user_menu()
#         else:
#             messagebox.showerror("Error", "Invalid username or password!")
#
#     # Librarian menu
#     def librarian_menu(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Librarian Menu", font=("Arial", 20)).pack(pady=10)
#
#         tk.Button(self.root, text="Add Book", command=self.add_book_screen).pack(pady=5)
#         tk.Button(self.root, text="Delete Book", command=self.delete_book_screen).pack(pady=5)
#         tk.Button(self.root, text="Display Books", command=self.display_books).pack(pady=5)
#         tk.Button(self.root, text="Sorted Books", command=self.display_sorted_books).pack(pady=5)
#         tk.Button(self.root, text="Waiting Users", command=self.display_waiting_users).pack(pady=5)
#         tk.Button(self.root, text="Borrowed Books", command=self.display_borrowed_books).pack(pady=5)
#         tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)
#
#     # User menu
#     def user_menu(self):
#         self.clear_screen()
#         tk.Label(self.root, text="User Menu", font=("Arial", 20)).pack(pady=10)
#
#         tk.Button(self.root, text="Display Books", command=self.display_books).pack(pady=5)
#         tk.Button(self.root, text="Borrow Book", command=self.borrow_book_screen).pack(pady=5)
#         tk.Button(self.root, text="Return Book", command=self.return_book_screen).pack(pady=5)
#         tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)
#
#
#     # Add book screen (for librarian)
#     def add_book_screen(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Add Book", font=("Arial", 20)).pack(pady=10)
#         tk.Label(self.root, text="Book Name:").pack()
#         self.book_name_entry = tk.Entry(self.root)
#         self.book_name_entry.pack()
#         tk.Button(self.root, text="Add", command=self.add_book).pack(pady=5)
#         tk.Button(self.root, text="Back", command=self.librarian_menu).pack(pady=5)
#
#     def add_book(self):
#         book_name = self.book_name_entry.get()
#         self.library_system.library.addbook(book_name)
#         messagebox.showinfo("Success", f"Book '{book_name}' added!")
#         self.librarian_menu()
#
#     # Delete book screen (for librarian)
#     def delete_book_screen(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Delete Book", font=("Arial", 20)).pack(pady=10)
#         tk.Label(self.root, text="Book Name:").pack()
#         self.book_name_entry = tk.Entry(self.root)
#         self.book_name_entry.pack()
#         tk.Button(self.root, text="Delete", command=self.delete_book).pack(pady=5)
#         tk.Button(self.root, text="Back", command=self.librarian_menu).pack(pady=5)
#
#     def delete_book(self):
#         book_name = self.book_name_entry.get()
#         if self.library_system.library.deletebook(book_name):
#             messagebox.showinfo("Success", f"Book '{book_name}' deleted!")
#         else:
#             messagebox.showerror("Error", f"Book '{book_name}' not found!")
#         self.librarian_menu()
#
#     # Display books screen (common)
#     def display_books(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Books in Library", font=("Arial", 20)).pack(pady=10)
#         books = self.library_system.library.displaybook()
#         if books:
#             for book in books:
#                 tk.Label(self.root, text=book).pack()
#         else:
#             tk.Label(self.root, text="No books available").pack()
#         tk.Button(self.root, text="Back", command=self.librarian_menu).pack(pady=10)
#
#     # Display sorted books (librarian)
#     def display_sorted_books(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Sorted Books", font=("Arial", 20)).pack(pady=10)
#         sorted_books = self.library_system.library.sorted_book()
#         if sorted_books:
#             for book in sorted_books:
#                 tk.Label(self.root, text=book).pack()
#         else:
#             tk.Label(self.root, text="No books available").pack()
#         tk.Button(self.root, text="Back", command=self.librarian_menu).pack(pady=10)
#
#     # Borrow book screen (for user)
#     def borrow_book_screen(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Borrow Book", font=("Arial", 20)).pack(pady=10)
#         tk.Label(self.root, text="Book Name:").pack()
#         self.book_name_entry = tk.Entry(self.root)
#         self.book_name_entry.pack()
#         tk.Button(self.root, text="Borrow", command=self.borrow_book).pack(pady=5)
#         tk.Button(self.root, text="Back", command=self.user_menu).pack(pady=5)
#
#     def borrow_book(self):
#         book_name = self.book_name_entry.get()
#         if self.library_system.library.borrowbook(book_name):
#             self.library_system.library.deletebook(book_name)
#             self.library_system.borrowed_books.append(book_name)
#             messagebox.showinfo("Success", f"You borrowed '{book_name}'!")
#         else:
#             messagebox.showerror("Error", f"Book '{book_name}' not available!")
#         self.user_menu()
#
#     # Return book screen (for user)
#     def return_book_screen(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Return Book", font=("Arial", 20)).pack(pady=10)
#         tk.Label(self.root, text="Book Name:").pack()
#         self.book_name_entry = tk.Entry(self.root)
#         self.book_name_entry.pack()
#         tk.Button(self.root, text="Return", command=self.return_book).pack(pady=5)
#         tk.Button(self.root, text="Back", command=self.user_menu).pack(pady=5)
#
#     def return_book(self):
#         book_name = self.book_name_entry.get()
#         if book_name in self.library_system.borrowed_books:
#             self.library_system.borrowed_books.remove(book_name)
#             self.library_system.library.addbook(book_name)
#             messagebox.showinfo("Success", f"Book '{book_name}' returned!")
#         else:
#             messagebox.showerror("Error", f"Book '{book_name}' not found in borrowed books!")
#         self.user_menu()
#
#     # Display waiting users (librarian)
#     def display_waiting_users(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Waiting Users", font=("Arial", 20)).pack(pady=10)
#         waiting_users = self.library_system.waiting_users.queue_display()
#         if waiting_users:
#             for user in waiting_users:
#                 tk.Label(self.root, text=user).pack()
#         else:
#             tk.Label(self.root, text="No waiting users").pack()
#         tk.Button(self.root, text="Back", command=self.librarian_menu).pack(pady=10)
#
#     # Display borrowed books (common)
#     def display_borrowed_books(self):
#         self.clear_screen()
#         tk.Label(self.root, text="Borrowed Books", font=("Arial", 20)).pack(pady=10)
#         borrowed_books = self.library_system.borrowed_books
#         if borrowed_books:
#             for book in borrowed_books:
#                 tk.Label(self.root, text=book).pack()
#         else:
#             tk.Label(self.root, text="No borrowed books").pack()
#         tk.Button(self.root, text="Back", command=self.librarian_menu).pack(pady=10)
#
# # Main function to run the GUI
# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = LibraryGUI(root)
#     root.mainloop()
#
#
#
