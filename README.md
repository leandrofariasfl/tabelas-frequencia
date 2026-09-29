# 📊 Tabelas de Frequência e Gráficos para Dados Quantitativos

Aplicação desenvolvida em **Python com Streamlit** para construção automática de tabelas de frequência e gráficos para dados quantitativos discretos e contínuos.

O projeto foi desenvolvido como atividade acadêmica, com foco em:

- aplicação prática de conceitos estatísticos;
- organização do código;
- separação de responsabilidades;
- testes automatizados;
- desenvolvimento colaborativo com Git e GitHub;
- construção de uma interface simples para exploração de distribuições de frequência.

---

## 🎯 Objetivo

Permitir que o usuário informe uma sequência de dados quantitativos e escolha se a variável é:

- **Discreta**
- **Contínua**

A aplicação processa os dados, gera automaticamente a distribuição de frequência correspondente e apresenta os gráficos adequados para cada tipo de variável.

---

## 🚀 Funcionalidades

### Dados discretos

Para variáveis quantitativas discretas, o sistema:

- identifica os valores distintos;
- ordena os valores;
- calcula a frequência absoluta (`fi`);
- calcula a frequência absoluta acumulada (`Fi`);
- calcula a frequência relativa (`fr`);
- calcula a frequência relativa acumulada (`Fr`);
- gera uma tabela de frequência;
- gera um gráfico de barras.

Exemplo de entrada:

```text
2, 3, 2, 5, 3, 2, 4, 5, 3, 2
```

Exemplo de resultado:

| Valor | fi | Fi | fr | Fr |
|------:|---:|---:|---:|---:|
| 2 | 4 | 4 | 40% | 40% |
| 3 | 3 | 7 | 30% | 70% |
| 4 | 1 | 8 | 10% | 80% |
| 5 | 2 | 10 | 20% | 100% |

---

### Dados contínuos

Para variáveis quantitativas contínuas, o sistema:

- identifica o menor e o maior valor;
- calcula a amplitude total;
- determina automaticamente a quantidade de classes;
- calcula a largura das classes;
- cria os intervalos;
- calcula o ponto médio de cada classe;
- calcula `fi`, `Fi`, `fr` e `Fr`;
- gera a tabela de frequência;
- gera um histograma;
- gera um polígono de frequência.

Exemplo de entrada:

```text
12, 15, 18, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 33, 34, 35, 37, 38, 40, 42
```

---

## 📐 Conceitos estatísticos utilizados

### Frequência absoluta

A frequência absoluta representa quantas vezes determinado valor ou classe aparece no conjunto de dados.

```text
fi
```

---

### Frequência absoluta acumulada

É a soma progressiva das frequências absolutas.

```text
Fi = soma acumulada de fi
```

---

### Frequência relativa

A frequência relativa indica a proporção de observações pertencentes a determinado valor ou classe.

```text
fr = fi / N
```

Onde:

```text
N = número total de observações
```

---

### Frequência relativa acumulada

```text
Fr = Fi / N
```

Internamente, os valores são armazenados como proporções e convertidos para porcentagem na camada de apresentação.

---

## 📏 Construção das classes

Para dados contínuos, a quantidade de classes é determinada utilizando a **Regra de Sturges**:

```text
k = 1 + 3.322 × log10(n)
```

Onde:

- `k` = quantidade de classes;
- `n` = número de observações.

O resultado é arredondado para o inteiro mais próximo.

A amplitude total é calculada por:

```text
A = valor máximo - valor mínimo
```

A largura das classes é calculada por:

```text
h = A / k
```

---

### Convenção dos intervalos

As classes intermediárias seguem a convenção:

```text
[limite inferior, limite superior)
```

Ou seja:

- o limite inferior pertence à classe;
- o limite superior não pertence à classe.

A última classe inclui também o limite superior:

```text
[limite inferior, limite superior]
```

Isso garante que o maior valor do conjunto seja incluído na distribuição.

---

## 🔎 Escolha do tipo da variável

A classificação entre variável discreta e contínua depende da **natureza da variável**, e não apenas da forma como os números são escritos.

De maneira geral:

- **Discreta:** representa valores contáveis ou pertencentes a um conjunto específico de possibilidades.
- **Contínua:** representa valores normalmente obtidos por medição e que podem assumir diferentes valores dentro de um intervalo.

Exemplos:

| Tipo | Exemplos |
|---|---|
| Discreta | número de filhos, quantidade de faltas, número de defeitos |
| Contínua | altura, peso, temperatura, tempo |

> A presença de casas decimais, isoladamente, não significa que uma variável seja contínua.

Por esse motivo, a aplicação solicita que o usuário informe o tipo da variável antes do processamento.

