from dataclasses import dataclass


@dataclass
class ClassInterval:
    lower_bound: float
    upper_bound: float
    midpoint: float