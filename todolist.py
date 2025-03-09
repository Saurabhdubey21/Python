#make a to do list program in python
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_item(todo_list):
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def remove_item(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            item_number = int(input("Enter the number of the item to remove: "))
            if 1 <= item_number <= len(todo_list):
                removed_item = todo_list.pop(item_number - 1)
                print(f"'{removed_item}' has been removed from your to-do list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()