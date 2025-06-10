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

### Gráfico 1: Remuneração Média Anual do mercado de trabalho formal de Vitória da Conquista por subsetor de atividade econômica no ano de 2015 considerando apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais 

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_1.png" width="120%"/>

Isso nos diz que os salários desse subsetor estão variando em torno de 81,78%. É um desvio padrão muito alto, o qual nos diz que há uma enorme variação dos dados, que estão muito afastados da média, indicando que há uma irregularidade e heterogeneidade desses dados, pois não há um padrão, uma normalidade. O gráfico 2 mostra em vermelho o coeficiente de  variação e em azul o desvio padrão dos demais subsetores analisados. 

### Gráfico 2: Coeficiente de Variação e Desvio Padrão dos subsetores analisados no ano de 2015

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/Imagem_2.png" width="120%"/>

O gráfico 2 mostra que os subsetores Instituições de Crédito, Seguros e Capitalização, Serviços Industriais de Utilidade Pública, Ensino, Transportes e Comunicações, Extrativa Mineral e Indústria Mecânica possuem um desvio padrão muito alto. Com isso, percebe-se que a distribuição salarial nesses subsetores é muito dispersa, irregular, heterogénea, em que os salários estão muito afastados da média salarial, indicando que há uma enorme diferença entre os salários e, portanto, esses subsetores apresentam individualmente uma forte desigualdade salarial.

O mesmo ocorre com os subsetores da Construção Civil, Comércio Atacadista, Comércio e Administração de Imóveis, Valores Mobiliários e Serviço Técnico, Indústria Química de Produtos Farmacêuticos, Veterinários e Perfumaria, Agricultura, Silvicultura, Criação de Animais e Extrativismo Vegetal, Indústria de Produtos Minerais Não Metálicos, Serviços Médicos, Odontológicos e Veterinários, Indústria Metalúrgica, Indústria de Produtos  Alimentícios, Bebidas e Álcool Etílico e Comércio Varejista. Estes, apresentam desvio padrão alto, sugerindo também, que cada um desses subsetores individualmente, retratam uma  dispersão nos salários em torno da remuneração média, indicando uma discrepância salarial. 

Já os ramos da Indústria da Borracha, Fumo, Couros, Peles, Similares, e Indústrias Diversas, Indústria do Papel, Papelão, Editorial e Gráfica, Serviço de Alojamento, Alimentação,  Reparação, Manutenção, Redação, Indústria da Madeira e Mobiliário, Indústria do Material Elétrico e de Comunicações e Indústria Têxtil do Vestuário e Artefatos de Tecidos demonstram um desvio padrão médio. Esse cenário sugere que esses subsetores apresentam pequena ou média variação dos dados. Assim, infere-se, que que eles apresentam uma pequena ou média diferença salarial.

Por fim, a Indústria do Material de Transporte e a Indústria de Calçados possuem desvio padrão baixo, o que indica que os salários desses subsetores estão próximos da remuneração  média que cada um apresenta, com pouca variação dos dados e, assim, diferença salarial pequena. O que demostra que a maioria das pessoas ganham próximos da remuneração média. Desse modo, a partir dos dados retratados no gráfico acima é possível visualizar a distribuição salarial de cada subsetor de maneira individual. Mas, podemos visualizar essa distribuição entre  os subsetores, estabelecendo uma relação entre eles. 

Com base no gráfico 3 pode-se examinar a concentração salarial entre os subsetores. 

### Gráfico 3: Distribuição salarial entre os subsetores da economia do mercado de trabalho formal de Vitória da Conquista no ano de 2015 considerando apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_3.png" width="120%"/>

Com base no gráfico 3, a média geral de todos os subsetores observados é de R$ 1.174,21; com desvio padrão de R$ 422,98 e coeficiente de variação em 36,02%. Esses dados nos sugerem que o desvio padrão de todos os subsetores é muito alto, uma vez que apresentam um coeficiente de variação maior do que 30%. Sendo assim, a remuneração média anual dos subsetores em análise varia em torno de 36,02% da média geral. Ou seja, esse cenário indica  uma variação muito grande dos dados, os quais demostram estar dispersos da média.

