from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Bonus:
    amount: float


@dataclass
class Commission:
    commission: float
    recruited_candidates: int

    def get(self):
        return self.commission * self.recruited_candidates


@dataclass
class Contract(ABC):
    conference: bool
    bonus: Optional[Bonus] = None
    commission: Optional[Commission] = None

    @abstractmethod
    def payment(self):
        output = 0
        if self.bonus:
            output += self.bonus.amount
        if self.commission:
            output += self.commission.get()

        return output


@dataclass
class MonthlyContract(Contract):
    salary: float = 0

    def payment(self):
        return super().payment() + self.salary


@dataclass
class HourlyContract(Contract):
    rate: float = 0
    worked_hours: float = 0

    def payment(self):
        return super().payment() + self.rate * self.worked_hours


@dataclass
class Employee:
    id: int
    name: str
    contract: Contract

    def can_go_to_conference(self):
        if self.contract:
            return self.contract.conference
        return False

    def salary(self):
        output = 0
        if self.contract:
            output += self.contract.payment()

        return output


@dataclass
class ThirdPartyEmployee:
    id: float
    name: str

    def can_go_to_conference(self):
        return False
