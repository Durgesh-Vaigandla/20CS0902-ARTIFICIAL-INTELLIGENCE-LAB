# Initial List
my_list = [1, 2, 3, 4, 5]

# Add an element at a specific index
index_to_add = 2
element_to_add = 10
my_list.insert(index_to_add, element_to_add)
print("List after Insert:", my_list)

# Append an element to the end of the list
element_to_append = 6
my_list.append(element_to_append)
print("List after Append:", my_list)

# Extend the list with another list
list_to_extend = [7, 8, 9]
my_list.extend(list_to_extend)
print("List after Extend:", my_list)

# Delete an element by value
element_to_delete = 3
if element_to_delete in my_list:
    my_list.remove(element_to_delete)
print("List after Remove:", my_list)

# Display the updated list
print("List after operations:", my_list)
