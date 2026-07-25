orders = []

def create_order(
    product: str,
    quantity: int,
    price: float
) -> dict:
    """
    Create a customer order.

    Args:
        product: Product name.
        quantity: Quantity ordered.
        price: Price per unit.
    """

    order = {
        "order_id": len(orders) + 1,
        "product": product,
        "quantity": quantity,
        "total": quantity * price
    }

    orders.append(order)

    return order    }
}
