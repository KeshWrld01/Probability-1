# ================================
# ASSIGNMENT: WHAT ARE YOUR WINNING CHANCES?
# ================================

# Taking input for the number of balls in the basket
red = int(input("Enter number of red balls: "))
blue = int(input("Enter number of blue balls: "))
white = int(input("Enter number of white balls: "))

# Calculate the total number of balls
total = red + blue + white

# Probability of picking a white ball first (P(A))
prob_a = white / total

# Probability of picking a white ball second given that the first was white (with replacement)
# Since the first ball is replaced, the total count and white count remain unchanged.
prob_b_given_a = white / total

# Probability of both events occurring: P(white 1st and white 2nd)
prob_a_and_b = prob_a * prob_b_given_a

# Displaying the results rounded to 3 decimal places
print("\nProbability that the second ball is white given that the first ball is white:")
print(round(prob_b_given_a, 3))

print("Probability that both the first and second balls are white:")
print(round(prob_a_and_b, 3))