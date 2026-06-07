import random

def search():
    while True:
        matching_indices = []

        prompt = input("Any filters? (e.g. cuisine, location):")
        if prompt == 0:
            rand_num = random.randint()
            matching_indices.append(rand_num)
        elif prompt