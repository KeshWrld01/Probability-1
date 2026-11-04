"""
Assignment: Central Limit Theorem Examples
Module M17 Lesson 6 – Sampling Distributions

This module provides 5 real-world examples demonstrating the practical 
application and effects of the Central Limit Theorem (CLT) across 
different domains.
"""

def example_dice_rolls():
    """
    1. Rolling a Fair or Unfair Die
    -------------------------------
    - Scenario: The probability distribution of rolling a single 6-sided die 
      is uniform (every face from 1 to 6 has an equal 1/6 chance).
    - CLT Application: When you take multiple random samples of 30 or more rolls, 
      calculate the mean of each sample, and plot them, the distribution of 
      sample means forms a normal (bell-shaped) curve.
    """
    pass


def example_call_center_wait_times():
    """
    2. Customer Service Call Center Wait Times
    ------------------------------------------
    - Scenario: Individual customer hold times are heavily right-skewed 
      (most callers wait briefly, while a few have long wait times).
    - CLT Application: If management tracks the average wait time for daily samples 
      of 100 callers, the distribution of these daily sample means is normally 
      distributed, enabling reliable staffing forecasts and statistical testing.
    """
    pass


def example_human_heights():
    """
    3. Human Heights in a Population
    --------------------------------
    - Scenario: Heights in a large population can sometimes exhibit slight 
      skewness depending on demographic groupings.
    - CLT Application: Taking multiple random samples (e.g., groups of 50 individuals) 
      and recording the mean height of each sample yields a normal distribution 
      centered around the true population mean.
    """
    pass


def example_manufacturing_quality_control():
    """
    4. Quality Control in Bottling Liquids
    --------------------------------------
    - Scenario: Individual bottles filled by a machine vary slightly around a 
      target volume due to mechanical tolerances.
    - CLT Application: Quality control inspectors pull samples of 40 bottles 
      at regular intervals and track the sample mean volume, which follows 
      a normal distribution to easily detect machine drift.
    """
    pass


def example_stock_market_returns():
    """
    5. Stock Market Daily Returns
    -----------------------------
    - Scenario: Daily stock price movements and returns for individual companies 
      are volatile and exhibit non-normal fat tails.
    - CLT Application: Portfolio managers analyze average monthly or yearly 
      returns across multiple periods; as sample sizes increase, the distribution 
      of these sample means approaches normality, forming the basis of modern 
      portfolio theory.
    """
    pass

if __name__ == "__main__":
    print("Central Limit Theorem Examples docstring module loaded successfully.")