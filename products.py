class Product:
    """Represents a single product in the store.
        Attributes:
            name (str): The name of the product.
            price (float): The price per unit.
            quantity (int): Units available in stock.
            active (bool): Whether the product is active (available for sale)."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a new product. Raises ValueError if input is invalid."""

        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Processes the purchase of a given quantity of the product.
        Reduces the product's available quantity and deactivates it if quantity reaches zero.
        Args:
            quantity (int): The number of units to purchase.
        Returns:
                float: The total price of the purchase (price * quantity).
        Raises:
                Exception: If the product is inactive or if the requested quantity
                is invalid (e.g., greater than available or non-positive)."""

        if not self.active:
            raise Exception(f"Product '{self.name}' is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception(f"Insufficient stock for '{self.name}'. Only {self.quantity} available.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price

