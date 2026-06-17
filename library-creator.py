# only to be run ONCE before u start a new list. 
# If run, library.csv will be reset.

import csv

food_library = [
    ["name", "cuisine", "price", "tags"],
    ["chicken Rice", "local", "$", "fast,local"],
    ["sushiro", "japanese", "$$", "sushi"],
    ["gyg", "mexican", "$", "fastfood"]
]

with open("library.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(food_library)