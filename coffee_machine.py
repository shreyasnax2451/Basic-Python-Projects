MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
  quarters = int(input('How many quarters? '))*0.25
  dimes = int(input('How many dimes? '))*0.1
  nickles = int(input('How many nickles? '))*0.05
  pennies = int(input('How many pennies? '))*0.01

  return quarters + dimes + nickles + pennies

def check_transaction(payment, drink_cost):
  if payment >= drink_cost:
    print("Here is ${:.2f} dollars in change".format(payment - drink_cost))
    global money
    money += drink_cost
    return drink_cost
  else:
    print("Sorry that's not enough money. Money refunded.") 

def check_resources(resources, drink):
  for resource in resources.keys():
    if resources[resource] < drink['ingredients'][resource]:
      print(f'Sorry there is not enough {resource}.')
      return False
  return True

def make_coffee(resources, drink):
  for resource in resources.keys():
    resources[resource] = resources[resource] - drink['ingredients'][resource]
  
machine_on = True
money = 0
drinks_list = ['espresso', 'latte', 'cappuccino']

while machine_on:
  order = input("What would you like? (espresso/latte/cappuccino) ")
  if order == 'off':
    machine_on = False
  elif order == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
  elif order not in drinks_list:
    print('Wrong Order!')
  else:
    drink = MENU[order]
    if check_resources(resources, drink):
      payment = process_coins()
      if check_transaction(payment, drink['cost']):
        make_coffee(resources, drink)
        print(f"Here is your {order}. Enjoy!")