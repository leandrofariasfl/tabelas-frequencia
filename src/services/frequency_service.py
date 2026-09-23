from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.models.frequency import FrequencyDistribution, FrequencyRow


class FrequencyService:

    def calculate(
        self,
        dataset: Dataset,
        classes: list[tuple[float, float]] | None = None,
    ) -> FrequencyDistribution:
        if dataset.type_values == TypeValues.DISCRETE:
            return self._calculate_discrete(dataset.values)

        return self._calculate_continuous(dataset.values, classes)

    def _calculate_discrete(self, values: list[int | float]) -> FrequencyDistribution:
        unique_values = sorted(set(values))
        counts = {value: values.count(value) for value in unique_values}

        return self._build_distribution(unique_values, counts, len(values))

    def _calculate_continuous(
        self,
        values: list[int | float],
        classes: list[tuple[float, float]] | None,
    ) -> FrequencyDistribution:
        if not classes:
            raise ValueError(
                "É necessário informar as classes para calcular a frequência de dados contínuos."
            )

        midpoints = []
        counts = {}
        last_upper_bound = classes[-1][1]

        for lower_bound, upper_bound in classes:
            midpoint = (lower_bound + upper_bound) / 2
            is_last_class = upper_bound == last_upper_bound

            midpoints.append(midpoint)
            counts[midpoint] = self._count_in_class(
                values, lower_bound, upper_bound, is_last_class
            )

        return self._build_distribution(midpoints, counts, len(values))

    def _count_in_class(
        self,
        values: list[int | float],
        lower_bound: float,
        upper_bound: float,
        is_last_class: bool,
    ) -> int:
        if is_last_class:
            return sum(1 for value in values if lower_bound <= value <= upper_bound)

        return sum(1 for value in values if lower_bound <= value < upper_bound)

    def _build_distribution(
        self,
        keys: list[int | float],
        counts: dict[int | float, int],
        total: int,
    ) -> FrequencyDistribution:
        rows = []
        cumulative_frequency = 0
        cumulative_relative_frequency = 0.0

        for key in keys:
            absolute_frequency = counts[key]
            cumulative_frequency += absolute_frequency
            relative_frequency = absolute_frequency / total
            cumulative_relative_frequency += relative_frequency

            rows.append(
                FrequencyRow(
                    value=key,
                    absolute_frequency=absolute_frequency,
                    cumulative_frequency=cumulative_frequency,
                    relative_frequency=relative_frequency,
                    cumulative_relative_frequency=cumulative_relative_frequency,
                )
            )

        return FrequencyDistribution(rows=rows, total=total)