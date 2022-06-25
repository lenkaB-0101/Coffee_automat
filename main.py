from source_data import MENU
from source_data import resources

# == zakladni nastaveni==
# Ceny - nastaveni

espresso_price = MENU ['espresso']['cost']
latte_price = MENU ['latte']['cost']
cappuccino_price = MENU ['cappuccino']['cost']


# fce

def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mléko: {data['milk']}")
    print(f"Káva: {data['coffee']}")

def coins():
  print("Prosím vložte mince 5, 10, 20, 50")
  kc5 = int(input("Kolik 5 Kč chcete vložit?: ")) * 5
  kc10 = int(input("Kolik 10 Kč chcete vložit?: ")) * 10
  kc20 = int(input("Kolik 20 Kč chcete vložit?: ")) * 20
  kc50 = int(input("Kolik 50 Kč chcete vložit?: ")) * 50
  suma = kc5 + kc10 + kc20 + kc50
  print(f"Celkem jste vložili: {suma} Kč")
  return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >=0:
      print("Nápoj se připravuje.")
      if refund > 0:
        print (f"Zde jsou peníze zpět: {refund} Kč")
    else:
      print(f"Nevhodili jste dostatek peněz. Ještě vložte {price - user_sum_coins} Kč")

def fill_in_ingredience():
    return resources

def con_sump_ingredience(name_of_drink, ingredience):
    ingredience["water"] = ingredience["water"] - MENU [name_of_drink]["ingredients"]["water"]
    ingredience["milk"] = ingredience["milk"] - MENU [name_of_drink]["ingredients"]["milk"]
    ingredience["coffee"] = ingredience["coffee"] - MENU [name_of_drink]["ingredients"]["coffee"]
    print (f"Zbylé ingredience: {ingredience}")

def calculate_ingredients(drink_name):
    if drink_name == "espresso":
      con_sump_ingredience(drink_name, rest_of_ingredience)
    elif drink_name == "latte":
      con_sump_ingredience(drink_name, rest_of_ingredience)
    elif drink_name == "cappuccino":
      con_sump_ingredience(drink_name, rest_of_ingredience)

def ingredience_checker(in_water, in_milk, in_coffee):
    if in_water < 0:
      print("Není dostatek ingrediencí na tento nápoj")
      return False
    elif in_milk < 0:
      print("Není dostatek ingrediencí na tento nápoj")
      return False
    elif in_coffee < 0:
      print("Není dostatek ingrediencí na tento nápoj")
      return False
    else:
      print("Na váš nápoj je dostatek ingrediencí.")
      return True


# === kód automatu===

# načítáme původní množství ingrediencí

rest_of_ingredience = fill_in_ingredience()

lets_continue = True

while(lets_continue):

# volba uživatele - nápoj
 user_choice = input("Co si dáte? (espresso/latte/cappuccino): ")

  # výpočet zbytku ingrediencí
 calculate_ingredients(user_choice)

# kontrola dostatku ingrediencí
 if user_choice != "report":
   lets_continue = ingredience_checker(rest_of_ingredience["water"], rest_of_ingredience["coffee"], rest_of_ingredience["milk"])


# má kód dále pokračovat??

 if lets_continue == False:
    break

  # kontrolní report
 if user_choice == "report":
    report(rest_of_ingredience)



  # hlavní kód automatu
 if user_choice == "espresso":
      sum = coins()
      print(f"Cena espressa je: {espresso_price} Kč")
      calculate_change(sum, espresso_price)
 elif user_choice == "latte":
      sum = coins()
      print(f"Cena latte je: {latte_price} Kč")
      calculate_change(sum, latte_price)
 elif user_choice == "cappuccino":
      sum = coins()
      print(f"Cena cappuccina je: {cappuccino_price} Kč")
      calculate_change(sum, cappuccino_price)
      
      