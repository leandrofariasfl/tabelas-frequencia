import plotly.graph_objects as go

class ChartService:

    def build_discrete_chart(self, distribution):
        x = [str(row.value) for row in distribution.rows]
        y = [row.absolute_frequency for row in distribution.rows]

        fig = go.Figure(data=[go.Bar(x=x, y=y)])
        fig.update_layout(
            title="Gráfico de Barras - Frequência Absoluta",
            xaxis_title="Valores",
            yaxis_title="Frequência",
        )
        return fig

    def build_histogram(self, distribution):
        x = []
        last_index = len(distribution.rows) - 1

        for index, row in enumerate(distribution.rows):
            if index == last_index:
                interval = f"[{row.lower_bound}, {row.upper_bound}]"
            else:
                interval = f"[{row.lower_bound}, {row.upper_bound})"

            x.append(interval)

        y = [row.absolute_frequency for row in distribution.rows]

        fig = go.Figure(data=[go.Bar(x=x, y=y)])

        fig.update_layout(
            title="Histograma",
            xaxis_title="Classes",
            yaxis_title="Frequência",
            bargap=0,
        )

        return fig

    def build_frequency_polygon(self, distribution):
        x = [row.midpoint for row in distribution.rows]
        y = [row.absolute_frequency for row in distribution.rows]

        fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines+markers')])
        fig.update_layout(
            title="Polígono de Frequências",
            xaxis_title="Ponto Médio",
            yaxis_title="Frequência Absoluta",
        )
        return fig
