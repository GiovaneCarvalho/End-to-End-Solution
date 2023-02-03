from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv('Dados_livros.csv', on_bad_lines='skip', sep=';')
''' Nome de usuário, senha, a porta do local host e o nome do database'''
#engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

print(df.sort_values(by ='0'))

str = 'XXXXXX'

df.rename(columns={"0":'nome_livro', "1": 'valor', "2": 'nota', "3":'em_estoque', "4": 'classificacao', "5":'comentarios'}, inplace = True)
engine = create_engine(str)
df.to_sql('Books_Data', engine,
            if_exists="replace", index = False)

