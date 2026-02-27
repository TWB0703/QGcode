class BookException(Exception):
    pass


class BookNotFoundError(BookException):
    pass


class BookNotAvailableError(BookException):
    pass


class Book:
    def __init__(self, book_id, title, author, total=1):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__total = total
        self.__borrowed = 0

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def total(self):
        return self.__total

    @property
    def borrowed(self):
        return self.__borrowed

    @property
    def available(self):
        return self.__total - self.__borrowed

    def borrow(self):
        if self.available <= 0:
            raise BookNotAvailableError(self.__title)
        self.__borrowed += 1
        return True

    def return_book(self):
        if self.__borrowed <= 0:
            raise BookException(self.__title)
        self.__borrowed -= 1
        return True

    def add_copy(self, count=1):
        if count > 0:
            self.__total += count

    def __str__(self):
        return f"{self.__book_id} {self.__title} {self.__author} {self.available}/{self.__total}"


class EBook(Book):
    def __init__(self, book_id, title, author, file_size, format="PDF"):
        super().__init__(book_id, title, author, total=999)
        self.__file_size = file_size
        self.__format = format

    @property
    def file_size(self):
        return self.__file_size

    @property
    def format(self):
        return self.__format

    def borrow(self):
        self._Book__borrowed += 1
        return True

    def __str__(self):
        return f"[电子书] {super().__str__()} {self.__file_size}MB {self.__format}"


class Magazine(Book):
    def __init__(self, book_id, title, publisher, issue_no):
        super().__init__(book_id, title, publisher, total=5)
        self.__issue_no = issue_no

    @property
    def issue_no(self):
        return self.__issue_no

    def __str__(self):
        return f"[杂志] {super().__str__()} 第{self.__issue_no}期"


class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = {}

    @property
    def name(self):
        return self.__name

    def add_book(self, book):
        if book.book_id in self.__books:
            raise BookException(book.book_id)
        self.__books[book.book_id] = book
        print(book)

    def find_book(self, book_id):
        book = self.__books.get(book_id)
        if not book:
            raise BookNotFoundError(book_id)
        return book

    def borrow_book(self, book_id):
        try:
            book = self.find_book(book_id)
            book.borrow()
            print(book.title)
            return True
        except BookException as e:
            print(e)
            return False

    def return_book(self, book_id):
        try:
            book = self.find_book(book_id)
            book.return_book()
            print(book.title)
            return True
        except BookException as e:
            print(e)
            return False

    def show_all_books(self):
        print(self.__name)
        print()
        if not self.__books:
            print()
        else:
            for book in self.__books.values():
                print(book)
        print()

    def search_books(self, keyword):
        results = []
        for book in self.__books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    def get_statistics(self):
        total_books = len(self.__books)
        total_copies = sum(book.total for book in self.__books.values())
        total_borrowed = sum(book.borrowed for book in self.__books.values())

        return {
            "总品种": total_books,
            "总册数": total_copies,
            "已借出": total_borrowed,
            "可借阅": total_copies - total_borrowed
        }


def main():
    print("图书管理系统")
    print()

    library = Library("快乐书屋")

    try:
        book1 = Book("B001", "Python入门", "张三", 3)
        library.add_book(book1)

        book2 = Book("B002", "Java编程", "李四", 2)
        library.add_book(book2)

        ebook = EBook("E001", "Python高级编程", "王五", 5.2, "PDF")
        library.add_book(ebook)

        magazine = Magazine("M001", "电脑爱好者", "电子出版社", "2024-01")
        library.add_book(magazine)

    except BookException as e:
        print(e)

    library.show_all_books()

    print("借书演示")
    library.borrow_book("B001")
    library.borrow_book("B001")
    library.borrow_book("B001")
    library.borrow_book("B001")

    library.borrow_book("E001")
    library.borrow_book("E001")

    print()
    print("还书演示")
    library.return_book("B001")
    library.return_book("B001")

    print()
    print("搜索演示")
    keyword = "python"
    results = library.search_books(keyword)
    print(keyword)
    for book in results:
        print(book)

    print()
    print("统计信息")
    stats = library.get_statistics()
    for key, value in stats.items():
        print(key, value)

    print()
    print("异常处理演示")
    try:
        library.find_book("B999")
    except BookNotFoundError as e:
        print(e)

    try:
        library.return_book("B002")
    except BookException as e:
        print(e)


if __name__ == "__main__":
    main()