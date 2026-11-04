import scipy.stats as stats

# Checkpoint 1: Calculate the probability of observing 12 or more days of rain
# P(X >= 12) = 1 - P(X <= 11)
prob_12_or_more = 1 - stats.poisson.cdf(11, 10)
print("Probability of observing 12 or more days of rain:", prob_12_or_more)

# Checkpoint 2: Calculate the probability of observing between 12 and 18 days of rain (inclusive)
# P(12 <= X <= 18) = P(X <= 18) - P(X <= 11)
prob_12_to_18 = stats.poisson.cdf(18, 10) - stats.poisson.cdf(11, 10)
print("Probability of observing between 12 and 18 days of rain:", prob_12_to_18)