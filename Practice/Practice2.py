

my_list = [1, 3, 4, 6, 9, 11, 23, 12]

new_list = list(filter(lambda x: (x%3 == 0) , my_list))

print(new_list)

# USING TERNARY OPERATOR
to_check = int(input('Give me a number: '))
msg = "Even" if to_check%2 == 0 else "Odd"
print(msg) 