import pandas as pd

from src.enums.enums import TypeValues
from src.models.frequency import FrequencyDistribution


def format_number(value: int | float) -> str:
    return f"{value:.2f}".rstrip("0").rstrip(".")


def create_frequency_dataframe(
    distribution: FrequencyDistribution,
    type_values: TypeValues,
) -> pd.DataFrame:
    table_data = []
    last_index = len(distribution.rows) - 1

    for index, row in enumerate(distribution.rows):
        if type_values == TypeValues.CONTINUOUS:
            lower_bound = format_number(row.lower_bound)
            upper_bound = format_number(row.upper_bound)

            if index == last_index:
                interval = f"[{lower_bound}, {upper_bound}]"
            else:
                interval = f"[{lower_bound}, {upper_bound})"

            table_data.append(
                {
                    "Intervalo": interval,
                    "Ponto médio": format_number(row.midpoint),
                    "fi": row.absolute_frequency,
                    "Fi": row.cumulative_frequency,
                    "fr": f"{row.relative_frequency:.2%}",
                    "Fr": f"{row.cumulative_relative_frequency:.2%}",
                }
            )

        else:
            table_data.append(
                {
                    "Valor": row.value,
                    "fi": row.absolute_frequency,
                    "Fi": row.cumulative_frequency,
                    "fr": f"{row.relative_frequency:.2%}",
                    "Fr": f"{row.cumulative_relative_frequency:.2%}",
                }
            )

    return pd.DataFrame(table_data)