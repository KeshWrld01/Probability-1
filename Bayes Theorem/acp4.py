import scipy.stats as stats

# Number of trials (coin flips)
n = 10

# Probability of success (getting heads on a fair coin)
p = 0.5

# Calculate the probability of observing between 2 and 4 heads (i.e., exactly 2, 3, or 4 heads)
prob_between_2_and_4 = (
    stats.binom.pmf(2, n, p) + 
    stats.binom.pmf(3, n, p) + 
    stats.binom.pmf(4, n, p)
)

print("Probability of observing between 2 and 4 heads from 10 coin flips:")
print(prob_between_2_and_4)