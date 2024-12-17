from abc import ABC, abstractmethod

class Subscriber(ABC): #Interface for subscribers, in this case our bidders
    @abstractmethod
    def update(self, item):
        pass