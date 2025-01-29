from menu import Menu

class Orders:
    def __init__(self):
        self.orders = []

    def take_order(self, menu):
        menu.display_menu()
        order_items = []
        while True:
            try:
                item_id = int(input("\nEnter item ID to order (0 to finish): "))
                if item_id == 0:
                    break
                item = menu.get_item(item_id)
                if item:
                    order_items.append(item)
                    print(f"Added {item['name']} to the order.")
                else:
                    print("Invalid item ID. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        if order_items:
            total_price = sum(item["price"] for item in order_items)
            self.orders.append({"items": order_items, "total": total_price})
            print(f"\nOrder placed successfully! Total Bill: ₹{total_price}")
        else:
            print("\nNo items were ordered.")
