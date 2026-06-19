import csv
import random

class Food_manager:
   def __init__(self, filename: str):
        self.filename = filename

   def load_food_option(self):
      food_options = []
      with open(self.filename, "r") as f:
         reader = csv.DictReader(f)
         for row in reader:
            food_option = [
                     row["name"],
                     row["cuisine"],
                     row["price"],
                     row["tags"]
            ]
            food_options.append(food_option)
      return food_options


   def display_food(self):
      food_options = self.load_food_option()
      if food_options == []:
            print(" Nothing to display.")
            return
      size = 10
      for i in range(0, len(food_options), size):
            chunk = food_options[i : i + size]
         
            for index, food in enumerate(chunk, start=i + 1):
               print(f""" 
   #{index} | {food[0]}
   Cuisine : {food[1]}
   Price: {food[2]}
   Tags: {food[3]}""")
               
            if i + size < len(food_options):
               response = input("Load more (yes/no?): ").lower()
               if response != 'yes':
                  break
            
            
   def add_or_remove_food(self):
      food_options = self.load_food_option()
      answer = input("Would you like to add or remove food option (add/del)?:  ")
      
      if answer == "add":
         new_name = input("Input name of restaurant: ")
         new_cuisine = input("Input cuisine: ")
         new_price = input("Input price: ")
         new_tags = input("Input tags (use comma to separate): ")
         with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([new_name, new_cuisine, new_price, new_tags])
            print("Item added successfully!")

      elif answer == "del":
         target = input("Input name of restaurant: ")
         
         try:
            with open(self.filename, "r", newline="") as f:
                reader = csv.reader(f)
                rows = list(reader)
         except FileNotFoundError:
            print("File not found.")
            return

         if len(rows) <= 1:
            print("No items available to delete.")
            return
         
         header = rows[0]
         data_rows = rows[1:]
         original_count = len(data_rows)
         remaining_data = []

         for row in data_rows:
            if row[0] != target:
               remaining_data.append(row)
            else:
               continue

         if len(remaining_data) < original_count:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header) 
                writer.writerows(remaining_data)
            print(
                f"Successfully removed '{target}' !"
            )
         else:
            print("No matching restaurant found.")

            
      else:
         print("Invalid. Back to home page...")
         return None


   def rank_food(self):
      food_options = self.load_food_option()
      print("Please input your preferences. Press enter to skip")
      cuisine_input = input("What cuisine do you prefer?: ").lower()
      price_input = input("What is your price range (from $ to $$$): ").lower()
      tag_input = input("Any other requirements? (use , to separate): ").lower()

      ranked_results = []

      for food in food_options:
         score = 0
         if cuisine_input:
            if cuisine_input in food[1]:
               score += 1
         if price_input:
            if food[2].lower() == price_input:
               score += 1
         if tag_input:
            food_tags = [item.strip() for item in food["tags"].lower().split(",")]
            for tag in tag_input.split(","):
               if tag.strip() in food[3].lower():
                  score += 1

         ranked_results.append((score, food))
      ranked_results.sort(reverse = True, key=lambda item: item[0])
      for i, (score, food) in enumerate(ranked_results[:3], start=1):
         print(f"""
   #{i} | {food[0]}
      Cuisine : {food[1]}
      Price: {food[2]} 
      Tags: {food[3]}
      Score: {score} """)


   def randomise_food(self):
      food_options = self.load_food_option()
      random_number = random.randint(0, len(food_options) - 1)
      print(f"""
   # Random-food | {food_options[random_number][0]}
      Cuisine: {food_options[random_number][1]}
      Price: {food_options[random_number][2]} 
      Tags: {food_options[random_number][3]} """)


   def run(self):
      print("Welcome!")
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
            self.display_food()
            print("")
         elif choice == "2":
            self.add_or_remove_food()
            print("")
         elif choice == "3":
            self.rank_food()
            print("")
         elif choice == "4":
            self.randomise_food()
            print("")
         elif choice == "5":
            print("Goodbye!")
            break
         else:
            print('invalid choice')


