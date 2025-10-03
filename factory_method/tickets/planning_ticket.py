from .ticket import Ticket

class PlanningTicket(Ticket):
    def register(self):
        print("Registrando ticket de planificación")

    def notify(self):
        print("Notificando al área de planificación")
