from dataclasses import dataclass
from enum import Enum
from employee import BaseEmployee


@dataclass
class Freelancer(BaseEmployee):
    rate: float = 0
    worked_hours: float = 0

    def can_go_to_conference(self):
        return False

    def salary(self):
        return self.rate * self.worked_hours
