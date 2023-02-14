import os


def menu(books) -> None:
	os.system("cls")
	print_books(books)
	print("\nЧто будете делать?\n")
	options =[
		["Добавить книгу в библиотеку", lambda: add_book(books)],
		["Удалить книгу из библиотеки", lambda: delete_book(books)],
		["Найти книгу в библиотеке", lambda: book_search(books)],
		["Узнать более подробную информацию о книге", lambda: info_book(books)]
		]
	for num, option in enumerate(options, 1):
		print(f"{num}.{option[0]}")
	user_option = input("\nВведите номер варианта и нажмите ENTER: ")
	if not user_option.isdigit():
		print("Ошибка! Введены не коректные данные, ввод должен соответсвовать номеру варианта")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	idx = int(user_option) - 1
	if not idx < len(options):
		print("Ошибка! Введены не коректные данные, ввод должен соответсвовать номеру варианта")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	options[idx][1]()

def add_book(books: list) -> dict:
	name = input("Введите название книги: ")
	if not name:
		print("Ошибка! Не указано название.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	author = input("Введите автора книги: ")
	if not author:
		print("Ошибка! Не указан год.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	year = input("Введите год написания книги: ")
	if not year:
		print("Ошибка! Не указан год.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	if year.isdigit():
		year = str(year)
	else:
		print("Ошибка! Введён не коректный год.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	for num in range(len(books)):
		if books[num]["название"] == name and books[num]["автор"] == author and books[num]["год"] == year:
			print("\nТакая книга уже есть!")
			input("\nНажмите ENTER чтобы продолжить: ")
			return menu(books)
	book = {
	"название": name,
	"автор": author,
	"год": year 
	}
	books.append(book)
	return menu(books)

def book_search(books: list) -> None:
	filter = None
	options = [
		["Найти книгу по названию", "название"],
		["Найти книгу по автору", "автор"],
		["Найти книгу по году написания", "год"]
	]
	for num, option in enumerate(options, 1):
		print(f"{num}.{option[0]}")
	user_option = input("\nВведите номер варианта и нажмите ENTER: ")
	idx = int(user_option) - 1
	text = input(f"Введите {options[idx][1]} книги: ")
	if not text:
		print("Ошибка! Не коректно введёные данные.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	else:
		print("\nКниги подходящие под описание: ")
		for num, book in enumerate(books):
			if book[options[idx][1]] == text:
				num += 1
				print(f"{num}.{book['название']}")
		input("\nНажмите ENTER чтобы продолжить: ")
		return menu(books)

def info_book(books: list) -> None:
	num_book = input("Введите порядковый номер книги: ")
	if num_book.isdigit():
		num_book = int(num_book)
		if num_book > 0 and num_book <= len(books):
			num_book -= 1
		else:
			print("Ошибка! В библиотеке нет книги под данным порядковым номером.")
			input("Нажмите ENTER чтобы продолжить: ")
			return menu(books)
	else:
		print("Ошибка! Введён не коректный порядковый номер.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	print("\nНазвание книги:", books[num_book]["название"])
	print("Автор книги:", books[num_book]["автор"])
	print("Год написания книги:", books[num_book]["год"])
	input("\nНажмите ENTER чтобы продолжить: ")
	return menu(books)

def delete_book(books: list) -> None:
	num = input("Введите порядковый номер книги: ")
	if not num.isdigit():
		print("Ошибка! Введены не коректные данные, ввод должен соответсвовать номеру книги")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	idx = int(num) - 1
	if not idx < len(books):
		print("Ошибка! Введены не коректные данные, ввод должен соответсвовать номеру книги")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	if num >= 0 and num < len(books):
		books.pop(num)
	else:
		print("Нет такой книги")
		input("\nНажмите ENTER чтобы продолжить: ")
		return menu(books)

def print_books(books: list) -> None:
	print("Имеющиеся книги в библиотеке:\n")
	if not books:
		print("Пусто")
	else:
		for num, book in enumerate(books):
			num += 1
			print(f"{num}.{book['название']}")


books = []
menu(books)