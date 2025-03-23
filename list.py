# Create an empty list
my_list = []
print(f"my empty list: {my_list}")

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"this is my list after appending: {my_list}")

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print(f"this is my list after inserting: {my_list}")

# Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"this is my list after extending: {my_list}")

# Remove the last element
my_list.pop()
print(f"this is my list after popping: {my_list}")

# Sort the list in ascending order
my_list.sort()
print(f"this is my list after sorting: {my_list}")

# Find and print the index of the value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Print final list to verify
print("Final List:", my_list)

