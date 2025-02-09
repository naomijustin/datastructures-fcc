new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

numbers = []

numbers.append(2)
numbers.append(200)

// =====

numbers = []
numbers.extend([4, 5, 6])
numbers

// Prints:
[4, 5, 6]