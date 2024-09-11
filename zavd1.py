n = int(input("n = "))
print(f"Введіть {n} елементів масиву: ")

array = [int(input(f"Введіть елемент {i + 1}: ")) for i in range(n)]

positive_elements = [element for element in array if element > 0]

if positive_elements:
    max_element = max(positive_elements)
    print("Максимальний додатний елемент: ", max_element)
else:
    print("Немає додатних елементів")
