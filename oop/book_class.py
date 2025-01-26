class Book:
    # Constructor method (__init__)
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor method (__del__)
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation method (__str__)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation method (__repr__)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
