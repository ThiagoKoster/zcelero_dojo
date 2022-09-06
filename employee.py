from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


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
