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

print("First food:", food_options[0])
def display_food_library():
    for item in food_library[1:]:  
        name = item[0]
        cuisine = item[1]
        price = item[2]
        tags = item[3]

        print(f"{name} | {cuisine} | {price} | {tags}")