Percebe-se que há uma irregularidade e heterogeneidade desses dados, pois não há um  padrão, isto é, uma normalidade na distribuição deles. Assim, depreende-se que há uma distribuição salarial entre subsetores muito dispersa, o que sugere uma forte discrepância salarial entre os subsetores. Conforme o gráfico 3, há uma maior concentração salarial setorial  entre R$ 892,00 e R$ 1.370,80. 

Além disso, é possível observar a distribuição salarial por grau  de instrução, conforme mostra a tabela 1:

### Tabela 1: Remuneração Média Anual do mercado de trabalho formal de Vitória da Conquista por subsetor de atividade econômica e grau de instrução no ano de 2015 considerando apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais 

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_4.png" width="120%"/>

Selecionou-se uma amostra de cinco subsetores, conforme a tabela 3, e desagregou a  renda média anual por grau de instrução. Com base na tabela, observa-se que não há uma diferença muito grande de salários entre quem é analfabeto, possuem fundamental completo, médio incompleto e completo. Ou seja, os salários são próximos. E não há diferença significante  desses para quem possui superior incompleto. Inclusive, é possível notar que na indústria da madeira e mobiliário, comércio atacadista, transportes e comunicações, quem possui fundamental completo ganha mais que do médio incompleto e completo. Além disso, nota-se que os subsetores cuja pessoas possui grau de instrução completo ganha mais. O subsetor da  construção civil apresentou uma remuneração anual média maior do que os demais subsetores considerando somete quem possui nível superior.

Portanto, quando se analisa a distribuição salarial intra subsetores, é possível perceber  que 16 subsetores apresentaram um desvio padrão muito alto ou alto, sugerindo que a distribuição salarial em cada subsetor é muito dispersa, irregular, heterogénea, em que os  salários estão muito afastados da média salarial, indicando que há uma enorme diferença entre os salários e, portanto, esses subsetores apresentam individualmente uma forte desigualdade salarial. Além disso, quando se analisa a distribuição salarial entre os subsetores, ocorre o mesmo, isto é, há uma discrepância salarial entre os subsetores. 

Por fim, ao selecionar cinco subsetores e desagregar por grau de instrução, observou-se que não há muita distinção de salários entre quem é analfabeto, possuem fundamental completo, médio incompleto e completo e superior incompleto. Notou-se que em alguns casos, quem possui fundamental completo ganha mais do que médio incompleto e completo, e até do que o superior incompleto. Mas, quem possui superior completo ganha mais. 

# 7.2  Analisando os resultados do ano de 2019

Assim como em 2015, o subsetor que possui a maior remuneração média anual é o de  instituições de crédito, seguros e capitalização, com valor de R$ 6.012,02 tomando como base uma amostra de 432 salários. A mediana é de R$ 5.400,81. A moda é  R$ 998,00, que foi salário mínimo do ano de 2019. Em seguida vem os serviços industriais de utilidade pública com R$ 
2.680,88 e extrativa mineral com R$ 1.730,89. 

A partir do gráfico 4 é possível visualizar esses dados.

### Gráfico 4: Remuneração Média Anual do mercado de trabalho formal de Vitória  da Conquista por subsetor de atividade econômica no ano de 2019 considerando apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais 

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_5.png" width="120%"/>

Conforme o gráfico 4, o subsetor de instituições de crédito, seguros e capitalização vem em primeiro e destoa dos demais com uma remuneração média bem acima. Logo após, aparece os serviços industriais de utilidade pública. Perceba que do subsetor extrativa mineral até  transportes e comunicações há uma concentração de salário na entre R$ 1.669,62 e R$ 1.768,09. Mas, de modo geral, ocorre uma concentração salarial setorial entre R$ 1.339,07 e R$ 1.768,09.

O gráfico 5 nos permite visualizar a distribuição salarial de cada subsetor, através do desvio padrão e coeficiente de variação. O coeficiente de variação está em vermelho e o desvio padrão em azul.

