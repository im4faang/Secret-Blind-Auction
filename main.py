from art import logo
import os

bidders = {}
should_end = False
print(logo)

def blind_auction(bidders):
  highest_bid = 0
  winner = ""
  for bidder in bidders:
    if bidders[bidder] > highest_bid:
      highest_bid = bidders[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not should_end:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  if more_bidders == "no":
    should_end = True
  elif more_bidders == "yes":
    os.system("clear")
  bidders[name] = bid
blind_auction(bidders)
