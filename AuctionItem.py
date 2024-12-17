

class AuctionItem:
    #Represents an auction item in the auction system.
    def __init__(self, name):
        self.name = name
        self.bidders = [] #List of bidders
        self.highest_bid = 0 #Start at 0

    def add_bidder(self, bidder):
        #Add a bidder to the list.
        if bidder not in self.bidders: #Don't want same bidder twice
            self.bidders.append(bidder)

    def remove_bidder(self, bidder):
        #Remove a bidder from the notification list.
        if bidder in self.bidders:
            self.bidders.remove(bidder)

    def place_bid(self, amount, bidder_name):
        #Place a new bid and notify all subscribed bidders.
        if amount > self.highest_bid:
            self.highest_bid = amount #Set highest bid to given amount
            print(f"New highest bid on '{self.name}': {amount} by {bidder_name}")#Print to help keep track of things
            self.notify_bidders(bidder_name) #Will notify bidders of the item, we send a bidder_name to know who placed the bid
        else: #Reject a lower bid, printing a message
            print(f"Bid of {amount} by {bidder_name} is lower than {self.highest_bid}.")

    def notify_bidders(self, bidder_name):
        #Notify all bidders except the one who placed the bid.
        for bidder in self.bidders:
            if bidder.name != bidder_name: #Don't want to send updates to the bidder who palced the bid
                bidder.update(self)
                