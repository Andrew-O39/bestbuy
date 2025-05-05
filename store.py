from typing import List, Tuple
import products # We import our products module

class Store:
    def __init__(self, products_list: List[products.Product] = None):
        self.products = products_list if products_list else []

    def add_product(self, product: products.Product):
        if not isinstance(product, products.Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: products.Product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"{product.name} not found in store")
            if not product.is_active():
                raise Exception(f"{product.name} is not active")
            if quantity > product.get_quantity():
                raise Exception(f"Not enough {product.name} in stock")
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

# Test block
if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    product_list = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(product_list[0], 1), (product_list[1], 2)]))