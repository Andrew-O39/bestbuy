from products import Product # We import our Product class
from store import Store # We import our Store class

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

def start(store: Store):
    while True:
        print("\nStore Menu")
        print("-----------------------------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nAvailable Products:")
            print("-----------------------------------")
            for product in store.get_all_products():
                print(product.show())

        elif choice == '2':
            total = store.get_total_quantity()
            print(f"\nTotal items in store: {total}")

        elif choice == '3':
            print("\nEnter the number of the products you want to buy:")
            print("Type -1 to finish, and 0 to cancel the order.")
            print("----------------------------------------------------")
            products = store.get_all_products()
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")

            shopping_list = []
            while True:
                try:
                    prod_num = int(input("Product number (-1 to finish, 0 to cancel): "))
                    if prod_num == 0:
                        print("\nOrder canceled.")
                        shopping_list = []
                        break
                    elif prod_num == -1:
                        break
                    elif 1 <= prod_num <= len(products):
                        quantity = int(input("Quantity: "))
                        shopping_list.append((products[prod_num - 1], quantity))
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter valid numbers.")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"\nOrder placed successfully! Total cost: ${total_price}")
                except Exception as e:
                    print(f"Error placing order: {e}")

# Setup inventory and start
if __name__ == '__main__':
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)
    start(best_buy)