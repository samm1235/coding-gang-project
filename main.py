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
    print("=" * 80 + "\n")

display_food(food_options)


def add_food(filename, food_options):
   answer = input("Would you like to add a new food option?")
   if answer == "yes":
      new_name = input("Input name of restaurant")
      new_cuisine = input("Input cuisine")
      new_price = input("Input price")
      with open(filename, "a", newline="") as f:
          writer = csv.writer(f)
          writer.writerow([new_name, new_cuisine, new_price])
          print("Added successfully!")
    else:
      print("invalid answer")
      return

add_food("library.csv", food_options)


   