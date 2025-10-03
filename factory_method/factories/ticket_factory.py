from abc import ABC, abstractmethod
from tickets.ticket import Ticket

class TicketFactory(ABC):
    @abstractmethod
    def create_ticket(self) -> Ticket:
        pass
