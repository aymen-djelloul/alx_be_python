def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    

    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item1 = str(input("enter the item add : "))
            shopping_list.append(item1)
            print(f"the item add : {item1}")
        elif choice == '2':
                item2 = str(input("enter the item remove : "))
                if item2 in shopping_list:
                    shopping_list.remove(item2)
                    print(f"the item removed : {item2}")
                else:
                    print(f"Item '{item2}' not found in the shopping list.")
            
        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
            
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()