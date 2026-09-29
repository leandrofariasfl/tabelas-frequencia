# 📊 Tabelas de Frequência e Gráficos para Dados Quantitativos

Aplicação desenvolvida em **Python com Streamlit** para construção automática de tabelas de frequência e gráficos para dados quantitativos discretos e contínuos.

O projeto foi desenvolvido como atividade acadêmica, com foco não apenas no funcionamento da aplicação, mas também em:

- organização do código;
- separação de responsabilidades;
- boas práticas de desenvolvimento;
- testes automatizados;
- trabalho colaborativo com Git e GitHub;
- aplicação dos conceitos estatísticos de distribuição de frequência.

---

## 🎯 Objetivo

Permitir que o usuário informe uma sequência de dados quantitativos e escolha se a variável é:

- **Discreta**
- **Contínua**

A aplicação realiza automaticamente o processamento dos dados, gera a tabela de distribuição de frequência correspondente e apresenta os gráficos adequados para cada tipo de variável.

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

## 📐 Regras estatísticas utilizadas

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

Onde `N` representa o número total de observações.

---

### Frequência relativa acumulada

```text
Fr = Fi / N
```

Na aplicação, os valores são armazenados internamente como proporções e formatados como porcentagens na camada de apresentação.

---

## 📏 Construção das classes

Para dados contínuos, a quantidade de classes é determinada utilizando a **Regra de Sturges**:

```text
k = 1 + 3.322 × log10(n)
```

Onde:

- `k` = quantidade de classes;
- `n` = quantidade de observações.

O resultado é arredondado para o inteiro mais próximo.

A amplitude total é calculada por:

```text
A = valor máximo - valor mínimo
```

A largura de cada classe é calculada por:

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

- limite inferior incluído;
- limite superior excluído.

A última classe inclui também o limite superior:

```text
[limite inferior, limite superior]
```

Isso garante que o maior valor do conjunto de dados pertença à distribuição.

---

## 📊 Gráficos

### Variável discreta

Para dados discretos é utilizado um **gráfico de barras**.

- eixo X: valores observados;
- eixo Y: frequência absoluta.

---

### Variável contínua

Para dados contínuos são utilizados dois gráficos.

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
6. receber mensagens de erro para entradas inválidas.

Os valores devem ser separados por vírgula.

Exemplo:

```text
10, 15, 20, 25, 30
```

Para casas decimais, deve ser utilizado ponto:

```text
10.5, 12.7, 15.2
```

A vírgula é reservada para separar as observações.

---

## 🛠️ Tecnologias utilizadas

O projeto utiliza:

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **pytest**

### Python

Responsável por toda a lógica da aplicação.

### Streamlit

Utilizado para construção da interface web.

### Pandas

Utilizado na camada de apresentação para criação das tabelas exibidas ao usuário.

### Plotly

Utilizado para geração dos gráficos interativos.

### pytest

Utilizado para testes automatizados das principais regras do sistema.

---

## 🏗️ Arquitetura

O projeto foi desenvolvido buscando separar as responsabilidades entre diferentes módulos.

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

Ponto de entrada da aplicação Streamlit.

Responsável por:

- receber a entrada do usuário;
- selecionar o tipo da variável;
- iniciar o fluxo de processamento;
- exibir tabela;
- exibir gráficos;
- apresentar mensagens de validação.

As regras estatísticas não ficam concentradas nesse arquivo.

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

Também identifica entradas malformadas, como campos vazios ou valores que não representam números.

---

### `DataValidator`

Responsável por validar os dados já convertidos.

Entre as validações estão:

- conjunto de dados vazio;
- valores não numéricos;
- compatibilidade com o tipo da variável.

Para dados discretos, os valores devem representar números inteiros.

---

### `Dataset`

Modelo que representa o conjunto de dados utilizado pela aplicação.

Contém:

```text
values
type_values
```

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

Responsável por construir automaticamente as classes dos dados contínuos.

Realiza:

- cálculo do mínimo;
- cálculo do máximo;
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

---

### `DistributionService`

Atua como serviço de orquestração.

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

Isso evita que a interface precise conhecer detalhes do processamento estatístico.

---

### `FrequencyRow`

Representa uma linha de frequência de dados discretos.

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

Representa uma linha de distribuição contínua.

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

Representa o resultado final de uma distribuição de frequência.

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

A camada de gráficos recebe resultados já processados e não recalcula frequências.

---

### `table.py`

Responsável por transformar uma `FrequencyDistribution` em um `DataFrame` apropriado para apresentação.

