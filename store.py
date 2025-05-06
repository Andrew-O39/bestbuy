from typing import List, Tuple
import products # We import our products module

class Store:
    """Represents a store containing a list of products.
        This class manages the store's inventory and provides methods to
        add or remove products, retrieve active products, calculate total
        stock quantity, and process orders.

        Attributes:
            products (List[Product]): The list of all Product instances in the store."""

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
        """ Processes a bulk order.
           Args:
               shopping_list (List[Tuple[Product, int]]): A list of (product, quantity) tuples.
           Returns:
               float: Total price of the order.
           Raises:
               Exception: If any product cannot fulfill the requested quantity."""


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

