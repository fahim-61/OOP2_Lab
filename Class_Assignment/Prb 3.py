#List
def manage_customers():
    # Initial list of customers
    customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

    # Access the third customer and print their name
    third_customer = customers[2]
    print(f"Third customer: {third_customer}")

    # Change the name of the second customer to "Ben"
    customers[1] = "Ben"

    # Add a new customer named "Frank" to the end of the list
    customers.append("Frank")

    # Remove the customer "David" from the list
    customers.remove("David")

    # Sort the customer names alphabetically
    customers.sort()

    # Print the final list of customers
    print(f"Final customer list: {customers}")


# Call the function to perform the operations
manage_customers()
