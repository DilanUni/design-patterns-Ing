from factories.billing_ticket_factory import BillingTicketFactory
from factories.technical_ticket_factory import TechnicalTicketFactory
from factories.planning_ticket_factory import PlanningTicketFactory

def client(factory):
    ticket = factory.create_ticket()
    ticket.register()
    ticket.notify()

if __name__ == "__main__":
    print("=== FACTORY METHOD DEMO ===\n")

    print("1. Billing Ticket:")
    client(BillingTicketFactory())

    print("\n2. Technical Ticket:")
    client(TechnicalTicketFactory())

    print("\n3. Planning Ticket:")
    client(PlanningTicketFactory())
