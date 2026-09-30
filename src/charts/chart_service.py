import plotly.graph_objects as go

from src.models.frequency import FrequencyDistribution


def format_number(value: int | float) -> str:
    return f"{value:.2f}".rstrip("0").rstrip(".")


class ChartService:

    def build_discrete_chart(
        self,
        distribution: FrequencyDistribution,
    ):
        x = [
            str(row.value)
            for row in distribution.rows
        ]

        y = [
            row.absolute_frequency
            for row in distribution.rows
        ]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=x,
                    y=y,
                )
            ]
        )

        fig.update_layout(
            title="Gráfico de Barras - Frequência Absoluta",
            xaxis_title="Valores",
            yaxis_title="Frequência",
        )

        return fig

    def build_histogram(
        self,
        distribution: FrequencyDistribution,
    ):
        intervals = []
        last_index = len(distribution.rows) - 1

        for index, row in enumerate(distribution.rows):
            lower_bound = format_number(row.lower_bound)
            upper_bound = format_number(row.upper_bound)

            if index == last_index:
                interval = f"[{lower_bound}, {upper_bound}]"
            else:
                interval = f"[{lower_bound}, {upper_bound})"

            intervals.append(interval)

        frequencies = [
            row.absolute_frequency
            for row in distribution.rows
        ]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=intervals,
                    y=frequencies,
                )
            ]
        )

        fig.update_layout(
            title="Histograma",
            xaxis_title="Classes",
            yaxis_title="Frequência",
            bargap=0,
        )

        return fig

    def build_frequency_polygon(
        self,
        distribution: FrequencyDistribution,
    ):
        midpoints = [
            row.midpoint
            for row in distribution.rows
        ]

        frequencies = [
            row.absolute_frequency
            for row in distribution.rows
        ]

        fig = go.Figure(
            data=[
                go.Scatter(
                    x=midpoints,
                    y=frequencies,
                    mode="lines+markers",
                )
            ]
        )

        fig.update_layout(
            title="Polígono de Frequências",
            xaxis_title="Ponto Médio",
            yaxis_title="Frequência Absoluta",
        )

        return fig