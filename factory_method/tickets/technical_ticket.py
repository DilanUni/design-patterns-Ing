from .ticket import Ticket

class TechnicalTicket(Ticket):
    def register(self):
        print("Registrando ticket técnico")

    def notify(self):
        print("Notificando al área técnica")
