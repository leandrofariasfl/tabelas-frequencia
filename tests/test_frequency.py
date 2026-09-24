import pytest

from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.services.frequency_service import FrequencyService


@pytest.fixture
def service():
    return FrequencyService()


def test_frequencia_discreta_calcula_absoluta_e_acumulada(service):
    dataset = Dataset(values=[2, 3, 3, 4, 4, 4, 5], type_values=TypeValues.DISCRETE)

    distribuicao = service.calculate(dataset)

    assert distribuicao.total == 7
    assert [row.value for row in distribuicao.rows] == [2, 3, 4, 5]
    assert [row.absolute_frequency for row in distribuicao.rows] == [1, 2, 3, 1]
    assert [row.cumulative_frequency for row in distribuicao.rows] == [1, 3, 6, 7]


def test_frequencia_discreta_calcula_relativa_e_relativa_acumulada(service):
    dataset = Dataset(values=[1, 1, 2, 2], type_values=TypeValues.DISCRETE)

    distribuicao = service.calculate(dataset)

    assert distribuicao.rows[0].relative_frequency == 0.5
    assert distribuicao.rows[1].relative_frequency == 0.5
    assert distribuicao.rows[-1].cumulative_relative_frequency == 1.0


def test_frequencia_discreta_ordena_valores_repetidos_fora_de_ordem(service):
    dataset = Dataset(values=[5, 2, 2, 5, 3], type_values=TypeValues.DISCRETE)

    distribuicao = service.calculate(dataset)

    assert [row.value for row in distribuicao.rows] == [2, 3, 5]


def test_frequencia_continua_calcula_por_classe(service):
    dataset = Dataset(
        values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        type_values=TypeValues.CONTINUOUS,
    )

    classes = [(1, 4), (4, 7), (7, 10), (10, 13)]

    distribuicao = service.calculate(dataset, classes=classes)

    assert distribuicao.total == 12

    assert [row.midpoint for row in distribuicao.rows] == [
        2.5,
        5.5,
        8.5,
        11.5,
    ]

    assert [
        (row.lower_bound, row.upper_bound)
        for row in distribuicao.rows
    ] == [
        (1, 4),
        (4, 7),
        (7, 10),
        (10, 13),
    ]

    assert [row.absolute_frequency for row in distribuicao.rows] == [
        3,
        3,
        3,
        3,
    ]

    assert distribuicao.rows[-1].cumulative_frequency == 12

def test_frequencia_continua_inclui_limite_superior_apenas_na_ultima_classe(service):
    dataset = Dataset(values=[1, 4, 7], type_values=TypeValues.CONTINUOUS)
    classes = [(1, 4), (4, 7)]

    distribuicao = service.calculate(dataset, classes=classes)

    # o valor 4 deve cair na segunda classe (limite inferior), não na primeira
    assert distribuicao.rows[0].absolute_frequency == 1  # apenas o valor 1
    # o valor 7 deve cair na segunda classe pois é a última (limite superior incluso)
    assert distribuicao.rows[1].absolute_frequency == 2  # valores 4 e 7


def test_frequencia_continua_sem_classes_lanca_erro(service):
    dataset = Dataset(values=[1, 2, 3], type_values=TypeValues.CONTINUOUS)

    with pytest.raises(ValueError):
        service.calculate(dataset)