### Gráfico 5: Coeficiente de Variação e Desvio Padrão dos subsetores analisados no ano de 2019 

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_6.png" width="120%"/>

De acordo com o gráfico, os subsetores Instituições de Crédito, Seguros e Capitalização, Serviços Industriais de Utilidade Pública, Extrativa Mineral, Transportes e Comunicações, Ensino e Construção Civil possuem um desvio padrão muito alto. Já os subsetores Indústria Química de Produtos Farmacêuticos, Veterinários e Perfumaria, Comércio Atacadista, Comércio e Administração de Imóveis, Indústria de Produtos Minerais Não Metálicos, Indústria de Produtos Alimentícios, Bebidas e Álcool Etílico, Indústria Metalúrgica, Indústria Mecânica, Indústria da Borracha, Fumo, Couros, Peles, Similares, Serviços Médicos, Odontológicos e Veterinários, Indústria do Papel, Papelão, Editorial e Gráfica e Agricultura, Silvicultura, Criação de Animais e Extrativismo Vegetal apresentam desvio padrão alto. 

Isso sugere que a distribuição salarial em cada um desses subsetores é muito dispersa, irregular, heterogénea, em que os salários estão muito afastados da média salarial, indicando que há uma enorme diferença entre os salários e, portanto, esses subsetores apresentam individualmente uma forte desigualdade salarial. Já os subsetores Indústria do Material Elétrico e de Comunicações, Comércio Varejista, Indústria da Madeira e Mobiliário, Serviço de Alojamento, Alimentação, Reparação e Indústria Têxtil do Vestuário e Artefatos de Tecidos apresentam um desvio padrão médio. Assim, esses subsetores apresentam pequena ou média variação dos dados. Dessa maneira, conclui-se, que que eles apresentam uma pequena ou média diferença salarial.

Por fim, a Administração Pública Direta e Autárquica, a Indústria de Calçados e Indústria do Material de Transportes mostram desvio padrão baixo, o que indica que os salários desses subsetores estão próximos da remuneração média que cada um apresenta, com pouca variação dos dados e, assim, diferença salarial pequena. Sendo assim, a partir do gráfico 5, conseguimos visualizar a distribuição salarial de cada subsetor de maneira individual.

Mas, podemos visualizar essa distribuição entre os subsetores, estabelecendo uma relação entre eles. 
Com base no gráfico 6 pode-se examinar a concentração salarial entre subsetores.

### Gráfico 6: Distribuição salarial entre os subsetores da economia do mercado de trabalho formal de Vitória da Conquista no ano de 2019 considerando apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_7.png" width="120%"/>

De acordo com o gráfico 11, a média de todos os subsetores observados é de R$ 1.611,44 com desvio padrão de R$ 970,06 e coeficiente de variação em 60,20%. Ou seja, percebe-se que  é um desvio padrão muito alto, visto que apresenta um coeficiente de variação maior do que  30%. Isso significa que a remuneração média anual dos subsetores em análise varia em torno de 60,20% da média geral. Sendo assim, há variação muito grande dos dados, os quais demostram estarem dispersos da média. Percebe-se que há uma irregularidade e heterogeneidade desses dados, pois não há um padrão, isto é, uma normalidade na distribuição deles. Portanto, infere-se que há uma distribuição salarial entre subsetores muito dispersa, o que sugere uma forte discrepância salarial entre os subsetores.Conforme o gráfico 6, há uma maior concentração salarial setorial entre R$ 1.339,07 e R$ 1.768,09.  

Outrossim, podemos observar a distribuição salarial por grau de instrução, conforme mostra a tabela 2:

### Tabela 2: Remuneração Média Anual do mercado de trabalho formal de Vitória da Conquista por subsetor de atividade econômica e grau de instrução no ano de 2019 considerando apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais 

<img src="https://github.com/mauriciomeira85/Analisando-a-estrutura-salarial-do-mercado-de-trabalho-formal-de-VCA/blob/main/Imagens/imagem_8.png" width="120%"/>

