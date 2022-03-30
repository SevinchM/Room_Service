appetizers = {'101': 'Ceasar Salad', '102': 'Meat Platter', '103': 'Mini Quiche'}

print ('Appetizer menu')
print ('----------------')
for code, food in appetizers.items():
    print(code, '-', food)

user_choice = input("Select one item from the menu: ")

match user_choice:
    case '101'|'102'|'103':
        print('You have chosen the ', appetizers[user_choice])
    case _:
        print('Wrong appetizer code.')