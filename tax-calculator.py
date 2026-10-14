#!/usr/bin/env python3
""" tax-calculator.py - print the amount of tax owed of given income, based on NZ tax brackets

Usage:
  python3 tax-calculator.py <income>
  python3 tax-calcultaor.py --test
"""
import sys
import argparse

# 1. define the problem and the data
# 2. define function signature
# 3. write examples (tests)
# 4. fill out function to handle your examples
# 5. run the program, see the tests pass, celebrate
#
# PROBLEM
# given income, return amount of tax owed, with tax rate based on NZ tax bracket.
# 
# DATA
# Income, Tax Amount, Tax Rate
#
# INCOME and TAX AMOUNT are numbers.
#
# Income is a Number, a person's yearly income
#
# Tax Amount is a Number.  It is a product of Income and Tax Rate.
#
# Tax Rate is a Number, representing the rate based on the income tax bracket.  It is one of:
# - .105 if income is between 0 and 15,600
# - .175 if income is between 15,601 and 53,500
# - .30 if income is between 53,501 and 78,100
# - .33 if income is between 78,101 and 180,000
# - .39 if income is 180,001 and up

# Income -> Tax Amount
def tax_calculator(income):
  """given income, return amount owed.
     the Tax rate is baed on NZ tax brackets.

  0-15,600: .105 
  >>> tax_calculator(1000)
  105.0

  15,601 - 53,500: .175 
  >>> tax_calculator(30000)
  5250.0

  53,501 - 78,100: .30
  >>> tax_calculator(60000)
  18000.0

  78,100 - 18,000: .30
  >>> tax_calculator(100000)
  33000.0
  
  180,000 and up: .39
  >>> tax_calculator(500000)
  195000.0
  """
  tax_rate = 0
  if 0 <= income <= 15600:
    tax_rate = .105
  elif 15601 <= income <= 53500:
    tax_rate = .175
  elif 53501 <= income <= 78100:
    tax_rate = .30
  elif 78101 <= income <= 180000:
    tax_rate = .33
  elif 180001 <= income:
    tax_rate = .39
  return income * tax_rate

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
  print(tax_calculator(args.income))

if __name__ == "__main__":
  if "--test" in sys.argv:
    import doctest
    results = doctest.testmod(verbose=True)
    sys.exit(results.failed)
  sys.exit(main(sys.argv))