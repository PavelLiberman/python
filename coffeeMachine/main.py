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


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coins = {
    "quarter": 0.25,
    "dimes": 0.1,
    "nickel": 0.05,
    "pennies": 0.01
}


def check_resource_capacity(ingredients, actual_resources):
    """_summary_

    Args:
        coffee_type (_type_): _description_
        actual_resources (_type_): _description_

    Returns:
        _type_: _description_
    """
    for k, _ in actual_resources.items():
        if k in ingredients and \
            actual_resources[k] < ingredients[k]:
            print(f"Sorry there is not enough {k}")
            return False
    return True


def check_transaction(cost, money):
    """_summary_

    Args:
        coffee_type (_type_): _description_
        money (_type_): _description_

    Returns:
        _type_: _description_
    """
    temp_result = 0
    for coin, val in coins.items():
        if coin in money:
            temp_result += val * money[coin]
    result = temp_result - cost
    if result < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def generate_report(actual_resources):
    """_summary_

    Args:
        actual_resources (_type_): _description_
    """
    print("The current resource values is:")
    for k, v in actual_resources.items():
        print(f"{k}: {v}")


def get_money():
    """_summary_

    Returns:
        _type_: _description_
    """
    quarter = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickel = int(input("Insert nickel: "))
    pennies = int(input("Insert pennies: "))
    return {
            "quarter": quarter, 
            "dimes": dimes, 
            "nickel": nickel, 
            "pennies": pennies
        }


def make_order(actual_resources, ingredients, money, cost):
    """_summary_

    Args:
        coffee_type (_type_): _description_
        money (_type_): _description_
    """
    update_resources(actual_resources, ingredients, cost)
    left = calc_insert_money(money) - cost
    if left > 0:
        print(f"Here is ${left} dollars in change.")


def calc_insert_money(money):
    """_summary_

    Args:
        money (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = 0
    for k, v in coins.items():
        result += money[k] * v
    return result


def update_resources(actual_resources, ingredients, cost):
    """_summary_

    Args:
        actual_resources (_type_): _description_
        coffee_type (_type_): _description_
        money (_type_): _description_
    """
    for k, _ in actual_resources.items():
        if k in ingredients:
            actual_resources[k] -= ingredients[k]
    actual_resources["Money"] += cost


def main():
    OFF = False
    actual_resources = resources
    actual_resources["Money"] = 0
    while not OFF:
        coffee_type = input("What would you like? (espresso/latte/cappuccino):")
        if coffee_type in MENU:
            ingredients = MENU[coffee_type]['ingredients']
            cost = MENU[coffee_type]['cost']
            if check_resource_capacity(ingredients, actual_resources):
                money = get_money()
                if check_transaction(cost, money): 
                    make_order(actual_resources, ingredients, money, cost)
                    print(f"Here is your {coffee_type}. Enjoy!")
        elif coffee_type == "report":
            generate_report(actual_resources)
        elif coffee_type == "off":
            print("Turning off coffee machine")
            exit(0)
            

if __name__ == "__main__":
    main()