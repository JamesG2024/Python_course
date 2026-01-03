if __name__ == '__main__':

    books = libary(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:  # string
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)  # converting string to integer

        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            books.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            books.returnBook(book)

        else:
            print("hot a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
        if  user_choice2 == "q":
            exit()

        elif  user_choice2 == "c":
            continue

            




