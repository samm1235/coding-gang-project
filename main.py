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



def rank_food(food_options):
   cuisine_input = input("What cuisine do you prefer?: ").lower()
   price_input = input("What is your price range").lower()
   tag_input = input("Any other requirements?").lower()
   searched_tags = []

   if tag_input:
      searched_tags = [tag.strip() for tag in tag.spilt("|")]
   
   ranked_results = []

   for food in food_options:
      library_tags = food["tags"].split("|")
      score = 0


      if cuisine_input:
         if food["cuisine"].lower() == cuisine_input:
            score += 3
      if price_input:
         if food["price"].lower() == price_input:
            score += 2
      if tag_input:
         for tag in searched_tags:
            if tag in library_tags:
               score += 1

      ranked_results.append((score, food))
   ranked_results.sort(reverse = True, key=lambda item: item[0])
   return print(f"{ranked_results}")
rank_food(food_options)
