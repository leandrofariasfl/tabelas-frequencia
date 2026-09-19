from src.enums.enums import TypeValues

class DataValidator:

    def validate(self, data, type_values):
        self._validate_not_empty(data)
        self._validate_numeric(data)
        self._validate_variable_type(data, type_values)

    def _validate_not_empty(self, data):
        if not data:
            raise ValueError("Os dados não podem estar vazios.")

    def _validate_numeric(self, data):
        for value in data:
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"O valor '{value}' não representa um número válido."
                )

    def _validate_variable_type(self, data, type_values):
        if not isinstance(type_values, TypeValues):
            raise ValueError("O tipo da variável é inválido.")

        if type_values == TypeValues.DISCRETE:
            for value in data:
                if not float(value).is_integer():
                    raise ValueError(
                        "Variáveis discretas devem possuir valores inteiros."
                    )