---

## 📊 Gráficos

### Variável discreta

Para dados discretos é utilizado um **gráfico de barras**.

- eixo X: valores observados;
- eixo Y: frequência absoluta.

---

### Variável contínua

Para dados contínuos são utilizados:

#### Histograma

- eixo X: classes;
- eixo Y: frequência absoluta;
- barras sem espaçamento entre as classes.

#### Polígono de frequência

- eixo X: ponto médio das classes;
- eixo Y: frequência absoluta;
- os pontos são conectados por segmentos.

---

## 🖥️ Interface

A interface foi construída utilizando **Streamlit**.

O usuário pode:

1. inserir os dados;
2. selecionar o tipo da variável;
3. solicitar o processamento;
4. visualizar a tabela de frequência;
5. visualizar os gráficos;
6. receber mensagens amigáveis para entradas inválidas.

Os valores devem ser separados por vírgula.

Exemplo:

```text
10, 15, 20, 25, 30
```

Para valores decimais, deve ser utilizado ponto:

```text
10.5, 12.7, 15.2
```

A vírgula é utilizada como separador entre as observações.

---

## 🛠️ Tecnologias utilizadas

O projeto utiliza:

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **pytest**

### Python

Responsável pela lógica principal da aplicação.

### Streamlit

Utilizado na construção da interface web.

### Pandas

Utilizado na camada de apresentação para criação das tabelas exibidas ao usuário.

### Plotly

Utilizado para criação dos gráficos interativos.

### pytest

Utilizado para testes automatizados das principais regras da aplicação.

---

## 🏗️ Arquitetura

O projeto foi estruturado buscando separar claramente as responsabilidades entre os módulos.

Fluxo principal:

```text
Entrada do usuário
        ↓
    DataParser
        ↓
list[int | float]
        ↓
   DataValidator
        ↓
      Dataset
        ↓
DistributionService
        ↓
FrequencyDistribution
        ↓
Tabela + Gráficos
```

Para dados contínuos:

```text
Dataset
   ↓
ClassService
   ↓
ClassInterval
   ↓
FrequencyService
   ↓
FrequencyDistribution
```

---

## 📁 Estrutura do projeto

```text
tabelas-frequencia/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   │
│   ├── charts/
│   │   └── chart_service.py
│   │
│   ├── enums/
│   │   └── enums.py
│   │
│   ├── models/
│   │   ├── dataset.py
│   │   ├── frequency.py
│   │   └── class_interval.py
│   │
│   ├── parsers/
│   │   └── data_parser.py
│   │
│   ├── services/
│   │   ├── class_service.py
│   │   ├── distribution_service.py
│   │   └── frequency_service.py
│   │
│   ├── ui/
│   │   └── components/
│   │       └── table.py
│   │
│   └── validators/
│       └── data_validator.py
│
└── tests/
    ├── test_classes.py
    ├── test_distribution.py
    └── test_frequency.py
```

---

## 🧩 Responsabilidade dos módulos

### `app.py`

É o ponto de entrada da aplicação Streamlit.

A função `main()` atua principalmente como orquestradora do fluxo da interface.

Para evitar concentrar todas as responsabilidades em uma única função, o arquivo foi dividido em funções auxiliares:

```text
main()
│
├── render_header()
├── render_input()
├── get_type_value()
├── process_data()
└── render_results()
```

Responsabilidades:

- `render_header()` → apresenta o título e a descrição da aplicação;
- `render_input()` → recebe os dados e o tipo da variável;
- `get_type_value()` → converte a opção selecionada para `TypeValues`;
- `process_data()` → conecta Parser, Validator, Dataset e serviços;
- `render_results()` → apresenta tabela e gráficos;
- `main()` → coordena o fluxo geral da aplicação.

As regras estatísticas continuam isoladas nos serviços.

---

### `DataParser`

Responsável por transformar a entrada textual do usuário em uma lista de valores numéricos.

Exemplo:

```text
"12, 15, 18.5"
```

é convertido para:

```python
[12, 15, 18.5]
```

Também identifica problemas de entrada, como:

- campos vazios;
- valores que não representam números.

---

### `DataValidator`

Responsável por validar os dados já convertidos.

Entre as validações estão:

- conjunto de dados vazio;
- valores não numéricos;
- tipo de variável inválido.

A aplicação não determina se uma variável é discreta ou contínua apenas pela presença de valores inteiros ou decimais.

O tipo da variável é informado pelo usuário de acordo com a natureza estatística dos dados.

---

### `Dataset`

Modelo que representa o conjunto de dados utilizado pela aplicação.

Contém:

```text
values
type_values
```

---

### `TypeValues`

Enum utilizado para representar os dois tipos de variável suportados:

