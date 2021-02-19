import pandas as pd
import enviarEmail as ee

#Lendo a tabela do excel e colocando na variável tabela_vendas
tabela_vendas = pd.read_excel(r'Vendas.xlsx')

#Criando a tabela do faturamento das lojas
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
faturamento = faturamento.sort_values(by='Valor Final', ascending=False)

#Criando a tabela da quantidade de vendas
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
quantidade = quantidade.sort_values(by='ID Loja', ascending=False)

#Criando a tabela do ticket médio (faturamento / quantidade)
ticketMedio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticketMedio = ticketMedio.rename(columns={0 : 'Ticket Médio'})
ticketMedio = ticketMedio.sort_values(by='Ticket Médio', ascending=False)

#Enviar o relatório da loja
lojas = tabela_vendas['ID Loja'].unique()

#Agrupando o relatório das lojas e enviando para determinado e-mail (para enviar para e-mails diferentes, necessitaria
#de uma lista de todos os e-mails)
for loja in lojas:
    tabela_loja = tabela_vendas.loc[tabela_vendas['ID Loja'] == loja, ['ID Loja', 'Quantidade', 'Valor Final']]
    resumo_loja = tabela_loja.groupby('ID Loja').sum()
    resumo_loja['Ticket Médio'] = resumo_loja['Valor Final'] / resumo_loja['Quantidade']
    ee.enviarEmail(resumo_loja, loja)

#Enviar o relatório das lojas para a diretoria
tabela_diretoria = faturamento.join(quantidade).join(ticketMedio)
ee.enviarEmail(tabela_diretoria, 'Todas as Lojas')