import pandas as pd

print('Leia o arquivo DadosEmpresa.csv')
dados_emp_df = pd.read_csv("DadosEmpresa.csv")#le o arquivo csv e salva em um dataframe
print(dados_emp_df)

print('Print no terminal as colunas do arquivo DadosEmpresa')
print(dados_emp_df.columns)#.columns retorna os rotulos do dataframe

print('Print no terminal as primeiras linhas do arquivo DadosEmpresa')
print(dados_emp_df.head())#.head() retorna as n primeiras linhas sendo por padrao n=5

print('Print no terminal o total de empresas do arquivo DadosEmpresa que tem a coluna "opcao_pelo_simples" com o valor "SIM"')
#.loc[] acessa um grupo de linhas e colunas pelo rótulo e retorna de acordo com as restrições desejadas
#len()calcula o comprimento da serie
#.value_counts() retorna uma serie contendo a contagem das linhas de um dataframe
print(len(dados_emp_df.loc[dados_emp_df['opcao_pelo_simples'] == 'SIM'].value_counts())) 

print('Print no terminal a soma do "capital_social" de todas as empresas;')
print(dados_emp_df['capital_social'].sum())#.sum() soma os valores da série

print('Print no terminal todas as empresas que tem "capital_social" maior que 10.000 e menor que 20.000')
#.loc[] acessa um grupo de linhas e colunas pelo rótulo e retorna de acordo com as restrições desejadas
print(dados_emp_df.loc[dados_emp_df['capital_social'] > 10000].loc[dados_emp_df['capital_social'] < 20000])

print('EXTRA: Leia o arquivo "DadosEndereco.csv"')
dados_end_df = pd.read_csv("DadosEndereco.csv")#le o arquivo csv e salva em um dataframe
print(dados_end_df)

print('EXTRA: Faça um merge entre os dois arquivos pela coluna "cnpj" e salve um arquivo CSV com todas as empresas que são de "CURITIBA"')
dados_emp_df = dados_emp_df.merge(dados_end_df)#.merge() une dataframe a partir de colunas iguais
#.to_csv() salva o dataframe em um arquivo csv sem os valores de indice
dados_emp_df.loc[dados_emp_df['municipio'] == 'CURITIBA'].to_csv('empresas_curitiba.csv', index=False)
print(dados_emp_df.loc[dados_emp_df['municipio'] == 'CURITIBA'])
