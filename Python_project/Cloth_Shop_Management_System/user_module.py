

import datetime
from prettytable import PrettyTable

class User:
    def __init__(self):
        self.filepath = "data/users.txt"
        self.username = None


    def register(self):
        print("\n===== USER REGISTRATION =====")
        username = input("Enter username: ")
        password = input("Enter password: ")

        table = PrettyTable()
        table.field_names = ["username", "password", "balance"]
        table.add_row([username, password, 5000])

        with open(self.filepath, "a") as f:
            f.write(str(table))
            f.write("\n\n")

        print("Registration successful! Default balance ₹5000.")

    def login(self):
        print("\n--------- USER LOGIN ---------")
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open(self.filepath, "r") as f:
                lines = f.readlines()

            for line in lines:
                if line.startswith("+") or "username" in line or line.strip() == "":
                    continue

                cols = [c.strip() for c in line.split("|")[1:-1]]
                uname, pwd, balance = cols

                if uname == username and pwd == password:
                    self.username = username
                    print(f"Login successful! Welcome {username}")
                    self.user_menu()
                    return

            print("Invalid credentials.")

        except FileNotFoundError:
            print("User file not found.")

    def user_menu(self):
        while True:
            print("\n--------USER MENU------")
            print("1. View Clothes")
            print("2. Purchase Cloth")
            print("3. View Balance")
            print("4. View Purchase History")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.view_clothes()
            elif choice == '2':
                self.purchase_cloth()
            elif choice == '3':
                self.view_balance()
            elif choice == '4':
                self.view_purchase_history()
            elif choice == '5':
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice")

    
    def view_clothes(self):
        try:
            with open("data/clothes_table.txt", "r") as f:
                lines = f.readlines()

            table = PrettyTable()
            table.field_names = ["ID", "Name", "Base Price", "Stock", "Price S", "Price M", "Price L"]

            for line in lines:
                if ":" not in line:
                    continue

                data = dict(item.split(":") for item in line.strip().split(" | "))

                table.add_row([
                    data["id"], data["name"], data["base_price"], data["stock"],
                    data["price_S"], data["price_M"], data["price_L"]
                ])

            print("\n----------- AVAILABLE CLOTHES -----------")
            print(table)

        except FileNotFoundError:
            print("No clothes found!")

    
    def purchase_cloth(self):
        item = input("Enter cloth name: ")
        size = input("Enter size (S/M/L): ").upper()
        quantity = int(input("Enter quantity: "))

        try:
            with open("data/clothes_table.txt", "r") as f:
                lines = f.readlines()

            for line in lines:
                if ":" not in line:
                    continue

                data = dict(i.split(":") for i in line.strip().split(" | "))

                name = data["name"]

                if name.lower() == item.lower():

                    price = (
                        int(data["price_S"]) if size == "S" else
                        int(data["price_M"]) if size == "M" else
                        int(data["price_L"])
                    )

                    total_cost = price * quantity

                    if not self.update_balance(total_cost):
                        print("Insufficient balance!")
                        return

                    sale_data = (
                        f"sale_id:{int(datetime.datetime.now().timestamp())} | "
                        f"username:{self.username} | "
                        f"item:{item} | size:{size} | "
                        f"quantity:{quantity} | price:{price} | "
                        f"total:{total_cost} | date:{datetime.date.today()}\n"
                    )

                    with open("data/sales.txt", "a") as s:
                        s.write(sale_data)

                    print(f"Purchased {quantity} * {item} ({size}) for ₹{total_cost}")
                    return

            print("Cloth not found!")

        except Exception as e:
            print("Error during purchase:", e)

    
    def update_balance(self, amount):
        try:
            with open(self.filepath, "r") as f:
                lines = f.readlines()

            new_content = ""
            updated = False

            for line in lines:
                if line.startswith("+") or "username" in line or line.strip() == "":
                    new_content += line
                    continue

                cols = [c.strip() for c in line.split("|")[1:-1]]
                uname, pwd, bal = cols

                if uname == self.username:
                    bal = int(bal)
                    if bal < amount:
                        return False
                    bal -= amount
                    updated = True

                table = PrettyTable()
                table.field_names = ["username", "password", "balance"]
                table.add_row([uname, pwd, bal])

                new_content += str(table) + "\n\n"

            with open(self.filepath, "w") as f:
                f.write(new_content)

            return updated

        except FileNotFoundError:
            print("User file not found.")
            return False

    
    def view_balance(self):
        with open(self.filepath, "r") as f:
            # Print the balance in prettytable format
            lines = f.readlines()
            table = PrettyTable()
            table.field_names = ["username", "balance"]
            for line in lines:
                if line.startswith("+") or "username" in line or line.strip() == "":
                    continue

                cols = [c.strip() for c in line.split("|")[1:-1]]
                uname, pwd, bal = cols

                if uname == self.username:
                    table.add_row([uname, bal])
                    print("\n💰 Current Balance:")
                    print(table)
                    return


    
    def view_purchase_history(self):
        try:
            with open("data/sales.txt", "r") as f:
                print("\n===== PURCHASE HISTORY =====")
                # Print the data in prettytable format
                table = PrettyTable()
                table.field_names = ["sale_id", "username", "item", "size", "quantity", "price", "total", "date"]
                found = False
                for line in f:
                    data = dict(item.split(":") for item in line.strip().split(" | "))
                    if data["username"] == self.username:
                        table.add_row([
                            data["sale_id"], data["username"], data["item"], data["size"],
                            data["quantity"], data["price"], data["total"], data["date"]
                        ])
                        found = True
                if found:
                    print(table)
                else:
                    print("No purchase history found.")
                
        except:
            print("No purchase history found.")
