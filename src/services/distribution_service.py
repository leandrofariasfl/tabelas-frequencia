from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.models.frequency import FrequencyDistribution
from src.services.class_service import ClassService
from src.services.frequency_service import FrequencyService


class DistributionService:

    def __init__(self):
        self.class_service = ClassService()
        self.frequency_service = FrequencyService()

    def calculate(self, dataset: Dataset) -> FrequencyDistribution:
        if dataset.type_values == TypeValues.DISCRETE:
            return self.frequency_service.calculate(dataset)

        classes = self.class_service.build_classes(dataset.values)

        return self.frequency_service.calculate(
            dataset,
            classes=classes,
        )