from agents import function_tool

# Fake database of orders
Orders = {
    123: {
        "order_id": 123,
        "customer_name": "John Doe",
        "items": ["item1", "item2"],
        "total_amount": 100.0
    },
    456: {
        "order_id": 456,
        "customer_name": "Jane Smith",
        "items": ["item3", "item4"],
        "total_amount": 150.0
    },
    789: {
        "order_id": 789,
        "customer_name": "Alice Johnson",
        "items": ["item5", "item6"],
        "total_amount": 200.0
    },
    101: {
        "order_id": 101,
        "customer_name": "Bob Brown",
        "items": ["item7", "item8"],
        "total_amount": 120.0
    },
}

# This function checks if the tool should be used
# It only returns True if the user message contains the word "order" or "orders"
def is_enabled(user_input):
    return "order" in user_input.lower() or "orders" in user_input.lower()

# This function handles errors
# Instead of crashing, it gives back a friendly error message
def error_function(error):
    return f"An error occurred: {error}"

# Tool function that fetches order details
# It takes an order_id and returns details if found, otherwise a "not found" message
@function_tool
async def get_order_details(order_id: int) -> str:
    try:
        # Look up the order in the Orders dictionary
        order = Orders.get(order_id)
        if not order:
            return f"No order found with ID {order_id}."
        
        # Create a nicely formatted string with order details
        order_details = (
            f"Order ID: {order['order_id']}\n"
            f"Customer Name: {order['customer_name']}\n"
            f"Items: {', '.join(order['items'])}\n"
            f"Total Amount: ${order['total_amount']:.2f}"
        )
        return order_details

    except Exception as e:
        # If something goes wrong, use the error_function to handle it
        return error_function(str(e))
