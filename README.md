# Salary Prediction

Esse projeto foi desenvolvido com objetivo de resolver um desafio para vaga de **Cientista de Dados Jr** requerido pelo a empresa **[GRIA](https://www.gria.io/)**.

Resumidamente, o desafio foi:

> Desenvolva um modelo de *Previsão* de salário de anúncios de empregos.

## Visão geral do Projeto

 - [Objetivo do desafio](#goal)
 - [Problema proposto](#problem)
 - [Visão geral do conjunto de dados](#data-overview)
 - [Análise preliminar do conjunto de dados](#preliminary-analysis)
 - [Tech Stack](#tech-stack)

---

<div id="goal"></div>

## Objetivo do desafio

O objetivo principal da **[GRIA](https://www.gria.io/)** era avaliar como o candidator se sairia dentro da sua função de **Cientista de Dados Jr** na empresa.

 - **Os principais *critérios de avaliação* eram:**
   - Documentação;
   - Reprodutibilidade:
     - Qualidade de reprodutível, que se pode reproduzir; que se pode exibir ou mostrar novamente.
   - Análise de código e qualidade;
   - Pipeline de modelagem;
   - Eficiência.

---

<div id="problem"></div>

## Problema proposto

Para o desafio (problema) foi considerado o conjunto de dados [Job Salary Prediction](https://www.kaggle.com/c/job-salary-prediction) disponibilizado no [Kaggle](https://www.kaggle.com/). Os objetivos e especificações descrito na competição vão ser os considerados pelo a **[GRIA](https://www.gria.io/)**.

A empresa fiadora da competição foi a [Adzuna](https://www.adzuna.co.uk/). A empresa tem um mecanismo de pesquisa novo e inovador para anúncios de *empregos*, *imóveis* e *carros*. Reunindo anúncios do mercado de centenas de fontes diferentes e, em seguida, acrescentando ferramentas úteis como redes sociais e estatísticas de mercado para ajudar os usuários a encontrar o emprego, carro ou imóvel perfeito para eles.

**SOBRE O CONJUNTO DE DADOS:**  
O conjunto de dados de avaliação era simplesmente um subconjunto aleatório de anúncios para os quais a [Adzuna](https://www.adzuna.co.uk/) sabia os salários, que não foram incluídos nos conjuntos de dados de *treinamento* e *teste público*.

> A métrica de avaliação para esta competição era o [Erro Médio Absoluto](https://en.wikipedia.org/wiki/Mean_absolute_error).

Durante a competição tiveram as seguintes étapas:
 1. Foi recebido um conjunto de dados de treinamento para construir o modelo, que incluirá todas as variáveis, incluindo salário.
 2. Um segundo conjunto de dados foi usado para fornecer feedback sobre a classificação pública.
 3. Após aproximadamente 6 semanas, o [Kaggle](https://www.kaggle.com/) liberou um conjunto de dados final que não incluia o campo de **salário** para os participantes, que então serão obrigados a enviar suas previsões salariais para cada cargo para avaliação.

**NOTE:**  
Os arquivos enviados para avaliação deveriam ser formatados da seguinte forma:
 - Ter um cabeçalho: **Id**, **SalaryNormalized**;
 - Contém duas colunas:
   - **Id:** Id para os anúncios no conjunto de validação na ordem de classificação.
   - **SalaryNormalized:** seu salário previsto para o anúncio de emprego.

**Exemplo:**  
```python
Id,       SalaryNormalized 
13656201, 36205 
14663195, 74570 
16530664, 31910,50 
```

---

<div id="data-overview"></div>

## Visão geral do conjunto de dados

O conjunto de dados principal consiste em um grande número de linhas que representam anúncios de emprego individuais e uma série de campos sobre cada anúncio de emprego.

Esses campos são os seguintes:

 - **Id**
   - Um identificador exclusivo para cada anúncio de emprego (amostra).
 - **Title**
   - Resumidamente, o Title é o resumo do cargo ou função.
 - **FullDescription**
   - O texto completo do anúncio de emprego, conforme fornecido pelo anunciante do emprego.
   - Onde teria o **salário (salary)** e foi retirado os valores da descrição para garantir que nenhuma informação de salário apareça nas descrições.
 - **LocationRaw**
   - Imagine que essa coluna representa a localização da vaga, porém, utilizando pontos cardeais e/ou referências.
 - **LocationNormalized**
   - Tem o mesmo significado da coluna LocationRaw, porém, com menos informações e referências.
   - Isso, porque essa coluna é o resultado de um Pré-Processamento da coluna LocationRaw feito pelo [Adzuna](https://www.adzuna.co.uk/).
 - **ContractType**
   - Essa coluna representa os tipos de contratos por amostra de vaga de emprego, que são **full_time** ou **part_time**.
 - **ContractTime**
   - Como vai ser o contrato que pode ser **permanente** ou **contrato**.
 - **Company**
   - O nome do empregador conforme fornecido pelo anunciante do emprego.
 - **Category**
   - Em qual das 30 categorias de empregos padrão este anúncio se encaixa, inferida de uma forma muito confusa com base na origem de onde o anúncio veio.
 - **SalaryRaw**
   - Imagine que essa coluna representa o salário do anúncio (amostra). Porém:
     - Sem formatação;
     - Com bonus;
     - Remuneração:
       - Por hora;
       - Por mês;
       - Por ano.
 - **SalaryNormalized**
   - Tem o mesmo significado da coluna "SalaryRaw", porém a Adzuna normalizou os dados para o salário ser representado de forma anualizado.
 - **SourceName**
   - O nome do site ou anunciante de quem recebemos o anúncio de emprego. 

**NOTE:**  
Todos os dados são reais, de anúncios de emprego coletados pelo a [Adzuna](https://www.adzuna.co.uk/), portanto, estão claramente sujeitos a muitos ruídos do mundo real, incluindo, mas não se limitando a: anúncios que não são do Reino Unido, salários que são declarados incorretamente, campos que estão incorretamente normalizados e anúncios duplicados.

---

<div id="preliminary-analysis"></div>

## Análise preliminar do conjunto de dados

> Nessa étapa do projeto foi feita uma **Análise preliminar do conjunto de dados** (como requisitado pelo a **[GRIA](https://www.gria.io/)**).

Os objetivos principais inicialmente seriam:

 - Análise de algum **Pré-Processamento** dos dados;
 - **Análise Estatística**.

**NOTE:**  
Vale salientar que nessa étapa não seria feita (como não foi) nenhuma alteração nos dados, apenas, análise de soluções futuras.

**Você vai poder *ver* e *entender* como foi feito esse processo clicando no *Jupyter Notebook* abaixo:**  
<a target="_blank" href="notebooks/preliminary-analysis.ipynb">
  <img src="images/jupyter-icon.ico" />
  Análise preliminar do conjunto de dados
</a>

**NOTE:**  
Outra observação aqui é que essa análise foi feita nos **dados de treino**.

---

<div id="preprocessing-ml"></div>

## Pré-Processamento & modelagem

Finalmente, nessa étapa do projeto foi feito um Pré-Processamento nas colunas (features) e em seguida feita a modelagem em vários modelos de regressão com o objetivo de encontrar o modelo com a melhor métrica **MAE (Mean absolute error)**.

**Você vai poder *ver* e *entender* como foi feito esse processo clicando no *Jupyter Notebook* abaixo:**  
<a target="_blank" href="notebooks/preprocessing-ml.ipynb">
  <img src="images/jupyter-icon.ico" />
  Pré-Processamento & Modelagem (ML)
</a>

**NOTE:**  
Essa étapa não foi finalizada por falta de tempo (pessoal, não tempo disponível pelo a GRIA) e planejamento.

---

<div id="tech-stack"></div>

## Tech Stack

 - **Python com:**
   - Scikit-Learn
   - Matplotlib
   - Seaborn
   - Pandas
   - py7zr

---

**Rodrigo Leite -** *drigols*
