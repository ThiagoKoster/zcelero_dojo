from dataclasses import dataclass
from enum import Enum
from employee import BaseEmployee


@dataclass
class TechRecruiter(BaseEmployee):
    monthly_salary: float = 0
    commission: float = 0
    recruited_candidates: int = 0

    def can_go_to_conference(self):
        return False

    def salary(self):
        return self.commission * self.recruited_candidates + self.monthly_salary
