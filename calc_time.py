# * Purpose
# * Take time in minutes and display hours and minutes
from math import trunc


def calculate_time(mins):
    """This function takes mins and print hours and minutes"""
    hours = mins / 60  # take quotient
    rem_mins = mins % 60  # take remainder as minutes
    print(f"{trunc(hours)} hours and {rem_mins} minutes.")

# function call
calculate_time(64+95+65+35-10)
