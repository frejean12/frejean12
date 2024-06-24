def calculator():
    while True:
        print("Select operation:" )
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Divide")
        print("5.Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                x = int(input("What's x? "))
                y = int(input("What's y? "))
            except ValueError:
                print("Invalid Input! Please enter an integer.")
                break

            if choice == '1':
                print(f"{x} + {y} = {x + y}")
            elif choice == '2':
                print(f"{x} - {y} = {x - y}")
            elif choice == '3':
                print(f"{x} * {y} = {x * y}")
            elif choice == '4':
                if y == 0:
                    print("Error! Division by 0")
                else:
                    print(f"{x} / {y} = {x / y}")

        elif choice == '5':
            print("Goodbye Calculator")
            break
        else:
            print("Invalid input! Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    calculator()
