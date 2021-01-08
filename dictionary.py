# create new dictionary.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" are keys and numbers are values
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book
del phone_book ["John"]

print(phone_book["Jane"])





phone_book = {"John": 123, "Jane": 234, "Jerard": 345}  # create new dictionary
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 456
print(phone_book)

print(phone_book.keys())

print(phone_book.values())




grocery_list = ["fish", "tomato", "apples"]   # create new list

print("tomato" in grocery_list)    # check that grocery_list contains "tomato" item

grocery_dict = {"fish": 1, "tomato": 6, "apples": 3}   # create new dictionary

print("fish" in grocery_dict)
