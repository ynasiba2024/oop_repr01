#1-masala
class Student:
    def __init__(self, fullname, grade):
        self.fullname = fullname
        self.grade = grade

    def __repr__(self):
        return f"{self.fullname} - {self.grade}-sinf o'quvchisi"


studen1 = Student("Ali Karimov", 9)
print(studen1)

#2-masala
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} kitobining muallifi: {self.author}"

k1 = Book("O'tkan kunlar", "Abdulla Qodririy")
print(k1)

#3-masala
class Telefon:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f"{self.brand} kompaniyasining {self.model} telefoni"

tel1 = Telefon("Samsung", "Galaxy A55")
print(tel1)

#4-masala
class Mashina:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"Rangi {self.color} bo'lgan avtomobil: {self.brand}"

m1 = Mashina("Chevrolet Cobalt", "oq")
print(m1)

#5-masala
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price =price

    def __repr__(self):
        return f"{self.name} mahsulotining narxi {self.price} so'm"

p1 = Product("Sichqoncha", 85000)
print(p1)
