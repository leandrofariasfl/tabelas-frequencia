# Sistema Estatístico - Tabelas e Gráficos de Frequência

Bem-vindos ao repositório do nosso projeto de Estatística! Este sistema recebe dados quantitativos, processa cálculos estatísticos rigorosos e gera tabelas de frequência (absoluta, relativa e acumuladas) e gráficos interativos.

---

## Arquitetura do Projeto

Nosso projeto segue o padrão `src/`, separando regras de negócio da interface. Isso evita conflitos e facilita testes.

    projeto-estatistica/
    ├── .github/                    # Configurações do repositório
    ├── app.py                      # Ponto de entrada para rodar o site (Streamlit)
    ├── tests/                      # Testes automatizados (pytest)
    │   ├── test_classes.py         # Testes de cálculo de classes
    │   ├── test_frequency.py       # Testes de tabelas de frequência
    │   └── test_validation.py      # Testes de validação de dados
    └── src/                        # Código fonte principal da aplicação
        ├── enums/                  # Enums de domínio
        │   └── enums.py            # TypeValues (contínuo, discreto)
        ├── parsers/                 # Processamento e parsing dos dados de entrada
        │   └── data_parser.py      # DataParser: split, limpeza e conversão dos dados
        ├── validators/              # Regras de validação (dados corretos, etc.)
        │   └── data_validator.py   # Validação dos dados recebidos
        ├── models/                  # Estruturas de dados
        │   └── dataset.py          # Dataset: dataclass com values e type_values
        ├── services/                 # Motor estatístico (cálculo de fi, fr, classes, etc.)
        │   ├── class_service.py    # Cálculo de classes (em construção)
        │   └── frequency_service.py # Cálculo das tabelas de frequência (em construção)
        ├── charts/                  # Funções geradoras de gráficos (Plotly)
        │   └── chart_service.py    # ChartService: geração dos gráficos interativos
        └── ui/                      # Componentes de interface do usuário (Streamlit)

---

## 🛠️ Configurando o Ambiente de Desenvolvimento

Para evitar o clássico problema "na minha máquina funciona", **todos devem rodar o projeto usando um Ambiente Virtual (venv)**. Siga o passo a passo:

### 1. Clonar o repositório
    git clone <COLOQUE_A_URL_DO_GITHUB_AQUI>
    cd tabelas-frequencia

### 2. Criar o Ambiente Virtual
Dentro da pasta do projeto, crie o ambiente isolado:
* **No Windows (PowerShell/CMD):**
   python -m venv .venv

* **No Mac/Linux:**
   python3 -m venv .venv

### 3. Ativar o Ambiente Virtual
Você precisa ativar o `venv` **toda vez** que for trabalhar no projeto.

* **No Windows (PowerShell/CMD):**
    .venv\Scripts\activate

* **No Mac/Linux:**
    source .venv/bin/activate

*(Se ativou corretamente, aparecerá `(venv)` no início da linha do seu terminal).*

### 4. Instalar Dependências
Com o ambiente ativado, instale as bibliotecas que usaremos (Pandas, Streamlit, Plotly, etc.):
    pip install -r requirements.txt

---

## 🚀 Como Rodar o Sistema

Sempre com o `venv` ativado, execute o Streamlit apontando para o arquivo principal, na raiz do projeto:
    
    streamlit run app.py

> ⚠️ **Nota:** o `app.py` ainda está em construção — a interface completa será implementada em breve.

Uma aba do navegador abrirá automaticamente com o sistema rodando.

---

## 🌿 Regras de Contribuição e Git (Como vamos trabalhar)

Para não sobrescrevermos o código uns dos outros, usaremos um fluxo baseado em **Pull Requests**.

1. **A branch `main` é sagrada:** Ninguém faz `git commit` ou `git push` direto na `main`. Ela deve ter sempre o código funcionando.
2. **Crie uma branch para sua tarefa:** Vai criar um botão? Consertar um cálculo? Crie uma branch a partir da `main`.
   * **Padrão de nome:** `tipo/nome-da-tarefa`
   * *Exemplos:* `feat/calculo-classes`, `fix/erro-divisao-zero`, `docs/atualiza-readme`
   * *Comando:* `git checkout -b feat/minha-tarefa`
3. **Faça os Commits:** Trabalhe na sua branch, faça os commits do seu progresso.
4. **Abra um Pull Request (PR):** Quando terminar, mande sua branch para o GitHub (`git push origin feat/minha-tarefa`) e abra um PR lá no site.
5. **Code Review:** Avise a equipe. Alguém vai ler seu código, aprovar e fazer o *Merge* para a `main`.

---

## 🧪 Rodando os Testes

Para garantir que os cálculos matemáticos não quebrem no futuro, rode nossos testes automatizados com o comando:
    
    pytest