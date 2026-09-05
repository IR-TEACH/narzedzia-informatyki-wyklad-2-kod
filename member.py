"""Model czytelnika biblioteki."""
from dataclasses import dataclass


@dataclass
class Member:
    name: str
    email: str
    max_loans: int = 3
