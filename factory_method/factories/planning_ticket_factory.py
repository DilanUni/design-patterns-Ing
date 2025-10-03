from .ticket_factory import TicketFactory
from tickets.planning_ticket import PlanningTicket

class PlanningTicketFactory(TicketFactory):
    def create_ticket(self):
        return PlanningTicket()
