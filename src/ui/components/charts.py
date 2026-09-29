import streamlit as st
from src.charts.chart_service import ChartService
from src.models.frequency import FrequencyDistribution

def renderizar_histograma(distribuicao: FrequencyDistribution):
    st.subheader("Visualização - Histograma")
    figura = ChartService.criar_histograma(distribuicao)
    st.plotly_chart(figura, use_container_width=True)