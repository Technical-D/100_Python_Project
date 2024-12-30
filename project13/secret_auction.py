# Secret auction
import os
from logo import logo
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_highest_bidder(bidder_list):
    winner = ''
    highest_bid = 0

    for bidder, bid in bidder_list.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
        
    return winner, highest_bid

print(logo)
print("Welcome to the Secret Auction Program!")
continue_bidding = True
bidder = {}
while continue_bidding:
    name = input("What is your name?: ")
    while True:
        bid = input("What is your bid?: $")
        try:
            bid = int(bid)
            break
        except ValueError:
            print("Please enter a valid bid!")
    
    while True:
        ques = input("Are there any more bidder? yes or no: ").lower()
        if ques in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")

    bidder[name] = bid

    if ques == 'no':
        continue_bidding = False
        winner, highest_bid = get_highest_bidder(bidder)
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
    elif ques == 'yes':
        clear_console()
        