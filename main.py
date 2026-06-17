import csv
import random


def load_food_option(filename: str):
  food_options = []
  with open(filename, "r") as f:
      reader = csv.DictReader(f)
      for row in reader:
        food_option = {
            "name": row["name"],
            "cuisine": row["cuisine"],
            "price": row["price"],
            "tags": row["tags"]
            }
        food_options.append(food_option)
  return food_options


def display_food(filename: str):
    food_options = load_food_option(filename)
    if food_options == []:
        print(" Nothing to display.")
        return

    print(f"=== Food options ===")

    for i, food_option in enumerate(food_options, start=1):
        print(f"""
   #{i} | {food_option['name']}
      Cuisine : {food_option['cuisine']}
      Price: {food_option['price']} 
      Tags: {food_option['tags']} """)
  

def add_or_remove_food(filename: str):
   food_options = load_food_option(filename)
   answer = input("Would you like to add or remove food option (add/del)?:  ")
   
   if answer == "add":
      new_name = input("Input name of restaurant: ")
      new_cuisine = input("Input cuisine: ")
      new_price = input("Input price: ")
      new_tags = input("Input tags (use _ to separate): ")
      with open(filename, "a", newline="") as f:
          writer = csv.writer(f)
          writer.writerow([new_name, new_cuisine, new_price, new_tags])
          print("")
          print("Item added successfully!")

   elif answer == "del":
      target = input("Input name of restaurant: ")
      for i, food_option in enumerate(food_options, start = 1):
         if target in food_option['name']:
            with open(filename, "r", newline="") as f:
               reader = csv.reader(f)
               rows = list(reader)
               del rows[i]
            with open(filename, "w", newline="") as file:
               writer = csv.writer(file)
               writer.writerows(rows)
            print("Item removed successfully!")
      
         
   else:
      print("Invalid. Back to home page...")
      return None


def rank_food(filename: str):
   food_options = load_food_option(filename)
   print("Please input your preferences. Press enter to skip")
   cuisine_input = input("What cuisine do you prefer?: ").lower()
   price_input = input("What is your price range (from $ to $$$): ").lower()
   tag_input = input("Any other requirements? (use , to separate): ").lower()

   ranked_results = []

   for food in food_options:
      score = 0
      if cuisine_input:
         if food["cuisine"].lower() == cuisine_input:
            score += 3
      if price_input:
         if food["price"].lower() == price_input:
            score += 2
      if tag_input:
         for tag in tag_input:
            if tag in food["tags"]:
               score += 1

      ranked_results.append((score, food))
   ranked_results.sort(reverse = True, key=lambda item: item[0])
   for i, (score, food) in enumerate(ranked_results[:3], start=1):
        print(f"""
   #{i} | {food['name']}
      Cuisine : {food['cuisine']}
      Price: {food['price']} """)


def randomise_food(filename: str):
   food_options = load_food_option(filename)
   random_number = random.randint(0, len(food_options) - 1)
   print(f"""
   # Random-food | {food_options[random_number]['name']}
      Cuisine: {food_options[random_number]['cuisine']}
      Price: {food_options[random_number]['price']} 
      Tags: {food_options[random_number]['tags']} """)


def run_library(filename: str):
   print("Welcome")
   while True:
      print("=== Menu ===")
      print("1. View all food options")
      print("2. Add or remove food option")
      print("3. Choose food options based on preferences")
      print("4. Random food generator")
      print("5. Quit and save")

      choice = input("Please input choice from 1-5: ")
      print()
      if choice == "1":
         display_food(filename)
         print("")
      elif choice == "2":
         add_or_remove_food(filename)
         print("")
      elif choice == "3":
         rank_food(filename)
         print("")
      elif choice == "4":
         randomise_food(filename)
         print("")
      elif choice == "5":
         print("Goodbye!")
         break
      else:
         print('invalid choice')


