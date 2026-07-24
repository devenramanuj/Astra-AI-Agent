orders = []

def create_order(product, quantity, price):
    order_id = len(orders) + 1

    order = {
        "order_id": order_id,
        "product": product,
        "quantity": quantity,
        "total": quantity * price
    }

    orders.append(order)

    return order
