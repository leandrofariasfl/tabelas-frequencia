import math

from src.models.class_interval import ClassInterval


class ClassService:

    def build_classes(
        self,
        values: list[int | float],
    ) -> list[ClassInterval]:

        if not values:
            raise ValueError(
                "Não é possível criar classes sem dados."
            )

        minimum = min(values)
        maximum = max(values)

        number_of_classes = self._calculate_number_of_classes(
            len(values)
        )

        class_width = self._calculate_class_width(
            minimum,
            maximum,
            number_of_classes,
        )

        return self._create_intervals(
            minimum,
            maximum,
            number_of_classes,
            class_width,
        )

    def _calculate_number_of_classes(self, n: int) -> int:
        number_of_classes = round(
            1 + 3.322 * math.log10(n)
        )

        return max(1, number_of_classes)

    def _calculate_class_width(
        self,
        minimum: float,
        maximum: float,
        number_of_classes: int,
    ) -> float:

        amplitude = maximum - minimum

        if amplitude == 0:
            return 0

        return amplitude / number_of_classes

    def _create_intervals(
        self,
        minimum: float,
        maximum: float,
        number_of_classes: int,
        class_width: float,
    ) -> list[ClassInterval]:

        if class_width == 0:
            return [
                ClassInterval(
                    lower_bound=minimum,
                    upper_bound=maximum,
                    midpoint=minimum,
                )
            ]

        intervals = []

        for index in range(number_of_classes):
            lower_bound = minimum + index * class_width

            if index == number_of_classes - 1:
                upper_bound = maximum
            else:
                upper_bound = lower_bound + class_width

            midpoint = (lower_bound + upper_bound) / 2

            intervals.append(
                ClassInterval(
                    lower_bound=lower_bound,
                    upper_bound=upper_bound,
                    midpoint=midpoint,
                )
            )

        return intervals