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
ORDER_TOOL = {
    "name": "create_order",
    "description": "ગ્રાહક માટે નવો ઓર્ડર બનાવે છે.",
    "parameters": {
        "type": "object",
        "properties": {
            "product": {
                "type": "string"
            },
            "quantity": {
                "type": "integer"
            },
            "price": {
                "type": "number"
            }
        },
        "required": [
            "product",
            "quantity",
            "price"
        ]
    }
}
