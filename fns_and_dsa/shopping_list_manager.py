def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # Remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"Item '{item}' not found in the list.")

        elif choice == '3':
            # View the current shopping list
            if shopping_list:
                print("Your shopping list:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

