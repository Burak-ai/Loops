planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')

    multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print('\n', product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

for i in range(6):
    print('\n', 'Doing important work i =', i)

i = 0 
while i < 10:
    i += 1
    print(i, end=" ")

# List comprehensions
squares = [n**2 for n in range(10)]
print(squares)

# only the planets whose names are shorter than 6 characters.
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

nums = [5, -1, -2, 0, 3]
def count_negatives(nums):
    return len([num for num in nums if num < 0]) 
print(nums)
# "For each num in the list nums, if num is less than 0, include num in the new list."

def count_negatives(nums):
    return sum([num < 0 for num in nums])
print([num for num in nums if num < 0])


# Here's one solution:
def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

# And here's the list comprehension version:
def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]



def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row and False otherwise.
    """
    for i in range(1, len(meals)):
        if meals[i] == meals[i - 1]: # "Check if today's meal is the same as yesterday's meal."
            return True  # Return early if a match is found
    return False  # Only after checking *all* days

meals = [
    ['Egg', 'Spam'],
    ['Spam', 'Eggs', 'Bacon', 'Spam'],
    ['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam'],
    ['Spam', 'Spam'],
    ['Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top', 'Spam'],
    ['Spam'],
    []
]
print(menu_is_boring(meals))


# Casino Slot Machine

import random

def play_slot_machine():
    """Simulate a slot machine payout."""
#   payout = random.choices([0, 1, 5], weights=[0.5, 0.4, 0.1])[0] 
    payout = random.choices([0, 1, 5], weights=[0.3, 0.5, 0.2])[0] # Generous
    return payout - 1  # subtract cost to play

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return average net profit per run."""
    total_profit = 0
    for _ in range(n_runs):
        result = play_slot_machine()
        total_profit += result
    return total_profit / n_runs

print(estimate_average_slot_payout(10000))
