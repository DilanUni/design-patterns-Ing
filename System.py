from abc import ABC, abstractmethod

# Factory method
class Ticket(ABC):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_resolution_strategy(self, strategy):
        pass

    @abstractmethod
    def resolve_ticket(self):
        pass

class BillingTicket(Ticket):
    def __init__(self):
        self.strategy = None
        
    def register(self):
        print("BillingTicket registered")
        
    def notify(self):
        print("BillingTicket notification sent")
        
    def set_resolution_strategy(self, strategy):
        self.strategy = strategy
        
    def resolve_ticket(self):
        if self.strategy:
            self.strategy.resolve(self)
        else:
            print("No resolution strategy assigned")

class TechnicalTicket(Ticket):
    def __init__(self):
        self.strategy = None
        
    def register(self):
        print("TechnicalTicket registered")
        
    def notify(self):
        print("TechnicalTicket notification sent")
        
    def set_resolution_strategy(self, strategy):
        self.strategy = strategy
        
    def resolve_ticket(self):
        if self.strategy:
            self.strategy.resolve(self)
        else:
            print("No resolution strategy assigned")

class PlanningTicket(Ticket):
    def __init__(self):
        self.strategy = None
        
    def register(self):
        print("PlanningTicket registered")
        
    def notify(self):
        print("PlanningTicket notification sent")
        
    def set_resolution_strategy(self, strategy):
        self.strategy = strategy
        
    def resolve_ticket(self):
        if self.strategy:
            self.strategy.resolve(self)
        else:
            print("No resolution strategy assigned")


class TicketFactory(ABC):
    @abstractmethod
    def create_ticket(self, type):
        pass
    

class ServiceTicketCreator(TicketFactory):
    def create_ticket(self, type):
        if type == "billing":
            return BillingTicket()
        elif type == "technical":
            return TechnicalTicket()
        elif type == "planning":
            return PlanningTicket()
        else:
            return None

# Observer
class DepartmentNotifier(ABC):
    @abstractmethod
    def update(self, ticket):
        pass

class TechnicalArea(DepartmentNotifier):
    def update(self, ticket):
        print("TechnicalArea notified about", type(ticket).__name__)

class PlanningArea(DepartmentNotifier):
    def update(self, ticket):
        print("PlanningArea notified about", type(ticket).__name__)

class SystemsArea(DepartmentNotifier):
    def update(self, ticket):
        print("SystemsArea notified about", type(ticket).__name__)

# Strategy
class Resolution(ABC):
    @abstractmethod
    def resolve(self, ticket):
        pass

class AutomaticResolution(Resolution):
    def resolve(self, ticket):
        print("Automatic resolution applied to", type(ticket).__name__)

class TechnicalServiceResolution(Resolution):
    def resolve(self, ticket):
        print("Technical service resolution applied to", type(ticket).__name__)

class SendResidenceResolution(Resolution):
    def resolve(self, ticket):
        print("Send residence resolution applied to", type(ticket).__name__)

# Facade
class CustomerService:
    def __init__(self):
        self.creator = ServiceTicketCreator()
        self.departments = [TechnicalArea(), PlanningArea(), SystemsArea()]

    def create_ticket(self, type):
        ticket = self.creator.create_ticket(type)
        ticket.register()
        ticket.notify()
        return ticket

    def resolve_ticket(self, ticket, strategy):
        ticket.set_resolution_strategy(strategy)
        ticket.resolve_ticket()

    def notify_departments(self, ticket):
        for dept in self.departments:
            dept.update(ticket)


# Aplicación
service = CustomerService()

ticket1 = service.create_ticket("billing")
service.resolve_ticket(ticket1, AutomaticResolution())
service.notify_departments(ticket1)

print('--'*10)
ticket2 = service.create_ticket("technical")
service.resolve_ticket(ticket2, TechnicalServiceResolution())
service.notify_departments(ticket2)
