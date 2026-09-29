import pandas as pd

from src.enums.enums import TypeValues
from src.models.frequency import FrequencyDistribution


def create_frequency_dataframe(
    distribution: FrequencyDistribution,
    type_values: TypeValues,
) -> pd.DataFrame:
    table_data = []
    last_index = len(distribution.rows) - 1

    for index, row in enumerate(distribution.rows):
        if type_values == TypeValues.CONTINUOUS:
            if index == last_index:
                interval = f"[{row.lower_bound}, {row.upper_bound}]"
            else:
                interval = f"[{row.lower_bound}, {row.upper_bound})"

            table_data.append(
                {
                    "Intervalo": interval,
                    "Ponto médio": row.midpoint,
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