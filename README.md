# Análise de Venda de Motos Usadas

Dashboard interativo em Streamlit que analisa um conjunto de dados de motocicletas seminovas à venda e responde perguntas de negócio sobre preço, quilometragem, tipo de vendedor e fabricante.

**[▶ Acessar o dashboard](https://ygormikassio-cds-curso-git-app-nmjm92pxehpfdjtudwze.streamlit.app/)**

---

## O problema

Quem compra ou revende moto usada decide quase sempre no achismo: não é óbvio se rodagem alta realmente derruba o preço, se moto de dono único vale o prêmio que se cobra, ou quais marcas concentram as melhores oportunidades.

Este projeto transforma uma base bruta de anúncios em respostas objetivas para essas perguntas.

## Perguntas respondidas

Quantas motos são vendidas pelos próprios donos e quantas por revendedores?

Quantas das motos anunciadas tiveram um único dono?

Motos com quilometragem alta são mais caras que as de quilometragem baixa?

Motos de dono único são, em média, mais caras que as demais?

Qual fabricante tem mais motos registradas na base?

Qual fabricante tem as motos mais caras em média — e é o mesmo que tem mais motos registradas?

Quais motos são boas oportunidades de compra?

## Como funciona

```
data/raw/          bike.csv + companies.csv (dados brutos)
      |
      v
notebooks/         tratamento, limpeza e criação de variáveis
      |            (km_class, km_per_year, km_per_month, company)
      v
data/processed/    bikes_completed.csv (base final)
      |
      v
src/               extraction.py (carga) + answers.py (análises)
      |
      v
app.py             dashboard Streamlit
```

A base bruta é enriquecida com variáveis derivadas — faixa de quilometragem, média de quilômetros por ano e por mês, e o fabricante extraído do nome do anúncio — antes de alimentar o dashboard.

## Stack

Python · pandas · plotly · Streamlit · Jupyter

## Como executar localmente

```bash
git clone https://github.com/ygormikassio/cds_curso_git.git
cd cds_curso_git
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura

`app.py` — layout e seções do dashboard

`src/extraction.py` — carga da base tratada

`src/answers.py` — funções de análise e gráficos

`notebooks/` — exploração e tratamento dos dados

`data/` — dados brutos e processados

## Contexto

Projeto desenvolvido durante a formação em Análise de Dados da Comunidade DS, também utilizado como base para o aprendizado de Git e trabalho colaborativo com branches e resolução de conflitos.

## Licença

MIT
