

import datetime
from prettytable import PrettyTable


class Admin:
    def __init__(self):
        self.filepath = "data/admin.txt"

    
    def login(self):
        print("\n===== ADMIN LOGIN =====")
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open(self.filepath, "r") as f:
                for line in f:
                    data = dict(item.split(":") for item in line.strip().split(" | "))
                    if data["username"] == username and data["password"] == password:
                        print("Login successful\n")
                        self.admin_menu()
                        return
            print("Invalid admin credentials.")
        except FileNotFoundError:
            print("Admin file not found")

    
    def admin_menu(self):
        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Add Cloth Item")
            print("2. View All Clothes")
            print("3. Update Price")
            print("4. View Daily Report")
            print("5. View Logs")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_cloth()
            elif choice == '2':
                self.view_clothes()
            elif choice == '3':
                self.update_price()
            elif choice == '4':
                self.generate_daily_report()
            elif choice == '5':
                self.view_logs()
            elif choice == '6':
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice Try again.")

   
    def add_cloth(self):
        try:
            cid = input("Enter Cloth ID: ")
            name = input("Enter Cloth Name: ")
            base_price = int(input("Enter Base Price: "))
            stock = int(input("Enter Stock: "))

            price_S = base_price
            price_M = base_price + 50
            price_L = base_price + 100

            data = (
                f"id:{cid} | name:{name} | base_price:{base_price} | stock:{stock} "
                f"| price_S:{price_S} | price_M:{price_M} | price_L:{price_L}\n"
            )

            with open("data/clothes_table.txt", "a") as f:
                f.write(data)

            self.log_activity(f"Added cloth item: {name}")
            print("Cloth added successfully")

        except ValueError:
            print("Invalid Input")

   
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

            print("\n===== CLOTH LIST =====")
            print(table)

        except FileNotFoundError:
            print("Clothes file not found")

   
    def update_price(self):
        name = input("Enter cloth name to update price: ")

        try:
            with open("data/clothes_table.txt", "r") as f:
                lines = f.readlines()

            updated = False
            new_file = ""

            for line in lines:
                data = dict(item.split(":") for item in line.strip().split(" | "))

                if data["name"].lower() == name.lower():
                    new_price = int(input("Enter new base price: "))
                    data["base_price"] = str(new_price)
                    data["price_S"] = str(new_price)
                    data["price_M"] = str(new_price + 50)
                    data["price_L"] = str(new_price + 100)
                    updated = True
                    print("Price updated successfully")

                new_line = " | ".join([f"{k}:{v}" for k, v in data.items()])
                new_file += new_line + "\n"

            with open("data/clothes_table.txt", "w") as f:
                f.write(new_file)

            if updated:
                self.log_activity(f"Updated price for: {name}")
            else:
                print("Cloth not found.")

        except Exception as e:
            print("Error:", e)

    
    def generate_daily_report(self): 
        try:
            total_sales = 0
            transactions = 0

            table = PrettyTable()
            table.field_names = [
                "Sale ID", "User", "Item", "Size",
                "Price", "Quantity", "Total", "Date"
            ]

            with open("data/sales.txt", "r") as f:
                for line in f:
                    if ":" not in line:
                        continue

                    data = dict(item.split(":") for item in line.strip().split(" | "))

                    transactions += 1
                    total_sales += int(data["total"])

                    table.add_row([
                        data["sale_id"],
                        data["username"],
                        data["item"],
                        data["size"],
                        data["price"],
                        data["quantity"],
                        data["total"],
                        data["date"]
                    ])

            print("\n===== DAILY SALES REPORT =====")
            print(table)
            print(f"\nTotal Sales: ₹{total_sales}")
            print(f"Total Transactions: {transactions}")

            with open("data/daily_report.txt", "a") as f:
                f.write("\n" + str(datetime.date.today()) + "\n")
                f.write(str(table))
                f.write(f"\nTotal Sales: {total_sales}\n")
                f.write(f"Total Transactions: {transactions}\n\n")

            self.log_activity("Generated daily report")

        except FileNotFoundError:
            print("No sales data found")

   
    def view_logs(self):
        try:
            with open("data/logs.txt", "r") as f:
                table = PrettyTable()
                table.field_names = ["Timestamp", "Action"]

                for line in f:
                    timestamp, action = line.strip().split(" | ", 1)
                    table.add_row([timestamp, action])

            print("\n===== SYSTEM LOGS =====")
            print(table)

        except FileNotFoundError:
            print("No logs found")

    
    def log_activity(self, action):
        with open("data/logs.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} | {action}\n")
