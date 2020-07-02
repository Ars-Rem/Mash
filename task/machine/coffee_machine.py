'''print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')
'''
'''
# ingredients


cups = int(input('Write how many cups of coffee you will need:'))

milk = 50
water = 200
coffee = 15

print('For', cups, ' cups of coffee you will need:')
milk_all = milk * cups
water_all = water * cups
cups_all = coffee * cups

print(water_all, 'ml of water')
print(milk_all, 'ml of milk')
print(cups_all, 'g of coffee beans')
'''

'''
# 3/4

# cups
# начало блока !!!!!!!!! промежуточные переменные для тестов!!!!!! удалить!!
milk = 50
water = 200
coffee = 15
#конец блока


water_input = int(input('Write how many ml of water the coffee machine has:'))
milk_input = int(input('Write how many ml of milk the coffee machine has:'))
coffee_input = int(input('Write how many grams of coffee beans the coffee machine has:'))
cups_input = int(input('Write how many cups your need:'))

water_cups = (water_input // water)
# print(water_cups)
milk_cups = (milk_input // milk)
# print(milk_cups)
coffee_cups = (coffee_input // coffee)
# print(coffee_cups)
# минимальное количество кружек из всех ингридиентов min_cups
min_cups = min(water_cups, milk_cups, coffee_cups)
if cups_input == min_cups:
    print('Yes, I can make that amount of coffee')
# дополнительные чашки кофе
additional_cups = min_cups - cups_input
if additional_cups > 0:
    print("Yes, I can make that amount of coffee (and even", abs(additional_cups), "more than that)")
elif cups_input > min_cups:
    print('No, I can make only', min_cups, 'cups of coffee')

'''

# 4/6

money = 550
water = 400
milk = 540
coffee = 120
cups = 9


# ingrid = [water, milk, coffee, cups]

def foo_latte():
    global water, milk, coffee, cups
    if water / 350 >= 1:
        print('I have enough resources, making you a coffee!')
        print(water)
    else:
        print('Sorry, not enough water!')


def state():
    print(water, " of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, " cups")
    print(money, " money")
    print()


def has():
    print('The coffee machine has:')
    print()


has()


# state()


def buy_espresso():
    global water
    global coffee
    global money
    global cups
    global milk
    water = water - 250
    milk = milk
    coffee = coffee - 16
    money = money + 4
    cups = cups - 1


def buy_latte() -> object:
    global water
    global coffee
    global money
    global cups
    global milk
    water = water - 350
    milk = milk - 75
    coffee = coffee - 20
    money = money + 7
    cups = cups - 1


def buy_cappuccino():
    global water
    global coffee
    global money
    global cups
    global milk
    water = water - 200
    milk = milk - 100
    coffee = coffee - 12
    money = money + 6
    cups = cups - 1


def fill():
    global water
    global coffee
    global cups
    global milk
    wat = int(input('Write how many ml of water do you want to add:\n'))
    water = water + wat

    mil = int(input('Write how many ml of milk do you want to add:\n'))
    milk = milk + mil

    cof = int(input('Write how many grams of coffee beans do you want to add:\n'))
    coffee = coffee + cof

    cup = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    cups = cups + cup


def take_my_money():
    global money
    print('I gave you $' + str(money))
    money = money - money


# меню пользователей
on = 1

while on == 1:
    what_do = input('Write action (buy, fill, take, remaining, exit):\n')
    if what_do == 'buy':
        what_coffee = input(
            'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - back to main menu: '
            '\n ')

        if what_coffee == '1':
            if water / 250 >= 1:
                print('I have enough resources, making you a coffee!')
                buy_espresso()
            else:
                print('Sorry, not enough water!')

            # state()
        if what_coffee == '2':
            if water / 350 >= 1:
                print('I have enough resources, making you a coffee!')
                buy_latte()
            else:
                print('Sorry, not enough water!')

            # state()
        if what_coffee == '3':
            if water / 200 >= 1:
                print('I have enough resources, making you a coffee!')
                buy_cappuccino()
            else:
                print('Sorry, not enough water!')
            # state()

    elif what_do == 'fill':
        fill()
        # state()
    elif what_do == 'take':
        take_my_money()
        # state()
    elif what_do == 'remaining':
        state()
    elif what_do == 'exit':
        on = 0
