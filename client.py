from AuctionItem import AuctionItem
from Bidder import Bidder

# Create auction items
item1 = AuctionItem("Tractor")
item2 = AuctionItem("Car")

# Create bidders
bidder1 = Bidder("Zach")
bidder2 = Bidder("Nolan")
bidder3 = Bidder("Hanna")
bidder4 = Bidder("Dude")
bidder5 = Bidder("Guy")

# Bidders subscribe to auction items
bidder1.subscribe(item1)
bidder2.subscribe(item1)
bidder2.subscribe(item2)
bidder3.subscribe(item2)
bidder4.subscribe(item1)
bidder4.subscribe(item2)
bidder5.subscribe(item1)

# Place bids on items
item1.place_bid(100, "Zach")
item1.place_bid(150, "Nolan")
item2.place_bid(200, "Hanna")
item1.place_bid(120, "Hanna")
item2.place_bid(500, "Dude")
item1.place_bid(250, "Guy")