```text
DISCRETE
CONTINUOUS
```

Evita o uso de strings soltas ao longo da aplicação.

---

### `ClassInterval`

Representa uma classe utilizada em distribuições contínuas.

Contém:

```text
lower_bound
upper_bound
midpoint
```

---

### `ClassService`

Responsável pela criação automática das classes para dados contínuos.

Realiza:

- identificação do menor valor;
- identificação do maior valor;
- cálculo da amplitude;
- cálculo da quantidade de classes;
- cálculo da largura das classes;
- construção dos intervalos;
- cálculo dos pontos médios.

---

### `FrequencyService`

Responsável pelos cálculos de frequência.

Calcula:

```text
fi
Fi
fr
Fr
```

para distribuições discretas e contínuas.

Para variáveis discretas, as frequências são calculadas por valor.

Para variáveis contínuas, as frequências são calculadas por classe.

---

### `DistributionService`

Atua como serviço de orquestração do processamento estatístico.

Para dados discretos:

```text
Dataset
   ↓
FrequencyService
```

Para dados contínuos:

```text
Dataset
   ↓
ClassService
   ↓
FrequencyService
```

Isso evita que a interface conheça detalhes da lógica estatística.

---

### `FrequencyRow`

Representa uma linha da distribuição de frequência para dados discretos.

Contém:

```text
value
absolute_frequency
cumulative_frequency
relative_frequency
cumulative_relative_frequency
```

---

### `ContinuousFrequencyRow`

Representa uma linha da distribuição para dados contínuos.

Contém:

```text
lower_bound
upper_bound
midpoint
absolute_frequency
cumulative_frequency
relative_frequency
cumulative_relative_frequency
```

---

### `FrequencyDistribution`

Representa o resultado final da distribuição de frequência.

Contém:

```text
rows
total
```

---

### `ChartService`

Responsável exclusivamente pela criação dos gráficos.

Disponibiliza:

- gráfico de barras;
- histograma;
- polígono de frequência.

O `ChartService` recebe resultados já processados e não recalcula as frequências.

---

### `table.py`

Responsável por transformar uma `FrequencyDistribution` em um `DataFrame` adequado para apresentação.

Também realiza:

- formatação dos intervalos;
- formatação das frequências relativas em porcentagem;
- diferenciação visual entre dados discretos e contínuos.

---

## ❌ Tratamento de erros

A aplicação possui validações para situações como:

### Entrada vazia

```text
""
```

### Campos vazios

```text
12, 15, , 20
```

### Valores não numéricos

```text
12, abc, 20
```

### Tipo de variável inválido

Internamente, o sistema verifica se o tipo informado pertence às opções definidas em `TypeValues`.

A escolha entre variável discreta e contínua é realizada pelo usuário com base na natureza dos dados, e não pela existência ou ausência de casas decimais.

Os erros de entrada são apresentados de forma amigável na interface.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/leandrofariasfl/tabelas-frequencia.git
```

Entre na pasta:

```bash
cd tabelas-frequencia
```

---

### 2. Crie um ambiente virtual

#### Windows

```bash
python -m venv .venv
```

Ative:

```bash
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a aplicação

Com o ambiente virtual ativado:

```bash
streamlit run app.py
```

O Streamlit deverá abrir a aplicação no navegador.

Caso isso não aconteça automaticamente, o terminal exibirá o endereço local.

Normalmente:

```text
http://localhost:8501
```

---

## 🧪 Executando os testes

Com o ambiente virtual ativado:

```bash
pytest
```

O projeto possui testes automatizados para as principais regras relacionadas a:

- construção de classes;
- distribuição de frequência;
- dados discretos;
- dados contínuos;
- limites dos intervalos;
- orquestração da distribuição.

A suíte de testes deve ser executada antes da integração de novas alterações à `main`.

---

## ✅ Exemplos para teste manual

### Dados discretos

Selecione:

```text
Discreta
```

Digite:

```text
2, 3, 2, 5, 3, 2, 4, 5, 3, 2
```

Resultado esperado:

```text
Valor 2 → fi = 4
Valor 3 → fi = 3
Valor 4 → fi = 1
Valor 5 → fi = 2
```

Além da tabela, deverá ser apresentado um gráfico de barras.

---

### Dados contínuos

Selecione:

```text
Contínua
```

Digite:

```text
12, 15, 18, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 33, 34, 35, 37, 38, 40, 42
```

O sistema deverá:

- criar automaticamente as classes;
- calcular os pontos médios;
- calcular as frequências;
- apresentar a tabela;
- apresentar o histograma;
- apresentar o polígono de frequência.

---

## 🌿 Git e organização do desenvolvimento

