#!/usr/bin/env python3
""" tax-calculator.py - print the amount of tax owed of given income, based on NZ tax brackets

Usage:
  python3 tax-calculator.py <income>
  python3 tax-calcultaor.py --test
"""
import sys
import argparse

# Income is your yearly income
# 
# Income Segment is a portion of your income that falls within a tax bracket.
#
# NZ Tax Bracket is the rates given  on ird.govt.nz.
# it represents the tax rates per segment of income.
# 
# Tax Bracket is a tuple (Threshold, Rate).
# Threshold is the lower threshold for the rate of this income bracket.  So for the NZ tax bracket 78,100 - 180,000, the threshold is 78,100.
#
# Total Owed is the sum of tax owed for each segment of your income.
# 
# Income Remaining is a number representing the portion of your income that has not yet been taxed.
#
# To determine total owed, you can take each segment starting from the highest valid tax bracket, calculate how much is owed for that segment and add this to the tally.
#
# As you calculate each bracket from highest to lowest, you can remove that segment from the income remaining to be taxed.  
#
# In other words, you can recurse over the total remaining and keep a running tally of total owed. Continue to recur the function until the remaining income is 0 (all segments have been taxed) and then grab the final total.

def determine_tax_bracket(income):
  """given income, determine highest threshold it qualifies for and return that threshold and its rate.
  """
  if income > 180000:
    return 180000, .39
  elif income > 78100:
    return 78100, .33
  elif income > 53500:
    return 53500, .30
  elif income > 15600:
    return 15600, .175
  else:
    return 0, .105

def tax_calculator(income_remaining, total_owed):
  """ recurse on the remaining income, calculating
  total owed per income segment from highest valid bracket downward, until there is no more income to be taxed. return
  the total tax remaining and the total owed.

  >>> tax_calculator(200000, 0)
  (0, 57077.5)
  >>> tax_calculator(195000,0)
  (0, 55127.5)
  >>> tax_calculator(82100,0)
  (0, 16970.5)
  >>> tax_calculator(65000,0)
  (0, 11720.5)
  >>> tax_calculator(35000,0)
  (0, 5033.0)
  >>> tax_calculator(5200,0)
  (0, 546.0)
  """
  if income_remaining == 0:
    return income_remaining, total_owed
  else:
    threshold, tax_rate = determine_tax_bracket(income_remaining)
    income_segment = income_remaining - threshold
    total_owed += income_segment * tax_rate 
    return tax_calculator(threshold, total_owed)

def main(argv):
  parser = argparse.ArgumentParser(
    prog="tax-calculator.py",
    description="Print tax owed based on given income, following NZ tax rules"
  )
  parser.add_argument(
    "income",
    type=float,
    help="income is a number to calculate (e.g., 1000 or 5250.25)"
  )
  args = parser.parse_args(argv[1:])
  income_remaining, total_owed = tax_calculator(args.income, 0)
  print(total_owed)

if __name__ == "__main__":
  if "--test" in sys.argv:
    import doctest
    results = doctest.testmod(verbose=True)
    sys.exit(results.failed)
  sys.exit(main(sys.argv))