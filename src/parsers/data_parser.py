class DataParser:

    def parse(self, data):
        values = self._split_values(data)
        values = self._clean_values(values)
        values = self._convert_values(values)

        return values

    def _split_values(self, data):
        return data.split(",")

    def _clean_values(self, values):
        cleaned_values = []

        for value in values:
            value = value.strip()

            if value == "":
                raise ValueError("Os dados não podem conter campos vazios.")

            cleaned_values.append(value)

        return cleaned_values

    def _convert_values(self, values):
        converted_values = []

        for value in values:
            try:
                number = float(value)

                if number.is_integer():
                    number = int(number)

                converted_values.append(number)

            except ValueError:
                raise ValueError(
                    f"O valor '{value}' não representa um número válido."
                )

        return converted_values