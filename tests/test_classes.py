import pytest

from src.services.class_service import ClassService


@pytest.fixture
def service():
    return ClassService()


def test_cria_classes_corretamente(service):
    values = [
        12, 15, 18, 20, 21,
        22, 24, 25, 27, 28,
        29, 30, 31, 33, 34,
        35, 37, 38, 40, 42,
    ]

    classes = service.build_classes(values)

    assert len(classes) == 5
    assert classes[0].lower_bound == 12
    assert classes[-1].upper_bound == 42


def test_valores_iguais_geram_uma_unica_classe(service):
    classes = service.build_classes([5, 5, 5, 5])

    assert len(classes) == 1
    assert classes[0].midpoint == 5


def test_sem_dados_lanca_erro(service):
    with pytest.raises(ValueError):
        service.build_classes([])