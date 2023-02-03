# End to end - Data Engineering & Data Science
 
O projeto é baseado em uma sugestão de um artigo do Medium, sobre projetos de portifólio para Data Engineering. O mercado de dados está em alta e muito se discute sobre cargos como engenheiros de dados, analista de dados, engenheiro de machine learning, cientista de dados e muitas outras funções.

Empresas tentam embalar na crista da onde contratando diversos cientistas de dados. Este, porém, é um movimento equivocado. Muitas destas mesmas empresas estão um grau de maturidade muito inferior, onde não há dados dispovíveis para análise ou, se há, estão altamente restritos.

Este fato leva a outro movimento de mercado: Cientista de dados se convertendo em Engenheiro de Dados. A falta de disponibilidade de dados para analise combinada com a cobrança por resultados leva o cientista de dados a ter uma independência muito grande, precisando aprender ferramentas e meios de ingerir, tratar e disponibilizar o dado para que possa realizar o seu trabalho de analise e previsão.

Este projeto se baseia na exploração dos conhecimentos de engenharia de dados, partindo da ingestão via web scrapping de um site de troca de livros, partindo para a limpeza dos valores e posteriormente a carga dentro de um DBT, neste caso o PostgreSQL. Além disso, o projeto vai além e explora os passos seguintes, partindo para uma análise exploratória dos dados dos livros e posteriormente para a criação de um sistema de recomendação misto, indicando para os usuários quais livros eles estão mais propensos a gostar, a partir de um livro já conhecido.

Por último, buscou-se uma maneira de deixar esses dados disponíveis para o usuário final. A ferramenta escolhida foi o Power BI e o painel com as recomendações pode ser acesso via: https://app.powerbi.com/view?r=eyJrIjoiYjFhMGFiYjAtZDdkNC00MGNhLWFiYzctZTFlZTZjZGJmYjc5IiwidCI6ImMyZjBkMDYxLWE3ZmYtNGExMi1iYTdkLWNiYjEyZTliMTljMCJ9