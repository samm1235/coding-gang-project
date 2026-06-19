# only to be run ONCE before u start a new list. 
# If run, library.csv will be reset.

import csv

food_library = [
    ["name", "cuisine", "price", "tags"],
    ["chicken rice", "local", "$", "fast,local"],
    ["sushiro", "japanese", "$$", "sushi"],
    ["gyg", "mexican", "$", "fastfood"]
]

with open("library.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(food_library)


import main

def display_food(filename: str):
    food_options = main.load_food_option(filename)
    if food_options == []:
        print(" Nothing to display.")
        return

    print(f"=== Food options ===")

    n = float(len(food_options)/10) + 1

    for i in range (1, n):
        for index in range(1,10i):
            print(f"""
#{index} | {food_options['name']}
    Cuisine : {food_options['cuisine']}
    Price: {food_options['price']} 
    Tags: {food_options['tags']} """)