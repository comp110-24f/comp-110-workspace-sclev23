"""Practice with Classes."""


class Pizza:
    gluten_free: bool
    size: str
    num_toppings: int

    def __init__(self):
        orders.append(self)

    def price(self) -> float:
        price: float = 0
        if self.size == "small":
            price += 5.25
        else:
            price += 7.50
        price += self.num_toppings * 0.25
        if self.gluten_free is True:
            price += 1
        return price


orders: list[Pizza] = []
my_pizza: Pizza = Pizza()
my_pizza.gluten_free = False
my_pizza.size = "large"
my_pizza.num_toppings = 2
print(my_pizza.price())


def num_orders(given: list[Pizza]) -> int:
    return len(given)


print(num_orders(orders))
