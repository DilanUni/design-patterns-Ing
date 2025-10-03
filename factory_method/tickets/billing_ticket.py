from .ticket import Ticket

class BillingTicket(Ticket):
    def register(self):
        print("Registrando ticket de facturación")

    def notify(self):
        print("Notificando al área de facturación")
