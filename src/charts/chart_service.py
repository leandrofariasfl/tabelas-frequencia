import plotly.graph_objects as go
from src.models.frequency import FrequencyDistribution, ContinuousFrequencyRow

class ChartService:
    @staticmethod
    def criar_histograma(distribuicao: FrequencyDistribution):
        x_labels = []
        
        # Mapeia os rótulos do eixo X dependendo do tipo de dado
        for row in distribuicao.rows:
            if isinstance(row, ContinuousFrequencyRow):
                # Formato padrão de classe estatística: limite_inferior |- limite_superior
                x_labels.append(f"{row.lower_bound} |- {row.upper_bound}")
            else:
                # Para dados discretos, usa apenas o valor exato
                x_labels.append(str(row.value))
                
        # Pega a frequência absoluta para o eixo Y
        y_values = [row.absolute_frequency for row in distribuicao.rows]

        fig = go.Figure(data=[
            go.Bar(
                x=x_labels, 
                y=y_values,
                marker_color='#1f77b4',
                text=y_values,
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            title_text="Histograma de Frequências",
            xaxis_title="Classes / Valores",
            yaxis_title="Frequência Absoluta (fi)",
            bargap=0, # Garante o visual de histograma
            template="plotly_white"
        )
        
        return fig