Assim como em 2015, para 2019 foi selecionado uma amostra de cinco subsetores, conforme a tabela acima, e desagregou a renda média anual por grau de instrução.  A análise não muda muito com relação a 2015. Pela tabela 3 verifica-se que não há uma diferença muito grande de salários entre quem é analfabeto, possuem fundamental completo, médio incompleto e completo. E assim como em 2015, em 2019 notou-se que nos subsetores indústria da madeira e mobiliário, comércio atacadista, transportes e comunicações, quem possui fundamental completo ganha mais que médio incompleto e completo. E não há diferença significante desses para quem possui superior incompleto, embora em certos casos que está cursando algum curso superior em andamento ganha mais, porém em outros, menos. Ademais, observa-se que os subsetores cuja pessoas possui grau de instrução completo ganha mais, porém em outros menos. 

Portanto, com base nos dados, percebe-se que 17 subsetores  apresentaram um desvio padrão muito alto ou alto, sugerindo que a distribuição salarial em cada subsetor é muito dispersa, irregular, heterogénea, em que os salários estão muito afastados da média salarial, apontando que há uma enorme diferença entre os salários e, portanto, esses subsetores apresentam individualmente uma forte desigualdade salarial. No momento em que se analisa a distribuição entre os subsetores, ocorre o mesmo. Isto é, há uma disparidade salarial entre os subsetores.

Para terminar, ao selecionar cinco subsetores e desmembrar por grau de instrução, observou-se que não há muita distinção de salários entre quem é analfabeto, possuem fundamental completo, médio incompleto e completo e superior incompleto. Contudo, teve subsetores que o fundamental completo ganhava mais do que o médio incompleto e completo, e até do que o superior incompleto. Ademais, quem possui superior completo ganha mais.

# 7. Considerações Finais

Desse modo, esta pesquisa constatou-se que que, ao analisar  essa distribuição intra subsetores, em alguns subsetores a discrepância salarial foi maior em 2019 do que em 2015, mas em outros foi menor. Em 2015, 16 subsetores e em 2019, 17 subsetores apresentaram um desvio padrão muito alto ou alto, sugerindo que a distribuição salarial em cada subsetor é muito dispersa, irregular, heterogénea, em que os salários estão muito afastados da média salarial, apontando que há uma enorme diferença entre os salários e, portanto, esses subsetores apresentam individualmente uma forte desigualdade salarial.

No momento em que se analisa a distribuição entre os subsetores, ocorre o mesmo, ou seja, ao relacionar a distribuição salarial dos subsetores entre si, percebe-se que há discrepância salarial. Isto é, há uma disparidade salarial entre os setores. Essa discrepância aumentou de 2015 para 2019, visto que enquanto em 2015 os dados variaram 36,02%, em 2019 a variação foi de 60,20%, ou seja, houve uma maior variação dos dados em 2019 do que em 2015 e, portanto, ocorreu um aumento da desigualdade salarial entre os subsetores nesse período. 

Além disso, ao selecionar cinco subsetores e desmembrar por grau de instrução, observou-se que não há muita distinção de salários entre quem é analfabeto, possuem fundamental completo, médio incompleto e completo e superior incompleto. Contudo, teve subsetores que o fundamental completo apresentou salários maiores que o médio completo e incompleto, e até que o superior incompleto. Além disso, quem possui superior completo ganha mais.

Dessa forma, os resultados validam a hipótese de que Vitória da Conquista possui em seu mercado de trabalho formal uma distribuição salarial desigual intra e entre os subsetores econômicos e grau de instrução, considerando o período analisado, e levando em conta apenas trabalhadores com vínculo CLT U/PJ IND e carga horária entre 40 e 44 horas semanais. Consta se ainda que a diferença salarial intra subsetores aumentaram de 2015 para 2019 em alguns subsetores, mas em outros não. Outrossim, ocorreu um aumento da desigualdade salarial entre  os subsetores de 2015 a 2019. Conforme os dados, pessoas que possuem médio completo, superior incompleto ou completo tende a ganha mais, com algumas exceções, visto que teve casos que o fundamental completo ganhava mais. Nos setores que têm como característica demandar mão de obra qualificada, a diferença salarial foi bem maior.









