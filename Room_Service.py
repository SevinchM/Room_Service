#creating a function for the entire code.
def order_code():
    #importing the datetime module to select delivery time later in the code.
    import datetime
    #creating dictionaries for the rooms/people and the food codes/food.
    guest_list = {'01':'Mr.V','02':'Joy','03':'Khaliun','04':'Jenny','05':'Ulemj', '06':'Connie', '07':'Dari'}
    appetizers = {'101': 'Ceasar Salad', '102': 'Meat Platter', '103': 'Mini Quiche'}
    main_menu = {'201':'Filet Mignon', '202':'Chicken Quesadilla','203':'Mushroom Cream Soup'}
    dessserts = {'301': 'Ice Cream', '302':'Cheesecake', '303':'Fruit Platter'}
    beverages = {'A': 'Tea', 'B':'Coffee', 'C':'Juice'}

    #empty variables created to allow user input
    name = None
    room = None

    #creating an emoty order dictionary
    order = {}
    #user input for room and name of person staying and the validation of the input.
    #if incorrect input entered, the code asks again and again.
    while room not in guest_list.keys():
        room = input('Please enter your room number: ')
        if room in guest_list.keys():
            name = input('Enter your name: ')
            if guest_list[room] != name:
                print ('The name entered does not match the current records.')
                room = None
        else:
            print (f'Incorrect room number: {room}')
    #creating a function to order the food. one function for all food items to make the code shorter and simpler.
    def selection (food_type, food_dict):
        print (f'{food_type} menu')
        #code to translate the food codes to the actual food items from the dictionaries.
        for code, food in food_dict.items():
            print(code, '- - -', food)
        

        food_code = None
        #user input to select food items.
        while food_code not in food_dict.keys():
            food_code = input ("Enter the menu code: ")
            if food_code not in food_dict:
                print("Wrong menu code.")
            else:
                return {food_code: food_dict[food_code]}

    #incoking the function for each menu course and adding user choice into the order dictionary
    order.update(selection ('Appetizers', appetizers))
    print()
    order.update(selection ('Main Course', main_menu)) 
    print()
    order.update(selection ('Desserts', dessserts)) 
    print()
    order.update(selection ('Beverages', beverages))
    #selecting the delivery time using the proper format.
    validtime = False
    timeformat = "%H:%M"
    while not validtime:
        delivery_time = input("Please, enter delivery time (hh:mm): ")
        try:
            validtime = datetime.datetime.strptime(delivery_time, timeformat)
        except ValueError:
            print ('Time format hh:mm')
    #just printing the order  
    def print_order():
        print ('Your order')
        print ('----------')
        for code, food in order.items():
            print (code, '->', food)

        print('Your delivery time:', delivery_time)

    print()
    #printing the whole order so the user can check it.
    print_order()

    print("----------")

    place_order = ''
    #code to place or cancel the order
    while place_order.lower() not in ('yes', 'no'):
        place_order = input ('Would you like to place your order (yes/no)? ')

    if place_order == 'yes':
        print ('Your order is being processed.')
    else:
        print ('Your order has been cancelled.')

    print()
    new_order = ''

    #Code to book again if order was cancelled AND if it was processed but the user wants to book again.
    while new_order.lower() not in ('yes', 'no'):
        new_order = input ('Would you like to order again (yes/no)? ')

    if new_order == 'yes':
        order_code()
    else:
        print("Thank you for using our room service!")
#invoking the whole code.
order_code()