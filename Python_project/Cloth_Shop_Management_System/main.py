from admin_module import Admin
from user_module import User

def main_menu():
    while True:
        print("\n===== CLOTH SHOP MANAGEMENT SYSTEM =====")
        print("1. Admin Login")
        
        print("2. User Login")
        print("3. User Registration")
        
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin = Admin()
            
            admin.login()
        elif choice == '2':
            
            user = User()
            user.login()
        elif choice == '3':
            user = User()
            
            
            user.register()
        elif choice == '4':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice Please try again.")

if __name__ == "__main__":
    main_menu()
