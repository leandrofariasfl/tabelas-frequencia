import pytest

from src.enums.enums import TypeValues
from src.models.class_interval import ClassInterval
from src.models.dataset import Dataset
from src.services.frequency_service import FrequencyService


@pytest.fixture
def service():
    return FrequencyService()


def test_frequencia_discreta_calcula_corretamente(service):
    dataset = Dataset(
        values=[2, 3, 3, 4, 4, 4, 5],
        type_values=TypeValues.DISCRETE,
    )

    distribuicao = service.calculate(dataset)

    assert distribuicao.total == 7
    assert [row.value for row in distribuicao.rows] == [2, 3, 4, 5]
    assert [row.absolute_frequency for row in distribuicao.rows] == [1, 2, 3, 1]
    assert [row.cumulative_frequency for row in distribuicao.rows] == [1, 3, 6, 7]
    assert distribuicao.rows[-1].cumulative_relative_frequency == 1.0


def test_frequencia_discreta_ordena_valores(service):
    dataset = Dataset(
        values=[5, 2, 2, 5, 3],
        type_values=TypeValues.DISCRETE,
    )

    distribuicao = service.calculate(dataset)

    assert [row.value for row in distribuicao.rows] == [2, 3, 5]


def test_frequencia_continua_calcula_por_classe(service):
    dataset = Dataset(
        values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        type_values=TypeValues.CONTINUOUS,
    )

    classes = [
        ClassInterval(lower_bound=1, upper_bound=4, midpoint=2.5),
        ClassInterval(lower_bound=4, upper_bound=7, midpoint=5.5),
        ClassInterval(lower_bound=7, upper_bound=10, midpoint=8.5),
        ClassInterval(lower_bound=10, upper_bound=13, midpoint=11.5),
    ]

    distribuicao = service.calculate(dataset, classes=classes)

    assert distribuicao.total == 12
    assert [row.midpoint for row in distribuicao.rows] == [
        2.5,
        5.5,
        8.5,
        11.5,
    ]
    assert [row.absolute_frequency for row in distribuicao.rows] == [
        3,
        3,
        3,
        3,
    ]
    assert distribuicao.rows[-1].cumulative_frequency == 12


def test_frequencia_continua_respeita_limites(service):
    dataset = Dataset(
        values=[1, 4, 7],
        type_values=TypeValues.CONTINUOUS,
    )

    classes = [
        ClassInterval(lower_bound=1, upper_bound=4, midpoint=2.5),
        ClassInterval(lower_bound=4, upper_bound=7, midpoint=5.5),
    ]

    distribuicao = service.calculate(dataset, classes=classes)

    assert distribuicao.rows[0].absolute_frequency == 1
    assert distribuicao.rows[1].absolute_frequency == 2


def test_frequencia_continua_sem_classes_lanca_erro(service):
    dataset = Dataset(
        values=[1, 2, 3],
        type_values=TypeValues.CONTINUOUS,
    )

    with pytest.raises(ValueError):
        service.calculate(dataset)