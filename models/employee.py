from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Collaborator(ABC):
    id: int
    name: str

    @abstractmethod
    def can_go_to_conference(self):
        pass

    @abstractmethod
    def salary(self):
        pass


@dataclass
class SalariedEmployee(Collaborator):
    """An employee that receives a monthly salary."""

    monthly_salary: float

    def can_go_to_conference(self):
        return True

    def salary(self):
        return self.monthly_salary


@dataclass
class SalariedEmployeeWithBonus(SalariedEmployee):
    """An employee that receives a monthly salary AND a monthly bonus."""

    bonus: float

    def salary(self):
        return super().salary() + self.bonus


@dataclass
class ThirdPartyCollaborator(Collaborator):
    def can_go_to_conference(self):
        return False


@dataclass
class TechRecruiter(ThirdPartyCollaborator):
    """A third party that provide recruiting services. It receices a montlhy salary and a comission per recruited candidate."""

    monthly_salary: float
    commission: float
    recruited_candidates: int

    def salary(self):
        return self.monthly_salary + self.commission * self.recruited_candidates


@dataclass
class Freelancer(ThirdPartyCollaborator):
    """A third party that is paid per worked hours at a flat rate."""

    rate: float = 0
    worked_hours: float = 0

    def salary(self):
        return self.rate * self.worked_hours
