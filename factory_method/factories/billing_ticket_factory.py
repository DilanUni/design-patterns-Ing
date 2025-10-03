from .ticket_factory import TicketFactory
from tickets.billing_ticket import BillingTicket

class BillingTicketFactory(TicketFactory):
    def create_ticket(self):
        return BillingTicket()
