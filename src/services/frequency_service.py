from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.models.frequency import (
    ContinuousFrequencyRow,
    FrequencyDistribution,
    FrequencyRow,
)


class FrequencyService:

    def calculate(
        self,
        dataset: Dataset,
        classes: list[tuple[float, float]] | None = None,
    ) -> FrequencyDistribution:

        if dataset.type_values == TypeValues.DISCRETE:
            return self._calculate_discrete(dataset.values)

        return self._calculate_continuous(dataset.values, classes)

    def _calculate_discrete(
        self,
        values: list[int | float],
    ) -> FrequencyDistribution:

        unique_values = sorted(set(values))

        counts = {
            value: values.count(value)
            for value in unique_values
        }

        rows = []
        total = len(values)
        cumulative_frequency = 0

        for value in unique_values:
            absolute_frequency = counts[value]
            cumulative_frequency += absolute_frequency

            relative_frequency = absolute_frequency / total
            cumulative_relative_frequency = cumulative_frequency / total

            rows.append(
                FrequencyRow(
                    value=value,
                    absolute_frequency=absolute_frequency,
                    cumulative_frequency=cumulative_frequency,
                    relative_frequency=relative_frequency,
                    cumulative_relative_frequency=cumulative_relative_frequency,
                )
            )

        return FrequencyDistribution(
            rows=rows,
            total=total,
        )

    def _calculate_continuous(
        self,
        values: list[int | float],
        classes: list[tuple[float, float]] | None,
    ) -> FrequencyDistribution:

        if not classes:
            raise ValueError(
                "É necessário informar as classes para calcular "
                "a frequência de dados contínuos."
            )

        rows = []
        total = len(values)
        cumulative_frequency = 0

        for index, (lower_bound, upper_bound) in enumerate(classes):

            is_last_class = index == len(classes) - 1

            absolute_frequency = self._count_in_class(
                values,
                lower_bound,
                upper_bound,
                is_last_class,
            )

            cumulative_frequency += absolute_frequency

            relative_frequency = absolute_frequency / total
            cumulative_relative_frequency = cumulative_frequency / total

            midpoint = (lower_bound + upper_bound) / 2

            rows.append(
                ContinuousFrequencyRow(
                    lower_bound=lower_bound,
                    upper_bound=upper_bound,
                    midpoint=midpoint,
                    absolute_frequency=absolute_frequency,
                    cumulative_frequency=cumulative_frequency,
                    relative_frequency=relative_frequency,
                    cumulative_relative_frequency=cumulative_relative_frequency,
                )
            )

        return FrequencyDistribution(
            rows=rows,
            total=total,
        )

    def _count_in_class(
        self,
        values: list[int | float],
        lower_bound: float,
        upper_bound: float,
        is_last_class: bool,
    ) -> int:

        if is_last_class:
            return sum(
                1
                for value in values
                if lower_bound <= value <= upper_bound
            )

        return sum(
            1
            for value in values
            if lower_bound <= value < upper_bound
        )