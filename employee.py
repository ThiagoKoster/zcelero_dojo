from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class EmployeeType(Enum):
    SalariedEmployee = 1
    SalariedEmployeeWithBonus = 2
    TechRecruiter = 3
    Freelancer = 4


@dataclass
class Employee:
    id: int
    name: str
    type: EmployeeType
    monthly_salary: float = 0
    bonus: float = 0
    rate: float = 0
    worked_hours: float = 0
    commission: float = 0
    recruited_candidates: float = 0

    def can_go_to_conference(self):
        if (
            self.type == EmployeeType.Freelancer
            or self.type == EmployeeType.TechRecruiter
        ):
            return False
        return True

    def salary(self):
        # An employee that receives a monthly salary.
        if self.type == EmployeeType.SalariedEmployee:
            return self.monthly_salary

        # An employee that receives a monthly salary AND a monthly bonus.
        if self.type == EmployeeType.SalariedEmployeeWithBonus:
            return self.bonus + self.monthly_salary

        # A third party that provide recruiting services. It receices a montlhy salary and a comission per recruited candidate.
        if self.type == EmployeeType.TechRecruiter:
            return self.commission * self.recruited_candidates + self.monthly_salary

        # A third party that is paid per worked hours at a flat rate.
        if self.type == EmployeeType.Freelancer:
            return self.rate * self.worked_hours


@dataclass
class BaseEmployee(ABC):
    id: int
    name: str

    @abstractmethod
    def can_go_to_conference(self):
        pass

    @abstractmethod
    def salary(self):
        pass
