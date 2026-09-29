import streamlit as st

from src.charts.chart_service import ChartService
from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.parsers.data_parser import DataParser
from src.services.distribution_service import DistributionService
from src.ui.components.table import create_frequency_dataframe
from src.validators.data_validator import DataValidator


def main():
    st.set_page_config(
        page_title="Tabelas de Frequência",
        layout="wide",
    )

    st.title("Tabelas de Frequência e Gráficos")

    st.write(
        "Insira os dados quantitativos separados por vírgula "
        "para gerar a distribuição de frequência."
    )

    input_data = st.text_area(
        "Dados (ex: 12, 15, 18.5, 20, 25)",
        "",
    )

    variable_type = st.radio(
        "Tipo de Variável",
        ("Discreta", "Contínua"),
    )

    if st.button("Processar Dados"):
        if not input_data.strip():
            st.warning(
                "Por favor, insira os dados para processamento."
            )
            return

        type_val = (
            TypeValues.DISCRETE
            if variable_type == "Discreta"
            else TypeValues.CONTINUOUS
        )

        parser = DataParser()
        validator = DataValidator()
        distribution_service = DistributionService()
        chart_service = ChartService()

        try:
            parsed_data = parser.parse(input_data)

            validator.validate(
                parsed_data,
                type_val,
            )

            dataset = Dataset(
                values=parsed_data,
                type_values=type_val,
            )

            distribution = distribution_service.calculate(
                dataset
            )

            st.success("Dados processados com sucesso!")

            st.subheader("Tabela de Frequência")

            dataframe = create_frequency_dataframe(
                distribution,
                type_val,
            )

            st.dataframe(
                dataframe,
                use_container_width=True,
            )

            st.subheader("Gráficos")

            if type_val == TypeValues.DISCRETE:
                figure = chart_service.build_discrete_chart(
                    distribution
                )

                st.plotly_chart(
                    figure,
                    use_container_width=True,
                )

            else:
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
                    polygon = (
                        chart_service.build_frequency_polygon(
                            distribution
                        )
                    )

                    st.plotly_chart(
                        polygon,
                        use_container_width=True,
                    )

        except ValueError as error:
            st.error(f"Erro de validação: {error}")


if __name__ == "__main__":
    main()