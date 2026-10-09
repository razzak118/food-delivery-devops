def calculate_total(price, quantity):
    return price * quantity

def test_burger_order():
    assert calculate_total(120, 2) == 240

def test_pizza_order():
    assert calculate_total(250, 1) == 250

def test_quantity():
    assert calculate_total(100, 3) == 300
