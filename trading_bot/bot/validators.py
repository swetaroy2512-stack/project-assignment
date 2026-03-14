def validate_symbol(symbol):

    if len(symbol) < 6:
        raise ValueError("Invalid trading symbol")


def validate_side(side):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")


def validate_price(price, order_type):

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")