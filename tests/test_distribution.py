from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.services.distribution_service import DistributionService


def test_calcula_distribuicao_discreta():
    service = DistributionService()

    dataset = Dataset(
        values=[2, 2, 3, 4],
        type_values=TypeValues.DISCRETE,
    )

    distribution = service.calculate(dataset)

    assert distribution.total == 4
    assert [row.value for row in distribution.rows] == [2, 3, 4]


def test_calcula_distribuicao_continua():
    service = DistributionService()

    dataset = Dataset(
        values=[10, 12, 15, 18, 20, 22, 25, 30],
        type_values=TypeValues.CONTINUOUS,
    )

    distribution = service.calculate(dataset)

    assert distribution.total == 8
    assert len(distribution.rows) > 0
    assert distribution.rows[-1].cumulative_frequency == 8