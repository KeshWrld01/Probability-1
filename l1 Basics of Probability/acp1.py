import random

def check_dice_probability():
    # Defining the possible outcomes of a standard 6-sided dice roll
    dice_faces = [1, 2, 3, 4, 5, 6]
    
    # "Rolling" the dice randomly
    result = random.choice(dice_faces)
    print(f"Dice rolled: {result}")
    
    # Calculating the probability of getting a 6
    # Number of favorable outcomes (getting a 6) = 1
    # Total possible outcomes = 6
    probability = dice_faces.count(6) / len(dice_faces)
    print("Probability of getting a 6 is:", probability)
    
    # Checking if a 6 was rolled
    if result == 6:
        return "Game can be started"
    else:
        return "Roll again"

# Running the experiment
res = check_dice_probability()
print(res)