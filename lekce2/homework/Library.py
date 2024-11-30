import csv
from abc import ABC, abstractmethod

RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

class InvalidWordError(Exception):
    pass


class Library:
    def __init__(self,title,name):
        self.name = name
        self.title = title

    @staticmethod
    def inventory():
        descriptions = set()
        with open("data.csv", "r", newline="") as info_file:
            reader = csv.reader(info_file)
            question_book = input("Enter the name of the book. ")
            for row in reader:
                if row[0].lower() == question_book.lower():
                    description = row[7]
                    if description not in descriptions:
                        descriptions.add(description)
                        print(description)
            if not descriptions:
                print("Book not found in our library")
            question = input(f"{RED}Would you like to rent a book?\n"
                             f"'Y' for yes\n"
                             f"'N' for no\n"
                             f"'Q' to return tu main manu: {RESET}")
            if question.lower() == "Y".lower():
                Library.rent()
            elif question.lower() == "n".lower():
                Library.library_info()
            elif question.lower() == "Q".lower():
                main()

    @staticmethod
    def rent():
        with open("data.csv", "r", newline="") as rent_file:
            rent_reader = csv.reader(rent_file)
            data = list(rent_reader)
            headers = data[0]
            rows = data[1:]

            question = input("Enter the name of the book: ").strip()
            available_type = [row for row in rows if row[0].lower() == question.lower()]

            if not available_type:
                print("Book not found in our library.")
                return

            print(f"'{question}' formats available:")
            for row in available_type:
                print(f"{row[2]}: {row[6]} copies")

            if len(available_type) == 1:
                selected_format = available_type[0]
                confirm = input(
                    f"Would you like to rent a {selected_format[2]} copy of '{question}'? (Y/N): ").strip().lower()
                if confirm == "y":
                    available_copies = int(selected_format[6])
                    if available_copies > 0:
                        selected_format[6] = str(available_copies - 1)
                        print(f"You rented a {selected_format[2]} copy of '{question}'.")
                    else:
                        print(f"Sorry, no {selected_format[2]} copies are available.")
            else:
                format_choice = input(f"Which format would you like? {" or ".join([row[2] for row in available_type])}")
                for row in available_type:
                    if row[2].lower() == format_choice.lower():
                        available_copies = int(row[6])
                        if available_copies > 0:
                            row[6] = str(available_copies - 1)
                            print(f"You rented a {row[2]} copy of '{question}'.")
                        else:
                            print(f"Sorry, no {row[2]} copies are available.")
                        break
                else:
                    print(f"'{format_choice}' is not a valid format for '{question}'.")

        with open("data.csv", "w", newline="") as rent_file:
            writer = csv.writer(rent_file)
            writer.writerow(headers)
            writer.writerows(rows)

    @staticmethod
    def return_book():
        with open("data.csv", "r", newline="") as return_file:
            return_reader = csv.reader(return_file)
            data = list(return_reader)

        book_return = input("Enter the name of the book you want to return: ").strip()
        available_types = [row for row in data if row[0].lower() == book_return.lower()]

        if not available_types:
            print("Book was not rented in this library.")
            return

        if len(available_types) > 1:
            print("What type are you returning:")
            for index, row in enumerate(available_types, start=1):
                print(f"{index}. {row[2]}")

            try:
                choice = int(input("Enter the number corresponding to the format: ").strip())
                if choice < 1 or choice > len(available_types):
                    print("Invalid choice. Operation canceled.")
                    return
                selected_row = available_types[choice - 1]
            except ValueError:
                print("Invalid input. Operation canceled.")
                return
        else:
            selected_row = available_types[0]

        available = int(selected_row[6])
        original = int(selected_row[8])

        if available < original:
            selected_row[6] = str(available + 1)
            print(f"You returned a {selected_row[2]} copy of '{selected_row[0]}' by {selected_row[1]}.")
        else:
            print("All copies are already returned. No action needed.")

        with open("data.csv", "w", newline="") as return_file:
            writer = csv.writer(return_file)
            writer.writerows(data)


    @staticmethod
    def library_info():
        with open("data.csv", "r", newline="") as new_file:
            reader = csv.reader(new_file)

            question = input(f"{RED}To list whole inventory press enter.\n"
                             f"To list titles enter:'title',\n"
                             f"To list Authors enter: 'author',\n"
                             f"What would you like to search? {RESET} ").lower()
            next(reader)
            books = []
            authors = set()

            for row in reader:
                if question == "":
                    books.append(
                        f"{row[0]}: {row[3]} by {row[1]}. Genre: {row[4]}, {row[2]} copies available: {row[6]}")
                elif question == "title":
                    books.append(f"{row[0]} | {row[3]} | {row[2]}")
                elif question == "author":
                    authors.add(row[1])

            if question == "author":
                for author in authors:
                    print(author)

            else:
                for book in books:
                    print(book)

            question = input(f"{RED}To search again press 'Y'\n"
                             f"To return to main manu pres 'N'\n"
                             f"To read about a book press enter:{RESET} ")
            if question.lower() == "y".lower():
                Library.library_info()
            elif question.lower() == "n".lower():
                main()
            elif question.lower() == "":
                Library.inventory()
            else:
                print("Invalid input, returning to main page")
                main()

    @staticmethod
    def Faq():
        types = set()
        genres = set()

        with open("data.csv", "r", newline="") as faq_file:
            faq_reader = csv.reader(faq_file)
            next(faq_reader)
            for row in faq_reader:
                types.add(row[2])
                genres.add(row[4])

        questions = (
            "Q: What type of books do you have?",
            "Q: What genres do you have?",
            "Q: Can I rent more than one book?",
            "Q: How long can I rent the book(s) for?",
            "Q: Is there an overdue charge?"
        )
        answers = (
            f"{RED}A: {', '.join(types)}{RESET}",
            f"{RED}A: {', '.join(genres)}{RESET}",
            f"{RED}A: Yes, but they can't be the same book.{RESET}",
            f"{RED}A: 14 days.{RESET}",
            f"{RED}A: No, but you need to call and ask for an extension.{RESET}",
        )
        for question, answer in zip(questions, answers):
            print("-" * 40)
            print(question)
            print(answer)
            print()
        return main()

    @staticmethod
    def Validate_input(user_input, right_words):
        try:
            if user_input not in right_words:
                raise InvalidWordError(f"'{user_input}' is not a valid. Please try again")

        except InvalidWordError as e:
            print(e)
            return False


        return True




