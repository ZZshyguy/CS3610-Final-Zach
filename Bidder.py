from Subscriber import Subscriber

class Bidder(Subscriber):
    #Represents a bidder in the auction system.
    def __init__(self, name):
        self.name = name
        self.subscribed_items = [] #List of items a bidder wants updates on

    def subscribe(self, auction_item):
        #Subscribe to an auction item.
        if auction_item not in self.subscribed_items:
            self.subscribed_items.append(auction_item) #add item to bidder's list
            auction_item.add_bidder(self) #add bidder to item's list to be notified

    def unsubscribe(self, auction_item):
        #Unsubscribe from an auction item.
        if auction_item in self.subscribed_items:
            self.subscribed_items.remove(auction_item)
            auction_item.remove_bidder(self)

    def update(self, auction_item):
        #Receive a notification from an auction item.
        print(f"{self.name} has been notified of a new bid on '{auction_item.name}': {auction_item.highest_bid}")
        