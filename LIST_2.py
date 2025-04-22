# Get two lists as input from the user
list1 = input("Enter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()

# Find common elements using set intersection
common_elements = set(list1) & set(list2)

# Create a dictionary with common elements as keys and their length as values
common_dict = {item: len(item) for item in common_elements}

# Print the resulting dictionary
print("Common elements dictionary:", common_dict)

