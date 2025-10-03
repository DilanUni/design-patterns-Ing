from .ticket_factory import TicketFactory
from tickets.technical_ticket import TechnicalTicket

class TechnicalTicketFactory(TicketFactory):
    def create_ticket(self):
        return TechnicalTicket()
