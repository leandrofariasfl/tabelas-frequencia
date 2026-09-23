from dataclasses import dataclass


@dataclass
class FrequencyRow:
    value: int | float
    absolute_frequency: int
    cumulative_frequency: int
    relative_frequency: float
    cumulative_relative_frequency: float

@dataclass
class FrequencyDistribution:
    rows: list[FrequencyRow]
    total: int