def main():
    password = "12345"
    right_words = ("I".lower(), "Rent".lower(), "Return".lower(), "FAQ".lower(), "Q".lower(), password)
    width = 40
    print("-" * width)
    print(f"|{'WELCOME TO VIRTUAL LIBRARY'.center(38)}|")
    print("-" * width)
    print()

    while True:
        try:
            welcome = input(f"{'What would you like to do?'.center(width)}\n"
                            f"{'-' * width}\n"
                            f"|     {YELLOW}To see our inventory hit 'I'{RESET}     |\n"
                            f"|     {YELLOW}To rent a book type 'Rent'{RESET}       |\n"
                            f"|     {YELLOW}To return a book type 'Return'{RESET}   |\n"
                            f"|     {YELLOW}For FAQ type 'FAQ'{RESET}               |\n"
                            f"|     {YELLOW}To leave hit 'Q.{RESET}                 |\n"
                            f"{'-' * width}\n").lower().strip()

            Library.Validate_input(welcome,right_words)


            if welcome.lower() == "I".lower():
                Library.library_info()
            elif welcome.lower() == "Rent".lower():
                Library.rent()
            elif welcome.lower() == "Return".lower():
                Library.return_book()
            elif welcome.lower() == "FAQ".lower():
                Library.Faq()
            elif welcome.lower() == "Q".lower():
                print("Thank you for visiting our library. Have a nice day.")
                break
            elif welcome.lower() == password:
                pass

        except InvalidWordError as e:
            print(e)

if __name__ == "__main__":
    main()

