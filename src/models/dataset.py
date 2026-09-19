from dataclasses import dataclass

from src.enums.enums import TypeValues

@dataclass
class Dataset:
    values: list[int | float]
    type_values: TypeValues




