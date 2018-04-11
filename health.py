import random

# Initial health of the player
health = 50

# Game difficulty
difficulty = random.randint(1,3)

# Printing the difficulty
print(difficulty)

# Value of the health potion depending upon the difficulty of the game
# Casting to int
potion_health = int(random.randint(25,50) / difficulty)

# Adding the value of health potion to the player's health
health += potion_health

# Printing the resultant health
print(health)