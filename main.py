import csv

food_library = [
    ["name", "cuisine", "price", "tags"],
    ["Chicken Rice", "singaporean", "cheap", "fast|lunch"],
    ["Sushiro", "japanese", "medium", "sushi|lunch"]
]

with open("library.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(food_library)


def load_food_option():
  food_options = []
  with open("library.csv", "r") as f:
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

food_options = load_food_option()

def display_food(food_options):
    if not food_options:
        print(" Nothing to display.")
        return

    print(f"=== Food options ===")

    for i, food_option in enumerate(food_options, start=1):
        print(f"""
#{i} | {food_option['name']}
   Cuisine  : {food_option['cuisine']}
   Price : {food_option['price']} """)
  

display_food(food_options)


def add_food(filename, food_options):
   answer = input("Would you like to add a new food option?")
   
   if answer == "yes":
      new_name = input("Input name of restaurant")
      new_cuisine = input("Input cuisine")
      new_price = input("Input price")
      new_tags = input("Input tags (use | to separate): ")
      with open(filename, "a", newline="") as f:
          writer = csv.writer(f)
          writer.writerow([new_name, new_cuisine, new_price, new_tags])
          print("Added successfully!")

  
add_food("library.csv", food_options)

def filter_food(food_options):
   filter_cuisine = input("What cuisine do you prefer?: ").lower()
   filter_price = input("What is your price range").lower()
   filter_tags = input("Any other requirements?").lower()
   results = []
   for food in food_options:
      tags = food["tags"].split("|")

      match = True
      if filter_tags:
         if filter_tags not in [t.lower() for t in tags]:  #for t in tags mean go through each item in "tags" list
            match = False
      if filter_cuisine:
         if food["cuisine"].lower()!= filter_cuisine:
            match = False
      if filter_price:
         if food["price"].lower() != filter_price:
            match = False
      if match == True:
         results.append(food)
   if match == False:
      print("There is no food that fits your requirements")
   return results
filter_food(food_options)