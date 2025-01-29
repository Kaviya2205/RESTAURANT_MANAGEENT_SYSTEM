class Customers:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, contact):
        if contact in self.customers:
            print("Customer already exists.")
        else:
            self.customers[contact] = {"name": name, "orders": []}
            print(f"Customer {name} added successfully!")

    def get_customer(self, contact):
        return self.customers.get(contact, None)
