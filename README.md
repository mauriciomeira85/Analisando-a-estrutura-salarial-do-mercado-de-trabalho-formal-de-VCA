# Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA
 Analisa a estrutura salarial do mercado de trabalho formal do  município de Vitória da Conquista (Bahia) nos anos 2015 e 2019, estabelecendo relações intra e entre  os subsetores da economia e grau de instrução. 

# 1. Introdução
   
 A estrutura salarial mostra a distribuição salarial que pode ser observada e analisada  considerando o setor econômico, subsetores , escolaridade/grau, cor/etnia, gênero, faixa etária, jornada de trabalho, dentre outros. Sob o aspecto escolaridade/grau de instrução por exemplo, são classificados em grupos ocupacionais de nível básico, que são os cargos que exigem pouca escolaridade; os de nível médio, os quais exigem no mínimo escolaridade de segundo grau e, os de nível superior, que exigem diploma de nível superior e outras qualificações. Sendo assim, esse tipo de estrutura nos permite visualizar quanto ganha cada profissão, quais profissões ganham mais, quais ganham menos, quais setores pagam mais, e, para além disso, torna possível visualizar a diferença salarial entre essas profissões, ou por setor econômico, grau de instrução e, assim, por diante. Dessa maneira, podemos nos perguntar o seguinte: por que existe diferença de salários  entre as profissões? E por que essa diferença é muito grande? Ou seja, por que uns ganham  muito mais do que os outros? Como se dá a dinâmica dos salários no mercado de trabalho?  Como funciona a dinâmica do mercado de trabalho? Bem, a estrutura salarial nos permite entender e se debruçar sobre esses questionamentos. Desse modo, esta pesquisa descreve e analisa a estrutura salarial do mercado de trabalho formal do  município de Vitória da Conquista nos anos 2015 e 2019, estabelecendo relações intra e entre os subsetores da economia e grau de instrução. A premissa do estudo é que o município possui  uma estrutura salarial intra e entre os subsetores econômicos e grau de instrução discrepante.

# 2. Objetivo

Caracterizar e analisar a estrutura salarial do mercado de trabalho formal da cidade de Vitória da Conquista, Bahia, nos anos 2015 e 2019, estabelecendo-se uma relação intra e entre os subsetores da  economia e grau de instrução, considerando apenas trabalhadores urbanos vinculados a empregador pessoa jurídica por contrato de trabalho regido, por prazo indeterminado (CLT U/PJ IND) e carga horária entre 40 e 44 horas semanais. Assim sendo, a problemática centra-se na seguinte questão: como se apresenta a estrutura salarial do mercado de trabalho formal de Vitória da Conquista nos anos 2015 e 2019 intra e entre os subsetores da economia e grau de instrução, levando em conta apenas trabalhadores CLT U/PJ IND e carga horária entre 40 e 44 horas semanais?

# 3. Justificativa
   
Esta pesquisa justifica-se pela sua viabilidade, relevância social e acadêmica. A viabilidade se dá pelo fato de ser um estudo exploratório, em que se avalia dados pré-existentes. A relevância social e acadêmica ocorre porque o trabalho abarca um conjunto considerável da população e de políticas públicas relacionados ao mercado de trabalho do município de Vitória da Conquista. Além contribuir para agregar conhecimento às teorias já existentes sobre o assunto, principalmente, conhecimento do ponto de vista empírico.


# 4. Hipótese
   
 A premissa do estudo é que o município possui uma estrutura salarial intra e entre os subsetores econômicos e grau de instrução discrepante. 


# 5. Metodologia
   
- Trabalhou-se com os microdados da Relação Anual de Informações Sociais (RAIS). A extração dos dados da RAIS seu deu através da plataforma Base dos Dados utilizando web scrapping (ou raspagem de dados), que é uma técnica para extrair dados automaticamente de sites da internet. As linguagens utilizadas na aplicação do web scrapping foram Python e SQL no ambiente jupyter notebook acessado por meio do anaconda.

- Após serem extraídos no formato xlsx no meu notebook, os dados foram carregados e concentrou-se na limpeza e tratamento deles, com a exclusão dos outliers. Os outliers são dados muito distantes da média, considerados pontos fora da curva e que enviesam a média. Assim, salários altos foram desconsiderados no cálculo da média salarial. Para identificar os outliers, utilizou-se o gráfico Boxplot, o qual permite visualizar a distribuição dos dados. Ele mostra o valor máximo; terceiro, segundo e primeiro quartil, valor mínimo e os outliers (valores discrepantes).

- Após a limpeza e tratamento dos dados, sobretudo com a exclusão dos outliers,  concentrou-se na geração das estatísticas descritivas. Esta pesquisa considera a média, mediana, desvio padrão e coeficiente de variação dos dados. Utilizou-se como parâmetro  o desvio padrão e o coeficiente de variação para entender a distribuição salarial por subsetor de atividade econômica e, assim, poder tirar conclusões acerca dessa  distribuição. A média “é o quociente da divisão da soma dos valores (dados, observações) da variável pelo número deles” (PRATES, 2017, p.81). A mediana é “definida como o número que se encontra no centro de uma série de números, estando estes dispostos segundo uma ordem (PRATES, 2017, p.81). Já o desvio padrão é “uma média quadrática dos desvios em relação à média aritmética  de um conjunto de números (PRATES, 2017, p.110). Ou seja, ele considera os desvios dos dados em relação à média. Só que, o “desvio-padrão por si só não revela muita coisa. Assim, um desvio padrão pode ser considerado pequeno para uma média e para outra é extremamente grande” (PRATES, 2017, p.113).

- Portanto, o desvio padrão pode ser considerado grande ou pequeno, dependendo da  ordem de grandeza da variável. Assim, conhecendo a ordem de grandeza do dado analisado,  podemos saber se o desvio padrão é alto ou baixo, uma vez que ele por si só não diz nada, sendo  necessário relacioná-lo com alguma coisa, neste caso a média. E uma maneira de verificarmos  isso é utilizando o coeficiente de variação, o qual é derivado da média e do desvio padrão e nos  mostra o quanto os dados variam em torno da média em termos percentuais. Assim, um coeficiente de variação menor do que 10% indicam um desvio padrão baixo. Se for 10 ≤ cv < 20, médio. Caso seja, 20 ≤ cv < 30, alto e, por fim, no caso de cv ≥ 30, muito alto.

- Utilizou-se o Excel com o auxílio do Python no Jupyter Notebook para gerar as estatísticas descritivas (média, mediana, desvio padrão e coeficiente de variação) e para criar astabelas e gráficos como forma de expor os resultados.

# 6. Técnicas e Ferramentas utilizadas
   
- Web scrapping
- Python
- SQL
- Excel
- Jupyter Notebook pelo Anaconda    
 

# 7. Análise dos Resultados
   
# 7.1  Analisando os resultados do ano de 2015

Analisando os dados, o subsetor que possui a maior remuneração média anual do  mercado de trabalho formal de Vitória da Conquista levando em conta somente funcionários com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais é o de instituições de crédito, seguros e capitalização, cujo valor é R$ 2.874,66 tomando como base uma amostra de 591 salários. A mediana é de R$ 1.674,76. A moda é R$ 788,00, que foi o salário-mínimo do  ano de 2015. O desvio padrão é R$ 2.350,85 e coeficiente de variação de 81,78%, conforme  mostra o gráfico 1:
