from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def notify(self):
        pass
