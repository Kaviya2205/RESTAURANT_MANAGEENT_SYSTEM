class Menu:
    def __init__(self):
        self.items = {
            1: {"name": "Burger", "price": 150},
            2: {"name": "Pizza", "price": 300},
            3: {"name": "Pasta", "price": 200},
            4: {"name": "Coffee", "price": 100}
        }

    def display_menu(self):
        print("\nMENU:")
        for id, item in self.items.items():
            print(f"{id}. {item['name']} - ₹{item['price']}")

    def get_item(self, item_id):
        return self.items.get(item_id, None)
