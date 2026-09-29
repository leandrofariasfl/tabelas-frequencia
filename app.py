import streamlit as st
from src.ui.components.charts import renderizar_histograma
from src.services.frequency_service import FrequencyService
from src.models.dataset import Dataset
from src.enums.enums import TypeValues

def main():
    st.title("Tabelas de Frequência")
    
    # 1. Dados brutos simulados (no futuro, virão de um input do usuário)
    valores_brutos = [12, 15, 15, 18, 20, 22, 22, 22, 25, 30, 31, 35, 40, 42]
    
    # 2. Monta o modelo Dataset conforme exigido pelo seu serviço
    # Usando DISCRETE para simplificar o teste direto sem precisar gerar as classes
    dataset = Dataset(values=valores_brutos, type_values=TypeValues.DISCRETE)
    
    # 3. Instancia o serviço e calcula
    servico_frequencia = FrequencyService()
    distribuicao = servico_frequencia.calculate(dataset=dataset)
    
    # 4. Renderiza o gráfico enviando a distribuição calculada
    renderizar_histograma(distribuicao)

if __name__ == "__main__":
    main()