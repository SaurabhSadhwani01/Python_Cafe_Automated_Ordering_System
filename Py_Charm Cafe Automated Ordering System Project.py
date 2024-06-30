#Saurabh Sadhwani Assignment
#Biscotti Cafe Automated Ordering ( 1 Order at a time)


#class cafe with 2 functions : 1.For Opening Order ; 2.Closing Order
class Cafe:
    def __init__(self, menu):
        self.menu = menu
        self.tables = {i: Table(i) for i in range(1, 7)} # Initializing 6 Tables

    #Function for Opening Order and Checking if It's in the range of 1 to 6
    def open_order(self, table_number):
        if table_number in self.tables:
            print("\nBiscotti Cafe Menu : ")
            for item, price in self.menu.items():
                print(f"{item} : Rs.{price}")
            return self.tables[table_number]
        else:
            raise ValueError("\nInvalid Table Number, Please select a Table between 1 to 6.")

    #Function for Closing the Order and Calculating Final Bill
    def close_order(self, table_number):
        if table_number in self.tables:
            table = self.tables[table_number]
            bill = table.get_bill(self.menu)
            self.tables[table_number] = Table(table_number)
            return bill
        else:
            raise ValueError("\nInvalid Table Number, Please select a Table between 1 to 6.")

#class Table with 2 Functions : 1.To Add Orders ; 2.To Generate Calculated Bill
class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = {} #Dictionary to store order with food menu(key) and there quantity(value).

#Function to Add Order if it Exists in Menu
    def add_order(self, item, quantity, menu):
        if item in menu:
            if quantity > 0: #Edge Case : Quantity Cannot be in Negative i.e Burger -1 - Not Allowed
                if item in self.orders:
                    self.orders[item] += quantity
                else:
                    self.orders[item] = quantity
            else:
                raise ValueError("\nQuantity Cannot be in Negative.")
        else:
            raise ValueError(f"\nItem '{item}' is not on the menu. Please Select your Order from Menu.")

#Function to Gernerate Bill
    def get_bill(self, menu):
        total = 0
        bill_details = []
        for item, quantity in self.orders.items():
            if item in menu:
                item_total = menu[item] * quantity
                total += item_total
                bill_details.append(f"\n{item} x {quantity} = Rs.{item_total:.2f}")
            else:
                bill_details.append(f"{item} x {quantity} = Price not found")
        bill_details.append(f"Your Total Bill = Rs.{total:.2f}")
        return "\n".join(bill_details)


#Main Function strats Here :
def main():
    #Biscotti Cafe Menu
    menu = {
        'Coffee': 80,
        'Tea': 30,
        'Juice': 45,
        "Sandwich": 95,
        'Burger': 65,
        'Fries': 50,
        'Cake': 250
    }
    cafe = Cafe(menu)

    while True:
        print("\nWelcome to Biscotti Cafe!")
        choice = input("Enter table number between 1-6, or press 'q' to leave : ")

        if choice.lower() == 'q':
            print("\nThankyou for Visiting Biscotti Cafe. Have a Great Day!")
            break

        try:
            table_number = int(choice)
            table = cafe.open_order(table_number) #Order Opens

            while True:
                print("\nWhat would you like to order ? ")
                action = input("Enter your Order in the given format (item1 quantity, item2 quantity ) :")
                try:
                    orders = action.split(',') #Splitting input after ',' boundary using split()
                    for order in orders:
                        item, quantity = order.strip().split() #Also removing whitespaces using strip()
                        item = item.strip()
                        quantity = int(quantity.strip())

                        if item not in menu:
                            raise ValueError(f"\nItem '{item}' is not on the menu.")
                        table.add_order(item, quantity, menu)
                        print(f"Added {quantity} of {item} to Table {table_number} order.")

#Asking User Again if they want to Order :
                    while True:
                        next_action = input("\nWould you like to Order again (yes/no) ?").strip().lower()
                        if next_action == 'yes':
                            break #It they want to - we continue to ordering exiting this loop
                        elif next_action == 'no':
                            bill = cafe.close_order(table_number)
                            print(f"Bill for Table Number {table_number} is : {bill}")
                            print(f"Have a Great Day! Visit Again!")
                            break #If they do not want to we generate bill and say Bye and exit loop
                        else:
                            print("\nInvalid Input, Please Try Again (write in lower cases)")
                            continue

                    if next_action == 'no': #If without ordering they say no we say Bye and exit inner loop
                        break

#Except - if user does not enter order in expected format
                except ValueError as e:
                    print(e)

            print(f"\nClosing Table '{table_number}'.")

#Except - if table number is not in range of 1 to 6
        except ValueError:
            print("\nPlease enter a valid Table Number between 1 to 6 or press 'q' (in lower case) to quit. Thankyou!")

#Running on Main Functions script
if __name__ == "__main__":
    main()

#Scope in main function provided to add Multiple Ordering