O projeto utiliza Git e GitHub para controle de versão e desenvolvimento colaborativo.

A branch:

```text
main
```

representa a versão estável do projeto.

Novas funcionalidades e alterações foram desenvolvidas em branches separadas.

Exemplos utilizados durante o desenvolvimento:

```text
feat/tabela-frequencia
feat/frequency-table
feat/interface-streamlit
refactor/frequency-service
refactor/frequency-table
refactor/interface-streamlit
fix/variable-type-validation
refactor/app-structure
```

Fluxo adotado:

```text
main
 ↓
feature / fix / refactor
 ↓
desenvolvimento
 ↓
testes
 ↓
revisão
 ↓
merge na main
```

---

## 📝 Padrão de commits

O projeto utiliza mensagens inspiradas em **Conventional Commits**.

Principais prefixos:

| Prefixo | Uso |
|---|---|
| `feat` | nova funcionalidade |
| `fix` | correção |
| `refactor` | reorganização sem alterar a funcionalidade |
| `test` | testes |
| `docs` | documentação |
| `chore` | manutenção |

Exemplos:

```text
feat: adiciona DistributionService
feat: adiciona componente de tabela
refactor: modela classes de frequência contínuas
refactor: reorganiza estrutura da aplicação
fix: corrige validação do tipo de variável
docs: atualiza documentação da arquitetura
```

---

## 🧠 Decisões de projeto

### Separação entre parsing e validação

O `DataParser` é responsável por interpretar a entrada textual.

O `DataValidator` é responsável por validar os dados já convertidos.

Isso evita misturar transformação de dados com regras de validação.

---

### Separação entre Estatística e interface

As regras estatísticas não dependem do Streamlit.

Isso permite testar o processamento de forma independente da interface.

---

### Serviços independentes

O `ClassService` é responsável pela criação das classes.

O `FrequencyService` é responsável pelos cálculos de frequência.

O `DistributionService` coordena esses serviços.

---

### O tipo estatístico não é inferido pelo tipo numérico

Inicialmente, valores discretos eram restringidos a números inteiros.

Essa regra foi revisada porque, estatisticamente, a presença de casas decimais não determina por si só se uma variável é discreta ou contínua.

Por isso, a aplicação passou a utilizar a classificação fornecida pelo usuário de acordo com a natureza da variável.

---

### Representações diferentes para dados discretos e contínuos

Dados discretos utilizam:

```text
FrequencyRow
```

Dados contínuos utilizam:

```text
ContinuousFrequencyRow
```

Essa separação mantém os modelos mais claros e evita campos opcionais desnecessários.

---

### Gráficos separados da regra estatística

O `ChartService` recebe resultados já calculados.

Nenhuma frequência é recalculada durante a geração dos gráficos.

---

### Apresentação da tabela separada da lógica principal

A criação da tabela foi isolada em:

```text
src/ui/components/table.py
```

Assim, o `app.py` não precisa montar manualmente os `DataFrames`.

---

### `main()` como função de orquestração

O `app.py` foi refatorado para evitar uma função principal excessivamente grande.

A função `main()` mantém apenas o fluxo geral da aplicação, enquanto tarefas de entrada, processamento e apresentação foram separadas em funções menores.

Essa organização melhora:

- legibilidade;
- manutenção;
- separação de responsabilidades;
- compreensão do fluxo da aplicação.

---

## 🔮 Possíveis melhorias futuras

O projeto foi desenvolvido de acordo com o escopo acadêmico proposto.

Possíveis evoluções futuras incluem:

- exportação das tabelas;
- exportação dos gráficos;
- personalização da quantidade de classes;
- escolha de outros métodos para determinação das classes;
- melhorias visuais na interface;
- implantação pública da aplicação;
- ampliação da cobertura de testes;
- inclusão de novos tipos de visualização.

Essas funcionalidades não fazem parte do escopo atual.

---

## 📚 Contexto acadêmico

O projeto foi desenvolvido para aplicação prática dos conceitos de:

- dados quantitativos;
- variáveis discretas;
- variáveis contínuas;
- tabelas de frequência;
- frequência absoluta;
- frequência absoluta acumulada;
- frequência relativa;
- frequência relativa acumulada;
- distribuição em classes;
- amplitude;
- Regra de Sturges;
- ponto médio;
- histogramas;
- polígonos de frequência.

Além dos conceitos estatísticos, o desenvolvimento também explorou práticas de engenharia de software como:

- modularização;
- separação de responsabilidades;
- testes automatizados;
- versionamento de código;
- desenvolvimento colaborativo;
- revisão de código;
- organização em branches.

---

## 📄 Licença

Este projeto possui finalidade acadêmica e educacional.