Também realiza a formatação das frequências relativas em porcentagem e dos intervalos das classes.

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

O Streamlit abrirá a aplicação no navegador.

Caso não abra automaticamente, o terminal exibirá o endereço local da aplicação.

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

- criação de classes;
- distribuição de frequência;
- dados discretos;
- dados contínuos;
- limites das classes;
- serviço de distribuição.

No estado atual do projeto:

```text
10 testes passando
```

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

O sistema deverá gerar os valores:

```text
2
3
4
5
```

com frequências absolutas:

```text
4
3
1
2
```

Além disso, deverá apresentar:

- tabela de frequência;
- frequências relativas;
- frequências acumuladas;
- gráfico de barras.

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
- gerar a distribuição de frequência;
- apresentar o histograma;
- apresentar o polígono de frequência.

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

### Valor incompatível com variável discreta

Exemplo:

```text
1, 2.5, 3
```

quando o tipo selecionado é discreto.

O sistema apresenta mensagens amigáveis para o usuário em vez de interromper a aplicação.

---

## 🌿 Git e organização da equipe

O desenvolvimento foi realizado utilizando Git e GitHub.

Foi adotado um fluxo baseado em branches.

Algumas branches utilizadas durante o desenvolvimento:

```text
feat/tabela-frequencia
feat/frequency-table
feat/interface-streamlit
refactor/frequency-service
refactor/frequency-table
refactor/interface-streamlit
```

A branch `main` foi utilizada como versão estável do projeto.

Novas funcionalidades foram desenvolvidas em branches separadas, revisadas e posteriormente integradas à `main`.

---

## 📝 Padrão de commits

O projeto adotou mensagens de commit inspiradas em **Conventional Commits**.

Exemplos:

```text
feat: adiciona DistributionService
feat: adiciona componente de tabela
refactor: aprimora componente de tabela
refactor: modela classes de frequência contínuas
fix: corrige representação dos intervalos
test: adiciona testes de distribuição
docs: atualiza documentação do projeto
```

Principais prefixos:

| Prefixo | Uso |
|---|---|
| `feat` | nova funcionalidade |
| `fix` | correção |
| `refactor` | reorganização sem alteração da funcionalidade |
| `test` | testes |
| `docs` | documentação |
| `chore` | tarefas de manutenção |

---

## 🧠 Decisões de projeto

### Separação entre parsing e validação

O `DataParser` interpreta a entrada textual.

O `DataValidator` valida os dados já convertidos.

---

### Separação entre estatística e interface

Os cálculos estatísticos não dependem do Streamlit.

Isso permite que as regras sejam testadas de forma independente da interface.

---

### Serviços independentes

O `ClassService` é responsável pela criação das classes.

O `FrequencyService` é responsável pelos cálculos de frequência.

O `DistributionService` coordena o fluxo entre esses serviços.

---

### Representação diferente para dados discretos e contínuos

Dados discretos utilizam:

```text
FrequencyRow
```

Dados contínuos utilizam:

```text
ContinuousFrequencyRow
```

Isso evita campos opcionais desnecessários e torna os modelos mais claros.

---

### Gráficos separados da regra estatística

O `ChartService` recebe resultados já processados.

Nenhuma frequência é recalculada durante a geração dos gráficos.

---

### Apresentação da tabela separada da lógica principal

A criação do `DataFrame` foi isolada em:

```text
src/ui/components/table.py
```

Assim, o `app.py` fica responsável principalmente pela orquestração da interface.

---

## 🔮 Possíveis melhorias futuras

O projeto foi desenvolvido de acordo com o escopo acadêmico proposto.

Possíveis evoluções futuras incluem:

- exportação das tabelas;
- exportação dos gráficos;
- personalização do número de classes;
- escolha do método de determinação das classes;
- melhorias visuais na interface;
- implantação da aplicação na nuvem;
- novos tipos de visualização;
- ampliação da cobertura de testes.

Essas funcionalidades não fazem parte do escopo atual.

---

## 👥 Equipe

Projeto desenvolvido em grupo para atividade acadêmica.

Integrantes:

- Nome do integrante 1
- Nome do integrante 2
- Nome do integrante 3
- Nome do integrante 4
- Nome do integrante 5

---

## 📚 Contexto acadêmico

Projeto desenvolvido para aplicação prática dos conceitos de:

- dados quantitativos;
- variáveis discretas;
- variáveis contínuas;
- tabelas de frequência;
- frequência absoluta;
- frequência acumulada;
- frequência relativa;
- frequência relativa acumulada;
- distribuição em classes;
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