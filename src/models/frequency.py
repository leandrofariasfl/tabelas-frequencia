from dataclasses import dataclass


@dataclass
class FrequencyRow:
    value: int | float
    absolute_frequency: int
    cumulative_frequency: int
    relative_frequency: float
    cumulative_relative_frequency: float

@dataclass
class ContinuousFrequencyRow:
    lower_bound: float
    upper_bound: float
    midpoint: float
    absolute_frequency: int
    cumulative_frequency: int
    relative_frequency: float
    cumulative_relative_frequency: float

@dataclass
class FrequencyDistribution:
    rows: list[FrequencyRow] | list[ContinuousFrequencyRow]
    total: int