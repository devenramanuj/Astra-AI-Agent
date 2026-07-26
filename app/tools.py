def create_order(product: str, quantity: int, price: float) -> dict:

    print("DEBUG:", product, quantity, price)

    order = {
        "order_id": len(orders) + 1,
        "product": product,
        "quantity": quantity,
        "price": price,
        "total": quantity * price
    }

    orders.append(order)

    return order
