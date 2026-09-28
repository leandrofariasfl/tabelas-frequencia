import pandas as pd

def create_frequency_dataframe(distribution, is_continuous: bool) -> pd.DataFrame:
    """
    Transforma o objeto FrequencyDistribution num DataFrame Pandas 
    formatado para exibição.
    """
    table_data = []
    
    for row in distribution.rows:
        if is_continuous:
            # Cria a string de intervalo (ex: 12 |-- 18)
            interval_str = f"{row.lower_bound} |-- {row.upper_bound}"
            
            table_data.append({
                "Intervalo": interval_str,
                "Ponto médio": row.midpoint,
                "fi": row.absolute_frequency,
                "Fi": row.cumulative_frequency,
                "fr": row.relative_frequency,
                "Fr": row.cumulative_relative_frequency
            })
        else:
            table_data.append({
                "Valor": row.value,
                "fi": row.absolute_frequency,
                "Fi": row.cumulative_frequency,
                "fr": row.relative_frequency,
                "Fr": row.cumulative_relative_frequency
            })
            
    return pd.DataFrame(table_data)