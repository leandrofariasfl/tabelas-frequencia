import streamlit as st
import pandas as pd

from src.enums.enums import TypeValues
from src.models.dataset import Dataset
from src.parsers.data_parser import DataParser
from src.validators.data_validator import DataValidator
from src.services.distribution_service import DistributionService
from src.charts.chart_service import ChartService

def main():
    st.set_page_config(page_title="Tabelas de Frequência", layout="wide")
    st.title("Tabelas de Frequência e Gráficos")

    st.write("Insira os dados quantitativos separados por vírgula para gerar a distribuição de frequência.")

    input_data = st.text_area("Dados (ex: 12, 15, 18.5, 20, 25)", "")

    variable_type = st.radio(
        "Tipo de Variável",
        ("Discreta", "Contínua")
    )

    if st.button("Processar Dados"):
        if not input_data.strip():
            st.warning("Por favor, insira os dados para processamento.")
            return

        type_val = TypeValues.DISCRETE if variable_type == "Discreta" else TypeValues.CONTINUOUS

        parser = DataParser()
        validator = DataValidator()
        distribution_service = DistributionService()
        chart_service = ChartService()

        try:
            # Parse data
            parsed_data = parser.parse(input_data)

            # Validate data
            validator.validate(parsed_data, type_val)

            # Create Dataset
            dataset = Dataset(values=parsed_data, type_values=type_val)

            # Calculate Distribution
            distribution = distribution_service.calculate(dataset)

            # Display Results
            st.success("Dados processados com sucesso!")
            
            st.subheader("Tabela de Frequência")
            
            # Format table based on type
            if type_val == TypeValues.DISCRETE:
                df = pd.DataFrame([
                    {
                        "Valor": row.value,
                        "fi": row.absolute_frequency,
                        "Fi": row.cumulative_frequency,
                        "fr": round(row.relative_frequency, 4),
                        "Fr": round(row.cumulative_relative_frequency, 4)
                    }
                    for row in distribution.rows
                ])
                st.dataframe(df, use_container_width=True)

                st.subheader("Gráficos")
                fig = chart_service.build_discrete_chart(distribution)
                st.plotly_chart(fig, use_container_width=True)

            else:
                df = pd.DataFrame([
                    {
                        "Classe": i + 1,
                        "Intervalo": f"[{row.lower_bound}, {row.upper_bound})",
                        "Ponto Médio": row.midpoint,
                        "fi": row.absolute_frequency,
                        "Fi": row.cumulative_frequency,
                        "fr": round(row.relative_frequency, 4),
                        "Fr": round(row.cumulative_relative_frequency, 4)
                    }
                    for i, row in enumerate(distribution.rows)
                ])
                # Corrigindo a formatação do último intervalo conforme a regra de classes inclusivas no fim
                if len(distribution.rows) > 0:
                    last_row = distribution.rows[-1]
                    df.at[len(distribution.rows)-1, "Intervalo"] = f"[{last_row.lower_bound}, {last_row.upper_bound}]"
                
                st.dataframe(df, use_container_width=True)

                st.subheader("Gráficos")
                col1, col2 = st.columns(2)
                with col1:
                    fig_hist = chart_service.build_histogram(distribution)
                    st.plotly_chart(fig_hist, use_container_width=True)
                with col2:
                    fig_poly = chart_service.build_frequency_polygon(distribution)
                    st.plotly_chart(fig_poly, use_container_width=True)

        except ValueError as e:
            st.error(f"Erro de Validação: {e}")
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
