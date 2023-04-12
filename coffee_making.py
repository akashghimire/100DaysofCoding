MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def coins():
    print("Please Insert Coins.")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def coffee_menu (drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

def is_transcation_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2 )
        print(f"here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money Refunded!!")
        return False


is_on = True
while is_on:
      choice = input("What would you like? (espresso/latte/cappuccino:")
      if choice == "off":
          is_on = False
      elif choice == "report":

          print(f"Water: {resources['water']}ml")
          print(f"Milk: {resources['milk']} ml")
          print(f"Coffee: {resources['coffee']}g")
          print(f"Money : ${profit}")
      else:
          drink = MENU[choice]
          if is_resources_sufficient(drink["ingredients"]):
              payment = coins()
              if is_transcation_success(payment,drink["cost"]):
                  coffee_menu(choice,drink["ingredients"])



