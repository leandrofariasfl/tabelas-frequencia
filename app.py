import streamlit as st

from src.charts.chart_service import ChartService
from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.parsers.data_parser import DataParser
from src.services.distribution_service import DistributionService
from src.ui.components.table import create_frequency_dataframe
from src.validators.data_validator import DataValidator


def render_header():
    st.title("Tabelas de Frequência e Gráficos")

    st.write(
        "Insira os dados quantitativos separados por vírgula "
        "para gerar a distribuição de frequência."
    )


def render_input():
    input_data = st.text_area(
        "Dados (ex: 12, 15, 18.5, 20, 25)",
        "",
    )

    variable_type = st.radio(
        "Tipo de Variável",
        ("Discreta", "Contínua"),
    )

    st.caption(
        "Discreta: valores contáveis ou pertencentes a um conjunto "
        "específico. Contínua: valores normalmente obtidos por medição."
    )

    process_button = st.button("Processar Dados")

    return input_data, variable_type, process_button


def get_type_value(variable_type: str) -> TypeValues:
    if variable_type == "Discreta":
        return TypeValues.DISCRETE

    return TypeValues.CONTINUOUS


def process_data(
    input_data: str,
    type_value: TypeValues,
):
    parser = DataParser()
    validator = DataValidator()
    distribution_service = DistributionService()

    parsed_data = parser.parse(input_data)

    validator.validate(
        parsed_data,
        type_value,
    )

    dataset = Dataset(
        values=parsed_data,
        type_values=type_value,
    )

    return distribution_service.calculate(dataset)


def render_results(
    distribution,
    type_value: TypeValues,
):
    st.success("Dados processados com sucesso!")

    st.subheader("Tabela de Frequência")

    dataframe = create_frequency_dataframe(
        distribution,
        type_value,
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
    )

    st.subheader("Gráficos")

    chart_service = ChartService()

    if type_value == TypeValues.DISCRETE:
        figure = chart_service.build_discrete_chart(
            distribution
        )

        st.plotly_chart(
            figure,
            use_container_width=True,
        )

        return

    col1, col2 = st.columns(2)

    with col1:
        histogram = chart_service.build_histogram(
            distribution
        )

        st.plotly_chart(
            histogram,
            use_container_width=True,
        )

    with col2:
        polygon = chart_service.build_frequency_polygon(
            distribution
        )

        st.plotly_chart(
            polygon,
            use_container_width=True,
        )


def main():
    st.set_page_config(
        page_title="Tabelas de Frequência",
        layout="wide",
    )

    render_header()

    input_data, variable_type, process_button = render_input()

    if not process_button:
        return

    if not input_data.strip():
        st.warning(
            "Por favor, insira os dados para processamento."
        )
        return

    type_value = get_type_value(variable_type)

    try:
        distribution = process_data(
            input_data,
            type_value,
        )

        render_results(
            distribution,
            type_value,
        )

    except ValueError as error:
        st.error(f"Erro de validação: {error}")


if __name__ == "__main__":
    main()