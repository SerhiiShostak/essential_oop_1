class Book:

    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.review_list = []

    def __str__(self):
        if self.review_list:
            reviews = '\n '.join([str(r) for r in self.review_list])  
        else:
            reviews = 'Відгуків немає'
        return f'"{self.title}" \nАвтор: {self.author} ({self.year} р.) \nЖанр: {self.genre}\nВідгуки:\n {reviews}'
    
    def __repr__(self):
        return f'Book(title={self.title}, author={self.author}, year={self.year}, genre={self.genre})'
    
    def add_review(self, review):
        self.review_list.append(review)


class BookReview:

    def __init__(self, author: str, text: str, rating: int):
        self.author = author
        self.text = text
        self.rating = rating

    def __str__(self):
        return f'{self.author} (оцінка: {self.rating}): {self.text}'


book1 = Book("Воно", "Стівен Кінг", 1986, "Жахи")
book2 = Book("Керрі", "Стівен Кінг", 1974, "Містика")
book3 = Book("Квіти для Елджернона", "Деніел Кіз", 1966, "Роман")

review1 = BookReview("Валерій", "Це найкраща книга, яку я коли-небудь читав!", 5)
review2 = BookReview("Григорій", "Цікава, але трохи затягнута.", 4)
review3 = BookReview("Олександр", "Нудно.", 2)

book1.add_review(review1)
book1.add_review(review3)
book2.add_review(review2)

print(book1)
print()
print(book2)
print()
print(book3)


